import Monte_Carlo
import Value_Iteration
import Q_Learning

class main():
    def __init__(self):
        
        print("Choose algorithm")
        print("1. Monete Carlo")
        print("2. Value Iteration")
        print("3. Q-Learning")
        inputVal = input("> ")
        
        if inputVal == "1":
        
            # run monte carlo
            mc = Monte_Carlo.Monte_Carlo()
            for x in range(50):
                print("Episode ",x)
                mc.execute()
            
            print("Val for all states is" )
            print(mc.MDP.get_States())
            
        elif inputVal == "2":     
            val_iter = Value_Iteration.Value_Iteration()
            
            val_iter.simulate()

        elif inputVal == "3":
            q_l = Q_Learning.Q_Learning()
            q_l.simulate()
        
        else:
            print("invalid input")
            
if __name__ == '__main__':
    main()

