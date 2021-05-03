import MDP as Diagram
import random

class Value_Iteration:

    def __init__(self):
        self.MDP = Diagram.MDP()
        self.alpha : float = 0.1
        self.vlambda = .99
        
    #Value_iteration main alogrithim    
    def simulate(self):
        
        #list of values 
        value_estimate = self.MDP.get_States()
        
        iterations = 0
        
        #Get list of states to be used to iterate through 
        x = self.MDP.get_States().keys()
        states_arry = list(x)
        
        
        while True:
            
            # used to store new states and there values
            new_value_estimate = {}
            
            #iterate through each state
            for state in states_arry:
                
                #When last state is reached
                if state is "DONE":
                    new_value_estimate[state] = 0.0
                
                else:
                    
                    maxQval = float('-inf')
                    actionName = ""
                    print("Value of prev state : " ,state , ":" ,value_estimate[state])
                    
                    for action in self.MDP.get_action(state):
                        
                        q_val = 0
                        
                        #.5 decision 
                        # first two if statements for diverging paths 
                        if state is "RD10p" and action is "P" :
                            dfirst = .5 * (self.MDP.generate_reward(state, action) + self.vlambda * self.MDP.States.get("RD8a"))
                            dsecond = .5 * (self.MDP.generate_reward(state, action) + self.vlambda * self.MDP.States.get("RD10a"))
                            q_val = dfirst + dsecond
                            
                        elif state is "RU10p" and action is "P" :
                            dfirst = .5 * (self.MDP.generate_reward(state, action) + self.vlambda * self.MDP.States.get("RU8a"))
                            dsecond = .5 * (self.MDP.generate_reward(state, action) + self.vlambda * self.MDP.States.get("RU10a"))
                            q_val = dfirst + dsecond
                        
                        else:
                            transition_probability = 1
                            reward = self.MDP.generate_reward(state, action)
                            new_state = self.MDP.simulate(action, state)
                            q_val = transition_probability * (reward + self.vlambda * value_estimate[new_state])
                                                              
                        print("Current estimate of each action ", action,": ", q_val)
                        
                        if maxQval < q_val:
                            maxQval = q_val
                            actionName = action
            
                    new_value_estimate[state] = maxQval
                    print("Current Action: ", actionName)
                    print("Current Value of state : " , state , ":"  , new_value_estimate[state])
                    print("#############")
            iterations = iterations + 1
            
            if max(abs(value_estimate[stateX]-new_value_estimate[stateX]) for stateX in states_arry ) < .001:
                # find convergence
                print("Iterations done: " , iterations)
                print("Convergence done")
                
                break
            
            value_estimate = new_value_estimate
        
        
        print("Val for all states is: ", new_value_estimate)
                            
        