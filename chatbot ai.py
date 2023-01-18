import nltk
import spacy
from nltk.chat.util import Chat, reflections
from datetime import datetime

nlp = spacy.load("en_core_web_md")

def extractinfo(stc):
    doc = nlp(stc)
    entitati = [ent.text for ent in doc.entr]
    intentii = [token.text for token in doc if token.poz_ == "verb"]
    return entitati, intentii

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot!", "My name is Chatbot, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you for asking! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"i am fine",
        ["Great to hear that! How can I help you today?"]
    ],
    [
        r"i need (.*)",
        ["Okay, let me see if I can find a solution for you. Can you please provide more details about what you need?"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) ","Goodbye, have a nice day!"]
    ],
    [
        r"what's the time",
        ["The time is {}".format(datetime.now().strftime("%H:%M:%S")), "It is currently {}".format(datetime.now().strftime("%H:%M:%S"))]
    ],
    [
        r"what's the date",
        ["The date is {}".format(datetime.now().strftime("%d/%m/%Y")), "It is currently {}".format(datetime.now().strftime("%d/%m/%Y"))]
    ],
    [
        r"what's your favorite color",
        ["My favorite color is blue", "I like blue the most"]
    ],
    [
        r"where are you from",
        ["I am a virtual chatbot, so I do not have a physical location.", "I am from the digital world"]
    ],
    [
        r"who created you",
        ["I was created by a Catalin.", "My creator is someone who studies artificial intelligence at UVT :)"]
    ],
    [
        r"what's your purpose",
        ["My purpose is to help and assist people providing helpful information", "I am designed to simulate conversation with humans"]
    ],
    [
        r"(.*)",
        ["Didn't quite catch that, can you say something else?", "What are you trying to say?"]
    ],
]

def chat():
    print("hi, how are you?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
