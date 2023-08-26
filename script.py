import re
import requests
from key import KEY
import userinfo
import matplotlib.pyplot as plt
import datetime
import pickle
import os

SECRET_KEYWORD = "ADMIN"
ERROR_RECORD_MSG = "[Due to an error, this message was not recorded]"
PROMPT_FOLDER = "src/prompts/"

#USR_JSONPATH = "usrdata.json"

def get_picklefile(username):
    return "users/" + username + "/data.pkl"

def make_conversation_file(username):
    path_to_user_folder = "users/" + str(username)
    path_to_user_history = path_to_user_folder + "/history"

    if not os.path.exists(path_to_user_folder):
        os.makedirs(path_to_user_folder)
    if not os.path.exists(path_to_user_history):
        os.makedirs(path_to_user_history)
    numConversations = len([f for f in os.listdir(path_to_user_history) if os.path.isfile(os.path.join(path_to_user_history, f))])
    path_to_new_conversation = path_to_user_history + "/Conversation" + str(numConversations+1) + ".txt"
    with open(path_to_new_conversation, "w"):
        pass
    return path_to_new_conversation


class DataStorage:
    def __init__(self):
        self.data = {}

    def add_entry(self, timestamp, values):
        self.data[timestamp] = values

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.data, f)

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            self.data = pickle.load(f)

    def getKeys(self):
        return self.data.keys()

    def getValues(self):
        return self.data.values()

def get_pickled_data(username):
    datastorage = DataStorage()
    if os.path.exists(get_picklefile(username)):
        datastorage.load_data(get_picklefile(username))
    return datastorage

# graph = {}

# potentially useless user info= personality, gender, past conversations
CONV = []

conv_for_history = ""

# def format_glossary(string : str):
#     '''
#     takes the raw message sent by the AI, and formats it into a list of words
#     '''
#     raw_glossary, dump = re.split("----------", string)

#     for line in raw_glossary.split("\n"):

#         line.split




# def update_glossary():
#     pass

def find_line_with_regex(text, regex_pattern):
    lines = text.split('\n')
    for line in lines:
        if re.match(regex_pattern, line):
            formatted_string = line.strip()
            formatted_string.replace(regex_pattern, "").strip()
            return formatted_string
    return None


def dump_personal_summary(text, json_filepath):
    interests = find_line_with_regex(text, "Interests: ")
    if not interests is None:
        interests = personality.split(", ")
    personality = find_line_with_regex(text, "Personality: ")
    if not personality is None:
        personality = personality.split(", ")
    behaviour = find_line_with_regex(text, "Behaviour: ")
    if not behaviour is None:
        behaviour = behaviour.split(", ")
    mistakes = find_line_with_regex(text, "Mistakes: ")
    if not mistakes is None:
        mistakes = mistakes.split(", ")
    past_conversation = find_line_with_regex(text, "Conversation topics: ")
    userinfo.PersonalInfo.dump_to_json(
        json_file_path=json_filepath,
        interests=interests,
        personality=personality,
        behaviours=behaviour,
        mistakes=mistakes,
        past_conversation=past_conversation)

def make_initial_prompt(usr_jsonpath):
    # PERSONAL_INFO = (1,1,1,1,1, "Complete beginner", "Grammatical errors", "None", "John", "Male", "Guitar, programming, AFL", "45", "Outgoing")
    personal_info = userinfo.get_user_personal_details(usr_jsonpath)
    user_proficiency = userinfo.get_user_language_proficiency(usr_jsonpath)

    f = open(PROMPT_FOLDER + "security.txt")
    SECURITY = f.read().format(**personal_info)
    f.close()

    f = open(PROMPT_FOLDER + "criterion.txt")
    CRITERION = f.read()
    f.close()

    f = open(PROMPT_FOLDER + "personal.txt")
    PERSONAL = f.read().format(**personal_info, **user_proficiency)
    f.close()

    f = open(PROMPT_FOLDER + "convo.txt")
    CONVO = f.read()
    f.close()

    return (SECURITY, CRITERION, PERSONAL, CONVO)


