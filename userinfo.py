import json
json_file_path = "usrdata.json"

def get_user_personal_details(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
        personal_info = data["user_information"]["personal_information"]
        language_choice = personal_info["language_choice"]
        name = personal_info["name"]
        gender = personal_info["gender"]
        interests = personal_info["interests"]
        age = personal_info["age"]
        personality = personal_info["personality"]
        behaviour = personal_info["behaviours"]
        mistakes = personal_info["mistakes"]
        past_conversation = personal_info["past_conversation"]
        
        user_details = {
            "language_choice": language_choice,
            "name": name,
            "gender": gender,
            "interests": interests,
            "age": age,
            "personality": personality,
            "behaviour": behaviour,
            "mistakes": mistakes,
            "past_conversation": past_conversation
        }
        
        return user_details
    
def get_user_language_proficiency(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
        language_proficiency = data["user_information"]["language_proficiency"]
        
        user_language_proficiency = {
            "vocabulary": language_proficiency["vocabulary"],
            "grammar": language_proficiency["grammar"],
            "social and cultural context": language_proficiency["social and cultural context"],
            "comprehension": language_proficiency["comprehension"],
            "conversational skills": language_proficiency["conversational skills"]
        }
        
        return user_language_proficiency

# Replace 'your_json_file.json' with the actual path to your JSON file
json_file_path = "usrdata.json"
