from dotenv import load_dotenv
import os
from fetch_db_record import DBConnection
from feedback import Feedback
from GodClass import GodClass
load_dotenv()

GPT_KEY = os.getenv('GPT_KEY1')
from langchain.schema import SystemMessage, AIMessage

#This chat solves an entire conversation for feedback collection...
def feedbackCollectionChat(orderId):
    gc = GodClass(GPT_KEY)
    fb = Feedback('Food Delivery Services','Zomato')
    fb.sessionMessages.append(SystemMessage(content = fb.getPrompt()))
    fb.sessionMessages.append(SystemMessage(content=f'Customers order is :- {DBConnection().getrecord(orderId)}'))
    while True:
        inp = input('> ')
        reply = gc.load_answer(inp, fb)
        print(reply)
        if "bye" in inp.lower():
            break
        

if __name__ == "__main__":
    feedbackCollectionChat(1)