import re

def clearText(user_input):
    """
    Erase a stranger characters of string
    and return a vector with all words
    """
    clear_sms = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    return clear_sms

print(clearText("Loco ooo o?"))
