import json

class PersonalInfo:
    def __init__(
        self,
        language,
        name,
        gender,
        interests,
        age,
        personality,
        mistakes,
        past_conversation,
        behaviours
    ):
        self.language = language
        self.name = name,
        self.gender = gender,
        self.interests = interests,
        self.age = age,
        self.personality = personality,
        self.mistakes = mistakes,
        self.past_conversation = past_conversation,
        self.behaviours = behaviours

    def get_language(self):
        return str(self.language)

    def get_name(self):
        return str(self.name)

    def get_gender(self):
        return str(self.gender)

    def get_interests(self):
        return ', '.join(str(i) for i in self.interests)

    def get_age(self):
        return str(self.age)

    def get_personality(self):
        return str(self.personality)

    def get_mistakes(self):
        return str(self.mistakes)

    def get_past_conversation(self):
        return str(self.past_conversation)

    def get_behaviours(self):
        return str(self.behaviours)
        
    def set_language(self, language):
        self.language = str(language)

    def set_name(self, name):
        self.name = str(name)

    def set_gender(self, gender):
        self.gender = str(gender)

    def set_interests(self, interests):
        if isinstance(interests, list):
            self.interests = interests
        else:
            self.interests = None

    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            self.age = None

    def set_personality(self, personality):
        self.personality = str(personality)

    def set_mistakes(self, mistakes):
        self.mistakes = str(mistakes)

    def set_past_conversation(self, past_conversation):
        self.past_conversation = str(past_conversation)

    def set_behaviours(self, behaviours):
        self.behaviours = str(behaviours)

    @staticmethod
    def dump_to_json(json_file_path, interests, personality, mistakes, past_conversation, behaviours):
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if not interests is None:
                data["user_information"]["personal_information"]["interests"] = interests
            if not personality is None:
                data["user_information"]["personal_information"]["personality"] = personality
            if not mistakes is None:
                data["user_information"]["personal_information"]["mistakes"] = mistakes
            if not past_conversation is None:
                data["user_information"]["personal_information"]["past_conversation"] = past_conversation
            if not behaviours is None:
                data["user_information"]["personal_information"]["behaviours"] = behaviours

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    

    
class LanguageProficiency:
    def __init__(
        self,
        vocabulary,
        grammar,
        social_cultural_context,
        comprehension,
        conversation_skills
    ):
        self.vocabulary = vocabulary
        self.grammar = grammar
        self.social_cultural_context = social_cultural_context
        self.comprehension = comprehension
        self.conversation_skills = conversation_skills

    def get_vocabulary(self):
        return self.vocabulary

    def set_vocabulary(self, vocabulary):
        if isinstance(vocabulary, int):
            self.vocabulary = vocabulary
        else:
            self.vocabulary = None

    def get_grammar(self):
        return self.grammar

    def set_grammar(self, grammar):
        if isinstance(grammar, int):
            self.grammar = grammar
        else:
            self.grammar = None

    def get_social_cultural_context(self):
        return self.social_cultural_context

    def set_social_cultural_context(self, social_cultural_context):
        if isinstance(social_cultural_context, int):
            self.social_cultural_context = social_cultural_context
        else:
            self.social_cultural_context = None

    def get_comprehension(self):
        return self.comprehension

    def set_comprehension(self, comprehension):
        if isinstance(comprehension, int):
            self.comprehension = comprehension
        else:
            self.comprehension = None

    def get_conversation_skills(self):
        return self.conversation_skills

    def set_conversation_skills(self, conversation_skills):
        if isinstance(conversation_skills, int):
            self.conversation_skills = conversation_skills
        else:
            self.conversation_skills = None

    def dump_to_json(self, json_file_path):
        newdata = {
            "vocabulary": self.vocabulary,
            "grammar": self.grammar,
            "social and cultural context": self.social_cultural_context,
            "comprehension": self.comprehension,
            "conversational skills": self.conversation_skills
        }
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            data["user_information"]["language_proficiency"].update(newdata)

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            

    
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
