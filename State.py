import random as rand

class MDP():
    def __init__(self):
        #Python Dictionary
        States = {
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
        Actions = [
            ["P"],
            ["R"],
            ["S"]
        ]

    def simulate(self, action, state):
        if (s == "RU8p") :
            if (a == "P") :
                return "TU10p"
            elif (a == "R") :
                return "RU10p"
            elif (a == "S") :
                return "RD10p"
                    
        if (s == "TU10p") :
            if (a == "P") :
                return "RU10a"
            elif (a == "R") :
                return "RU8a"
                    
        if (s == "RU10p") :
            if (a == "R") :
                return "RU8a"
            elif (a == "P") :
                if (rand.choice([True, False])) :
                    return "RU8a"
                else :
                    return "RU10a"
                
            elif (a == "S") :
                return "RD8a"
                    
        if (s == "RD10p") :
            if (a == "R") :
                return "RD8a"
            elif (a == "P") :
                if (rand.choice([True, False])) : #coin flip 
                    return "RD8a"
                else :
                    return "RD10a"
                
        if (s == "RU8a") :
            if (a == "P") :
                return "TU10a"
            elif (a == "R") :
                return "RU10a"
            elif (a == "S") :
                return "RD10a"
                    
        if (s == "RD8a") :
            if (a == "R") :
                return "RD10a"
            elif (a == "P") :
                return "TD10a"
                    
        return "DONE"

    def get_num_decisions(state):
        two_actions = {"TU10p","RD8a","RD10p"}
        if state in two_actions:
            return 2
        else:
            return 3
    
    def generate_reward(state, action):
        
        if (action == "P"):
            return 2
        elif (action == "R"): 
            return 0
        else: #for action s 
            return -1
        
        
        
        if (state == "TU10a"): 
            return -1
        elif (state == "RU10a"): 
            return 0
        elif (state == "RD10a"): 
            return 4
        elif (state == "TD10a"):
            return 3
        
        