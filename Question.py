"""
FelipdelosH
2023

This is a model to 

"""
class Question(object):
    def __init__(self, bot_response, list_of_words, single_response, required_words) -> None:
        self.bot_response = bot_response
        self.list_of_words = list_of_words
        self.single_response = single_response
        self.required_words = required_words
        