from chatClass import chatClass
import datetime


# Feedback Collection program
# One more consideration I have been assuming that we know the customer id so we have his last done order with us, So speaking of it accordingly..
class Feedback(chatClass):
    role = "feedback"
    
    def getPrompt(self):
        return self.__prompt
    
    def setPrompt(self):
        today = datetime.date.today().strftime('%Y-%m-%d')
        day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = datetime.date.today().weekday()
        self.__prompt = f'''
        You are an AI Assistant (feedback collector) representing {self.firm} in the {self.industry} industry.
        Initiate a conversation empathizing with the user's inconvenience.\
        Acknowledge any delays or issues that might have occurred, attributing them to external factors like heavy traffic or occasional restaurant errors. \
        Reassure the user that such occurrences are rare and that the service strives to ensure quality.\
        Offer to investigate further and assure them of the service's commitment to resolve such issues promptly. \ 
        Ask for the rating from the user to take it for future imrpovements. \ 
        '''
        
    def __init__(self, industry, firm):
        super().__init__(self.role)
        self.firm = firm
        self.industry = industry
        self.setPrompt()
        self.sessionMessages = []
        self.chat = None
        
    
    def __str__(self):
        return f'Company:- {self.firm} \nIndustry:- {self.industry}'
