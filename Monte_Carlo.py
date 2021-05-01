import MDP as Diagram
import random as rand


class Monte_Carlo():
    def __init__(self):
        
        self.MDP = Diagram.MDP()
        # Learning Rate
        self.alpha = .1
        
    def execute(self):
        starting_state = "RU8p"
        reward = 0

        saved_states = ["RU8p"]
        saved_actions = []
        saved_rewards = []
        
        while(True):
            if(starting_state is "DONE"):
                break
            
            action_todo = self.action_decision(starting_state)
            
            saved_actions.append(action_todo)
            
            reward_val = self.MDP.generate_reward(starting_state,action_todo)
            
            reward = reward + reward_val
            
            saved_rewards.append(reward_val)
            
            self.update_rule(action_todo, reward_val, starting_state)
            
            new_state = self.MDP.simulate(action_todo, starting_state)
            
            saved_states.append(new_state)
            
            starting_state = new_state
        
        print(saved_states)
        print(saved_actions)
        print(saved_rewards)
        print(reward)
        print(reward/len(saved_rewards))
        print("#############")    
            
    
    # V(s)<-V(s)+alpha[R-V(s)]g
    def update_rule(self, action, reward, state):
        updated_value = self.MDP.States.get(state) + self.alpha *(reward - self.MDP.States.get(state))
        self.MDP.States.update({state: updated_value})
    
    def action_decision(self, state):
        num_decisions = self.MDP.get_num_decisions(state)
        rand_decision =  rand.randint(0, num_decisions-1)
        
        if num_decisions == 3:
            if rand_decision == 0:
                return "S"
            elif rand_decision == 1:
                return "R"
            else:
                return "P"
        
        if num_decisions == 2:
            if rand_decision == 0:
                return "P"
            else:
                return "R"
            
        
        