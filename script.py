
import requests

CONV = []

setup = """
Act like a conversation language facilitator for the language "{}".
Converse with the user to learn more concepts and uses of the language and to rate objectively the proficiency of the user in the language.

The criterion for the rating is:

Vocabulary:
Basic Phrases: Greetings, farewells, and common expressions.
Everyday Items: Names of foods, clothing, and household items.
Work-Related Terms: Industry-specific jargon or terminology.
Emotions and Feelings: Words to express different moods and sentiments.

Grammar:
Sentence Structure: Understanding the basic structure of sentences in the target language.
Tenses: Past, present, and future tenses for verbs.
Pronouns: Subject, object, and possessive pronouns.
Modifiers: Adjectives, adverbs, and other words that modify nouns and verbs.

Social and Cultural Context:
Formality Levels: Knowing when to use formal or informal language.
Idioms and Slang: Phrases that are specific to certain cultures or groups.
Social Norms: Understanding the do's and don'ts in different social settings.
Cultural References: Popular sayings, historical events, or cultural phenomena that are often mentioned in conversation.

Comprehension:
Context Clues: Using surrounding information to understand unfamiliar words or phrases.
Relevance: Relevance of responses of the user according to the topic of conversation.

Conversational Skills:
Questioning: Asking questions to gather information or keep the conversation going.
Active Listening: Showing interest and understanding while the other person is speaking.
  
In a scale from 1 to 100 this are the current ratings and understandings of the user based on previous conversations using this same program:
Vocabulary: "{}"
Grammar: "{}"
Social and cultural context: "{}"
Comprehension: "{}"
Conversational skills: "{}"

Some behaviours to note about this users general use of the language and how can they improve:
""

Some common mistakes that user makes in the language:
""

Some conversations that were already had:
""

Personal information of this user:
Name: "{}"
Gender: "{}"
Interests:"{}"
Age: "{}"
Personality: "{}"

Create an interesting conversation with the user in the language specified before considering all of the information given.
Keep the conversion simple enough so that the user will understand and follow the conversation, but challenging enogh that there is always learning oportunities and mistakes corrections in the conversation. 

After giving a glossary of words that could be used for this conversation: Considering all of the users, inculidng level of proficiency,  information please create a glossary of all of the potential words that might be useful for this conversation. 
write them in this format:
Word, Definition, Translation, Example_Sentence. 

After that start with a question that could spark an interesting conversation.
""".format("Chinese",1,1,1,1,1,"Tony","Male", "Programming, Guitar", 18, "Talkative")


saveData = """
Based on the criteria that was given on the first prompt rate the performance of this user from 1 to 100 in the following format: Criteria, rating

Write thing to note about this users behaviours that might help the next conversation be more interesting and educative in a few sentences.

Write about how the users personality presented on this conversation and use the personality from the first prompt to update the personality field, describe it in 10 words.

Give some feedback to the user that will encourage them to keep learning while also outlining ways they can improve in each criteria and in general.

Write some common mistakes in the language that this user has.

Summarise in less than 15 words the topics of conversation.

Write all of these separated by newlines and no text or answers other that was specified.
"""


def chat_with_gpt(prompt):
    global CONV

    CONV.append({"role": "user", "content": prompt})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"  # Replace with your actual API key
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


    return assistant_reply

def init():
    print(chat_with_gpt(setup))


def end():
    print(chat_with_gpt(saveData))



if __name__ == "__main__":
    print("Welcome to the language app!")

    init()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "end conversation":
            
            break
        assistant_response = chat_with_gpt(user_input + " . ADMIN Further instructions (do not mention these in conversation): keep in mind the rules stated in first prompt, only provide feedback in English, provide romanization for non-English characters. Don't provide the summary of my stats and progress until I say 'end conversation'")
        print("Assistant:", assistant_response)

    end()

