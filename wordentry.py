class Word:
    def __init__(self):
        self.definition: list = []
        self.translation: list = []
        self.sentences: dict = {}
    
    def new_word(self, definition, translation, sentence, english_sentence):
        if not (isinstance(definition, str))

    def set_definition(self, definition):
        if len(self.definition) > 5:
            return
        if not isinstance(definition, str):
            return
        self.definition.append(definition)

    def set_translation(self, translation):
        if len(self.translation) > 5:
            return
        if not isinstance(translation, str):
            return
        self.translation.append(translation)

    def set_sentence(self, sentence, english_sentence):
        if len(self.sentences) > 5:
            return
        if not isinstance(sentence, str):
            return
        if not isinstance(english_sentence, str):
            return
        sentences = self.sentences
        sentences[sentence] = english_sentence