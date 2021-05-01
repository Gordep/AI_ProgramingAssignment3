import Monte_Carlo

class main():
    def __init__(self):
        # run monte carlo
        mc = Monte_Carlo.Monte_Carlo()
        for x in range(50):
            print("Episode ",x)
            mc.execute()
        
        print("Val for all states is" )
        print(mc.MDP.get_States())
            
            
if __name__ == '__main__':
    main()

