import os

def user_exists(name):
    return os.path.isdir("users/" + name)

def make_new_user(form_input: dict):
    """
        Create a new folder for user and make
        the user setting json file
    """
    os.mkdir("users/" + form_input['name'])

    f = open("users/" + form_input['name'] + "/usrdata.json", "w")

