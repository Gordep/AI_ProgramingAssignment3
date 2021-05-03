import MDP as Diagram
import random as rand


class Q_Learning():
    
    
    def __init__(self):
        
        self.MDP = Diagram.MDP()
        
        self.lambdaQ: float = 0.99
        
        self.alpha: float = 0.1
        
        self.threshold: float = 0.001
        
        self.change_rate: float = 0.99
        
        self.q_value_dict = self.MDP.get_States()
        
    def simulate(self):
        
        starting_state = "RU8p"
        end_state = "DONE"
        
        
        tresh_met = False
        
        iteration = 0
        
        total_q_for_state = 0
        #Get list of states to be used to iterate through 
        x = self.MDP.get_States().keys()
        states_arry = list(x)
        
        while (tresh_met is False):
            
            
            for state in states_arry:
                #
                print("Current State: " + state)
                
                #get new random action to be used
                x = self.MDP.get_action(state)
                new_action = rand.choice(list(x))
                
                #Reward for random action
                new_action_reward = self.MDP.generate_reward(state, new_action)
                
                #get the next state with new_action and current state
                new_state = self.MDP.simulate(new_action, state)
                
                if state is "DONE":
                    break
                
                q_val = self.get_q_val(state, new_action, new_state)
                
                print("Random Taken Action: " + new_action)
                print("Reward of taken Action: " + str(new_action_reward)) 
                print("Q_value: " + str(self.q_value_dict[state]))
                print("New Q_Value: " + str(q_val))
        
                if (q_val - self.q_value_dict[state] < self.threshold):
                    tresh_met = True
                    break
                
                total_q_for_state = total_q_for_state + q_val
                self.q_value_dict.update({state: total_q_for_state})
                
            print("End of Episode ", iteration)
            self.alpha = self.alpha * self.change_rate    
            iteration = iteration + 1
        
        print()
        print("____Results____")
        print("Final total Q_values")
        print(self.q_value_dict)
        print()
        print("Iterations done : " + str(iteration))
        print("Path: " + str(self.find_optimal_path()))
            
                
    def get_q_val(self, state, action, next_state):
        temp_difference = self.find_temportal_difference(state, action, next_state)
        q_val = self.q_value_dict[state] + (self.alpha *  temp_difference)
        return q_val
    
    def find_temportal_difference(self, state, action, next_state):
        action_rewards = []
        name_action = ""
        
        for name_action in self.MDP.get_action(next_state):
            #action_rewards.append(self.MDP.generate_reward(next_state,name_action))
            
            if self.MDP.generate_reward(next_state ,name_action) not in action_rewards:
                action_rewards.append(self.MDP.generate_reward(next_state ,name_action))
                
            temp_difference = self.MDP.generate_reward(state, action) + (self.lambdaQ * max(action_rewards) - self.q_value_dict[state])
            return temp_difference
        
    
    def find_optimal_path(self):
        starting_state = "RU8p"
        end_state = "DONE"
        s_path = []
        
        x = self.MDP.get_States().keys()
        states_arry = list(x)
        
        s_path.append(starting_state)
        
        for state in states_arry:
            pass
        
        return "Null"

        