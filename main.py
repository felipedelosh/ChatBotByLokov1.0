import re
import random

def clearText(user_input):
    """
    Erase a stranger characters of string
    and return a vector with all words
    ['str', 'str', ...]
    """
    clear_sms = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    return clear_sms

def get_response(user_input):
    response = check_all_messages(clearText(user_input))
    return response


def message_probability(clear_user_input, recognized_words, single_response=False, required_word=[]):
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

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hola', ['hola', 'hello', 'saludos', 'buenas'], single_response=True)
    response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
    response('Estamos en Risaralda Caldas en la Carrera segunda # 11 - 05', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
    response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)



    best_match = max(highest_prob, key=highest_prob.get)

    if highest_prob[best_match] < 1:
        return unknown()
    else:
        return best_match

def unknown():
    responses = ['Podrias Repetir?', 'No estoy seguro', 'No tengo esa información']
    return responses[random.randint(0, len(responses)-1)]


while True:
    print("BOT: " + get_response(input('You : ')))