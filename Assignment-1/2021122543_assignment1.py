from BFS import BFS
from CSP import CSP
from HC import HC

import os

def main():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    currentDir.replace("\\","\\\\")

    try:
        with open(currentDir+"\\input.txt","r") as inputFile:
            for line in inputFile:
                N, func = line.split(" ")
                
                if func.startswith("bfs"): # Breadth First Searching
                    algorithm = BFS(int(N))
                    solution = algorithm.bfs()

                    with open(currentDir+"\\{}_bfs_output.txt".format(N),"w") as outputFile:
                        if solution is not None:
                            print(solution)
                            for answer in solution:
                                outputFile.write(str(answer)+" ")
                        else:
                            print("no solution")
                            outputFile.write("no solution")

                elif func.startswith("csp"): # CSP using Backtracking (DFS)
                    algorithm = CSP(int(N))
                    solution = algorithm.csp()

                    with open(currentDir+"\\{}_csp_output.txt".format(N),"w") as outputFile:
                        if solution is not None:
                            print(solution[0])
                            for answer in solution[0]: # 다양한 솔루션 중 가장 먼저 나온 결과 출력 -> 하나의 솔루션으로 수정됨
                                outputFile.write(str(answer)+" ")
                        else:
                            print("no solution")
                            outputFile.write("no solution")
                    pass

                elif func.startswith("hc"): # Hill Climbing
                    algorithm = HC(int(N))
                    solution = algorithm.hc(int(N))

                    with open(currentDir+"\\{}_hc_output.txt".format(N),"w") as outputFile:
                        if solution is not None:
                            print(solution)
                            for answer in solution:
                                outputFile.write(str(answer)+" ")
                        else:
                            print("no solution")
                            outputFile.write("no solution")
                else:
                    pass
    except: # error
        print("No input.txt file in current directory")


if __name__=="__main__":
    main()

