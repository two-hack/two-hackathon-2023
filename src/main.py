import os
import re
import json

def user_exists(name):
    if not os.path.isdir("users"):
        os.mkdir("users")

    return os.path.isdir("users/" + name)

def make_new_user(form_input: dict[str, str]):
    """
        Create a new folder for user and make
        the user setting json file
    """

    name = form_input['name'].lower().strip()

    if "age" in form_input and form_input['age'] != "":
        age = int(form_input['age'])
    else:
        age = 18

    skill = int(form_input['level']) * 10

    out = {"user_information": {
        "personal_information": {
            "language_choice": form_input['lang'],
            "name": name,
            "gender": "Male",
            "interests": form_input['interests'].split(),
            "age": age,
            "personality": None,
            "mistakes": None,
            "past_conversation": None,
            "behaviours": None
        },
        "language_proficiency":{
            "vocabulary": skill,
            "grammar": skill,
            "social and cultural context": skill,
            "comprehension": skill,
            "conversational skills": skill
        }
    }}

    os.mkdir("users/" + name)
    f = open("users/" + name + "/usrdata.json", "w")
    json.dump(out, f, indent=4)

def parse_respone(respone:str):
    """replaces \\n and other md things with html tag"""
    respone = respone.replace("\n", "<br>")
    respone = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', respone)
    respone = re.sub(r'\*(.*?)\*', r'<i>\1</i>', respone)
    print(respone)
    return respone
