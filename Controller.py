"""
FelipedelosH

This is a Chatbot load controller

"""

import os # To know path project}
import re
import random

class Controller:
    def __init__(self) -> None:
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        self.chat_historial = ""


    def getIMGRouteOfFempuradora(self):
        

        return self.pathProject + "\\Resources\\img\\femputadora.gif"


    def getNameFemputadora(self):
        

        return "FEMPUTADORA"

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

        response('Hola', ['hola', 'hello', 'saludos', 'buenas'], single_response=True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos en Risaralda Caldas en la Carrera segunda # 11 - 05', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)



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
    