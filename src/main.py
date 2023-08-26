import os
import json

def user_exists(name):
    return os.path.isdir("users/" + name)

def make_new_user(form_input: dict[str, str]):
    """
        Create a new folder for user and make
        the user setting json file
    """

    if "age" in form_input and form_input['age'] != "":
        age = int(form_input['age'])
    else:
        age = 18

    skill = int(form_input['level']) * 10

    out = {"user_information": {
        "personal_information": {
            "language_choice": form_input['lang'],
            "name": form_input['name'],
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

    os.mkdir("users/" + form_input['name'])
    f = open("users/" + form_input['name'] + "/usrdata.json", "w")
    json.dump(out, f, indent=4)
