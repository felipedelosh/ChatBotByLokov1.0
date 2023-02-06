"""
FelipedelosH

This is a Chatbot load controller

"""

import os # To know path project
from os import scandir
import re
import random
from Question import *
import json

class Controller:
    def __init__(self) -> None:
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        # Load all Questions
        self.questions = []
        self._loadAllQuestions()
        self.chat_historial = ""
        


    def getIMGRouteOfFempuradora(self):
        

        return self.pathProject + "\\Resources\\img\\femputadora.gif"


    def getNameFemputadora(self):
        

        return "FEMPUTADORA"

    def rtnArcheveInfo(self, path):
        """
        Read a file via path and return all write in there
        """
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info

    def rtnArchieveFilesNames(self):
        """
        Return all files names of data folder
        """
        try:
            path = self.pathProject + "/Resources/Questions/"

            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ".json" in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None

    def _loadAllQuestions(self):
        path_questions = self.rtnArchieveFilesNames()
        path_file = self.pathProject + "/Resources/Questions/"
        for i in path_questions:
            brute_data = self.rtnArcheveInfo(path_file+i)
            json_data = json.loads(brute_data)
            q = Question(**json_data)
            self.questions.append(q)
            

    def update_chat(self, user, txt):
        if self.chat_historial == "":
            self.chat_historial = user + ":\n" + txt + "\n"
        else:
            self.chat_historial = self.chat_historial + "\n" + user + ":\n" + txt + "\n"

    def insert_user_input(self, user_input):
        if self.valitateInput(user_input):
            self.update_chat("USER", user_input)
            response = self.get_response(user_input)
            self.update_chat(self.getNameFemputadora(), response)
            

    def clearText(self, user_input):
        """
        Erase a stranger characters of string
        and return a vector with all words
        ['str', 'str', ...]
        """
        clear_sms = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        return clear_sms

    def get_response(self, user_input):
        response = self.check_all_messages(self.clearText(user_input))
        return response

    def message_probability(self, clear_user_input, recognized_words, single_response=False, required_word=[]):
        message_certrainty = 0
        has_required_words = True

        for w in clear_user_input:
            if w in recognized_words:
                message_certrainty = message_certrainty + 1

        percentage = message_certrainty / len(recognized_words)


        for w in required_word:
            if w not in clear_user_input:
                has_required_words = False
                break

        if has_required_words or single_response:
            return percentage * 100
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] =  self.message_probability(message, list_of_words, single_response, required_words)

        for i in self.questions:
            response(i.bot_response, i.list_of_words, i.single_response, i.required_words)

        best_match = max(highest_prob, key=highest_prob.get)

        if highest_prob[best_match] < 1:
            return self.unknown()
        else:
            return best_match

    def unknown(self):
        responses = ['Podrias Repetir?', 'No estoy seguro', 'No tengo esa información']
        return responses[random.randint(0, len(responses)-1)]


    def valitateInput(self, user_input):
        return str(user_input).strip() != ""
