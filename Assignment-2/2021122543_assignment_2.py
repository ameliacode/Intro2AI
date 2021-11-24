import os

class Environment:
    def __init__(self):
        self.map = []
        self.QTable = [[0 for _ in range(4)] for _ in range(25)]
        self.actions = ["up","right","left","down"]
        self.states = {"S":0, "G":100, "T":1, "B":-100, "P": 0}
        self.gamma = 0.9
        
    def Q(self, state, action): #state: position index, action: self.actions
        pass

    def import_env(self):
        # current directory
        currentDir = os.path.dirname(os.path.abspath(__file__))
        currentDir.replace("\\","\\\\")
        try:
            with open(currentDir+"\\input.txt","r") as inputFile:
                for line in inputFile:
                    self.map.append([self.states[line[i]] for i in range(5)])

                
        except Exception as error:
            print(error)


def main():

    env = Environment()
    
    env.import_env()
    print(env.map)
    

if __name__=="__main__":
    main()
