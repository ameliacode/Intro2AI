from BFS import BFS
from CSP import CSP
from HC import HC

import os #os 써서 상대경로 만들어놓을 것

def main():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    currentDir.replace("\\","\\\\")

    with open(currentDir+"\\input.txt","r") as inputFile:
        for line in inputFile:
            N,func = line.split(" ")
            # func = func.replace(" ","")
            if func.startswith("bfs"):
                pass
                # solution = bfs(int(N)) #list or string("no solution")
                # print(solution)
                #file.writelines(solution)
            elif func.startswith("csp"): # Backtracking
                algorithm = CSP(int(N))
                solution = algorithm.csp()

                with open(currentDir+"\\{}_csp_output.txt".format(N),"w") as outputFile:
                    if solution is not None:
                        print(solution[0])
                        for answer in solution[0]: # 다양한 솔루션 중 가장 먼저 나온 결과 출력
                            outputFile.write(str(answer)+" ")
                    else:
                        print("no solution")
                        outputFile.write("no solution")
                pass
            elif func.startswith("hc"):
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
    

if __name__=="__main__":
    main()

