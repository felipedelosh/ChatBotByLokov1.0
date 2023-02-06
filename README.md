# ChatBotByLokov1.0
Simple python chatbot... user.input &lt;=> bot.response

![](/Docs/evidence.png)

1 -> The user generates a input and the bot response in limitated set of responses.

# General funtion:

Exists a folder: Resources\Questions

You find there a archives.json with the nest extructure:

{
    "bot_response" : "This is the str to the BOT response",
    "list_of_words" : [
        "str",
        "str",
        ...
    ],
    "single_response" : Bool,
    "required_words" : ["STR"?]
}

## about "bot_response"

This is a static text with the Bot always respond.

## about "list_of_words"

This is a vector to input words to calculate a sentence propability

for example:

if the user ask for a product, the user use a some words like a:

how, much, name of product, buy, price, cost, ... words to references:

- How much does the rice cost?
- price rice?
- i want to buy


## about "Single response"

This is a boolean to indicate if the user greeting or need specifid action.

## abot "required_words"


This is a vector to input obligatory string... for example

if the user need buy rice the sentence contain a word "rice".

# Solution of model:


Calculate a propabilite of sentence and the bisgest concidency return a string (def message_probability) all message_probability calculate into a vector in for loop (def check_all_messages) 

