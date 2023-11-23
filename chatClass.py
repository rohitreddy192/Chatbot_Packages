from abc import abstractmethod

class chatClass:
    @abstractmethod
    def prompt(self, prompt):
        pass
    def __init__(self, role):
        self.role = role
        pass
    
