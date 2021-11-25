import random
import copy

class HC:
    def __init__(self, N):
        self.N = int(N)
        self.chessboard = [random.randint(0, self.N-1) for _ in range(self.N)] # complete-State formulation
        self.heuristicBoard = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.hCost = float("inf")

    def heuristic(self, chessboard): #heuristic function >> 좀더 좋은 방향으로 생각해볼 것 시간 비용.
        currentHCost = 0
        for xi in range(self.N-1):
            for xi_idx in range(xi+1, self.N):  # column
                if chessboard[xi_idx] == chessboard[xi]:  # 직선일 경우
                    currentHCost += 1
                if abs(chessboard[xi] - chessboard[xi_idx]) == abs(xi - xi_idx):  # 대각선일 경우
                    currentHCost += 1
        return currentHCost

    def getHeuristicBoard(self):
        chessboard = copy.copy(self.chessboard) # temporary chessboard
        for xi in range(self.N):
            originalPos = chessboard[xi]
            for yi in range(self.N):
                chessboard[xi]=yi
                self.heuristicBoard[yi][xi] = self.heuristic(chessboard)
            chessboard[xi] = originalPos

    def hc(self, N):
        steps = 0
        attempts = 0

        while self.hCost > 0:
            if attempts > 100:
                break
            if steps > N :
                self.__init__(N)  # generate initial state randomly ( # 무작위 재시작 언덕 오르기)
                steps = 0
                attempts += 1

            self.getHeuristicBoard()

            globalMinXi = -1
            globalMinYi = -1
            globalMin = float('inf')

            for xi in range(0, self.N):
                columnHeuristic = []
                for yi in range(0, self.N):
                    columnHeuristic.append(self.heuristicBoard[yi][xi])
                columnMin = min(columnHeuristic)
                columnMinYi = columnHeuristic.index(min(columnHeuristic))
                columnMinXi = xi

                if columnMin < globalMin:
                    globalMin = columnMin
                    globalMinXi = columnMinXi
                    globalMinYi = columnMinYi

            self.chessboard[globalMinXi] = globalMinYi
            self.hCost = self.heuristic(self.chessboard)
            steps += 1

        if self.hCost == 0:
            solution = [i+1 for i in self.chessboard]
            return solution
        else:
            pass #return null
