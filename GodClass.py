
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
)


#This class have the instantiation of ChatGPT/ Our AI Agent at work.. 
class GodClass:
    def __init__(self, GPT_KEY):
        self.chat = ChatOpenAI(openai_api_key=GPT_KEY,temperature=0)
        
    def load_answer(self, question, feedbackObject):
        feedbackObject.sessionMessages.append(HumanMessage(content=question))

        assistant_answer  = self.chat(feedbackObject.sessionMessages)

        feedbackObject.sessionMessages.append(AIMessage(content=assistant_answer.content))

        return assistant_answer.content


