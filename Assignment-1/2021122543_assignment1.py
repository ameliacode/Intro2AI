from BFS import bfs 
from CSP import CSP
from HC import hc

def main():
    with open("D:\\GitHub\\Intro2AI\\Assignment-1\\input.txt","r") as inputFile:
        for line in inputFile:
            N,func = line.split(" ")
            if func.startswith("bfs"):
                pass
                # solution = bfs(int(N)) #list or string("no solution")
                # print(solution)
                #file.writelines(solution)
            elif func.startswith("csp"):
                algorithm = CSP(int(N))
                solution = algorithm.csp()

                with open("D:\\GitHub\\Intro2AI\\Assignment-1\\{}_csp_output.txt".format(N),"w") as outputFile:
                    if solution is not None:
                        for answer in solution[0]:
                            outputFile.write(str(answer)+" ")
                    else:
                        outputFile.write("no solution")
                pass
            elif func.startswith("hc"):
                #solution = hc(N)
                #file.writelines(solution)
                pass
            else:
                pass
    

if __name__=="__main__":
    main()