def chat_with_gpt(prompt, recordPrompt:bool=True, recordReply:bool=True):

    global CONV, conv_for_history

    CONV.append({"role": "user", "content": prompt})

    if recordPrompt:
        try:
            toRecord = prompt.split(SECRET_KEYWORD)[0]
            conv_for_history += (toRecord + "\n")
        except:
            conv_for_history += (ERROR_RECORD_MSG + "\n")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + KEY  # Replace with your actual API key
    }
    data = {
        "messages": CONV,
        "model": "gpt-4"
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    # print(response_json)


    # The structure of the response might have changed
    assistant_reply = response_json["choices"][0]["message"]["content"] if "choices" in response_json else ""
    #assistant_reply = response_json
    #CONV.append(response_json["message"][-1])
    CONV.append({"role": "assistant", "content": assistant_reply})
    if recordReply:
        conv_for_history += (assistant_reply + "\n")


    return assistant_reply

def getTTSString(reply):

    pattern = r'>>>(.*?)<<<'
    match = re.search(pattern, input_text, re.DOTALL)

    if match:
        TTSString = match.group(1).strip()
    else:
        TTSString = " "

    return TTSString


def init(username):
    usr_jsonpath = os.path.normpath(f"users/{username}/usrdata.json")
    SECURITY, CRITERION, PERSONAL, CONVO = make_initial_prompt(usr_jsonpath=usr_jsonpath)
    chat_with_gpt(SECURITY, False, False)
    chat_with_gpt(CRITERION, False, False)
    chat_with_gpt(PERSONAL, False, False)
    initial_text = chat_with_gpt(CONVO, False, True)
    print(initial_text)
    return initial_text

def end(lastInput, username) -> str:
    global FINAL
    usr_jsonpath = os.path.normpath(f"users/{username}/usrdata.json")
    datastorage = get_pickled_data(username)

    f = open(PROMPT_FOLDER + "final_prompt.txt")
    FINAL = f.read()
    f.close()
    summary = chat_with_gpt(FINAL)
    print(summary)

    lines = []

    for line in summary.split("\n"):
        if line.strip():
            lines.append(line)

    try:
        statsLines = lines[:5]
    except:
        statsLines = []

    stats = []
    for statsLine in statsLines:
        try:
            num = int(statsLine.split(",")[1].strip())
        except:
            num = 1
        stats.append(num)

    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time().replace(microsecond=0))
    timestamp = date + " " + time

    dump_personal_summary(summary, usr_jsonpath)
    updated_stats = userinfo.LanguageProficiency(stats[0], stats[1], stats[2], stats[3], stats[4])
    updated_stats.dump_to_json(usr_jsonpath)
    datastorage.add_entry(timestamp, stats)

    if lastInput == "graph":

        # Extract timestamps and values from the dictionary
        # graph = {
        #     '2023-08-26 20:59:48': [25, 25, 15, 30, 30],
        #     '2023-08-26 21:59:48': [30``, 27, 16, 30, 50],
        #     '2023-08-26 22:59:48': [40, 30, 20, 40, 70],
        #     '2023-08-26 23:59:00': [61, 35, 54, 41, 95]
        # }

        timestamps = list(datastorage.getKeys())
        values = list(datastorage.getValues())

        # Transpose the values to separate the 5 elements into different lists
        transposed_values = list(zip(*values))

        # Labels for the line graphs
        labels = [
            "Vocabulary",
            "Grammar",
            "Social & Cultural Context",
            "Comprehension",
            "Conversational Skills"
        ]

        # Create a line plot for each element with appropriate label
        for i, value_list in enumerate(transposed_values):
            plt.plot(timestamps, value_list, marker='o', label=labels[i])

        plt.xlabel("Timestamps")
        plt.ylabel("Values")
        plt.title("User {}'s Progress".format(username))
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()



        plt.savefig("users/{}/out.png".format(username))

        # print(graph)

    datastorage.save_data(get_picklefile(username=username))

    return summary


if __name__ == "__main__":

    init()

    while True:

        user_input = input("You: ")
        if user_input.lower() == "explain":
            f = open(PROMPT_FOLDER + "explain.txt")
            EXPLAIN = f.read()
            f.close()
            user_input = EXPLAIN
        if user_input.lower() == "end conversation":
            break
        if user_input.lower() == "graph":
            break

        if user_input.lower() == "":
            print("Assistant: Sorry, I cannot interpret a blank message")
        assistant_response = chat_with_gpt(user_input + " . ADMIN Further instructions (do not mention these in conversation): keep in mind the rules stated in first prompt, only provide feedback in English, provide romanization for non-English characters. Don't provide the summary of my stats and progress until I say 'end conversation'. Surround the dialogue in other language with >>> and <<<, for example >>> hola, como estas <<<.")
        print("Assistant:", assistant_response)

        TTSString = getTTSString(assistant_response)



    end(user_input.lower())
