import os
import random

class Environment:
    def __init__(self):
        self.map = []
        self.QTable = [[0 for _ in range(4)] for _ in range(25)]
        self.actions = {"up":0,"right":1,"left":2,"down":3}
        self.states = {"S":0, "G":100, "T":1, "B":-100, "P": 0}
        self.gamma = 0.9
        self.start = 0 #index
        self.goal = 0
        self.current_state = 0

    def move_agent(self, action, current_pos):
        if action == "up":
            current_pos = current_pos-5
            if current_pos < 0:
                return False
        elif action == "right":
            if (current_pos-4)%5 == 0:
                return False
            else:
                current_pos = current_pos + 1
        elif action == "left":
            if current_pos % 5 == 0:
                return False
            else:
                current_pos = current_pos-1
        elif action == "down":
            if current_pos // 10 == 2:
                return False
            else:
                current_pos = current_pos + 5
        else:
            pass
        return current_pos

    def Q(self, state, action):  # state: position index, action: self.actions
        next_move = self.move_agent(action=action, current_pos=state)
        _action = self.actions[action]
        self.current_state = next_move
        if not next_move:
            pass
        else:
            self.QTable[state][_action] = self.map[state] + self.gamma * max(self.QTable[next_move])

    def import_env(self):
        # current directory
        currentDir = os.path.dirname(os.path.abspath(__file__))
        currentDir.replace("\\","\\\\")
        try:
            with open(currentDir+"\\input.txt","r") as inputFile:
                num_line = 0
                for line in inputFile:
                    for i in range(5):
                        self.map.append(self.states[line[i]])
                        if line[i]=="S":
                            self.start = num_line*5+i
                        if line[i]=="G":
                            self.goal = num_line*5+i
        except Exception as error:
            print(error)


def main():

    env = Environment()
    env.import_env()
    print(env.map)

    for step in range(1):
        pos = env.start
        while True:
            _action = random.choice(list(env.actions.keys()))
            env.Q(state=pos, action=_action)
            pos = env.current_state
            if pos == env.goal:
                break
    for i in range(25):
        print(env.QTable[i])
    

if __name__=="__main__":
    main()
