import random as rand

class MDP():
    def __init__(self):
        #Python Dictionary
        self.States = {
            "RU8p": 0,
            "TU10p": 0,
            "RU10p": 0,
            "RD10p": 0,
            "RU8a": 0,
            "RD8a": 0,
            "TU10a": 0,
            "RU10a": 0,
            "RD10a": 0,
            "TD10a": 0,
            "DONE": 0
        }
        self.Actions = [
            "P",
            "R",
            "S"
        ]
        
        self.Actions_Two = [
            "P",
            "R"
        ]

    def simulate(self, action, state):
        if state is "RU8p" :
            if (action is "P") :
                return "TU10p"
            elif (action is "R") :
                return "RU10p"
            elif (action is "S") :
                return "RD10p"
                    
        elif (state is "TU10p") :
            if (action is "P") :
                return "RU10a"
            elif (action is "R") :
                return "RU8a"
                    
        elif (state is "RU10p") :
            if (action is "R") :
                return "RU8a"
            elif (action is "P") :
                if (rand.choice([True, False])) :
                    return "RU8a"
                else :
                    return "RU10a"
                
            elif (action is "S") :
                return "RD8a"
                    
        elif (state is "RD10p") :
            if (action is "R") :
                return "RD8a"
            elif (action is "P") :
                if (rand.choice([True, False])) : #coin flip 
                    return "RD8a"
                else :
                    return "RD10a"
                
        elif (state is "RU8a") :
            if (action is "P") :
                return "TU10a"
            elif (action is "R") :
                return "RU10a"
            elif (action is "S") :
                return "RD10a"
                    
        elif (state is "RD8a") :
            if (action is "R") :
                return "RD10a"
            elif (action is "P") :
                return "TD10a"
                    
        return "DONE"

    def get_num_decisions(self, state):
        two_actions = {"TU10p","RD8a","RD10p"}
        if state in two_actions:
            return 2
        else:
            return 3
    
    def get_action(self,state):
        two_actions = {"TU10p","RD8a","RD10p"}
        
        if (state in two_actions):
            return self.Actions_Two
        else:
            return self.Actions
    
    def generate_reward(self, state, action):
                
        if (state is "TU10a"): 
            return -1
        elif (state is "RU10a"): 
            return 0
        elif (state is "RD10a"): 
            return 4
        elif (state is "TD10a"):
            return 3   
        
        if (action is "P"):
            return 2
        elif (action is "R"): 
            return 0
        else: #for action s 
            return -1
        
    def get_States(self):
        return self.States