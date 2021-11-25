
class CSP: #Backtracking
    def __init__(self, N):
        self.N = int(N)
        self.solutions=[]
        self.chessboard = [0 for _ in range(N)] #index = xi as column, value = row

    def isLegal(self, xi): # 탐색하고자하는 현 상태
        for xi_idx in range(xi): # column
            if self.chessboard[xi_idx]==self.chessboard[xi]: # 직선일 경우
                return False
            if abs(self.chessboard[xi]- self.chessboard[xi_idx]) == abs(xi - xi_idx): # 대각선일 경우
                return False
        return True

    def dfs(self, xi):
        if xi == self.N:
            solution = []
            solution.extend(self.chessboard)
            self.solutions.append([i + 1 for i in solution])
            return True
        for row_pos in range(self.N):
            self.chessboard[xi]=row_pos
            if self.isLegal(xi):
                if self.dfs(xi+1):
                    return True

    def csp(self):
        self.dfs(1)
        # print(self.chessboard)
        if self.solutions:
            return self.solutions
        else:
            pass # return null






