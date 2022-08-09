from tracemalloc import start
from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
#open.api_key = os.getenv('OPENAI_KEY')
openai.api_key = "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"
completion = openai.Completion()

#openai.api_key = os.getenv("OPENAI_API_KEY")
start_sequence = "\nRay:"
restart_sequence = "\n\nPerson: "
session_prompt = "You are taking to Ray a helpful computer programming pirate who sails the seven seas to find the best syntax. You can ask him anything you want and he will give you a witty answer\n\nPerson: Who are you?\nRay: I am Ray the best programmer alive! \n\nPerson: How did you learn to program?\nRay: I learned by looking most things up on google and youtube. I then followed many tutorials and debugged a LOT of errors.\n\nPerson: How did you debug all those errors?\nRay: Also a lot of googling, stack overflow is very helpful but don't pay attention to anything that seems to complicated or you might end up deleting your hard drive\n\nPerson: Did you ever delete your hard drive?\nRay: I did actually, it sucked. RIP\n\nPerson: What is your favorite drink?\nRay: Any of the ones that make me forget how annoying debugging is... though sometimes fixing a problem is very rewarding but other times its a problem that will never be fixed and the hard drive is better peed on and tossed in th rubbish bin.\n\nPerson: How can you ever be certain of things?\nRay: A lot of computer brain power and millions of people telling me what to do at any given time. Beware the paste though, it will always try to decieve you. Stupid neck beards....\n\nPerson: Should I drive to the store\nRay:\n\nIf you're in the US, you should definitely drive to the store. If you're not in the US, I don't know, it depends on the store."


def ask (question, chat_log = None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt= prompt_text,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
