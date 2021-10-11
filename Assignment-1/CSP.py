
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

    def dfs(self,xi):
        if xi == self.N :
            solution = []
            solution.extend(self.chessboard)
            self.solutions.append([i+1 for i in solution])
            return
        for row_pos in range(self.N):
            self.chessboard[xi]=row_pos # 일단 해당 위치에 queen을 배치한다.
            if self.isLegal(xi): # promising한 자리일 경우,
                self.dfs(xi+1) # 다음 column으로 넘어가
                # print("Backtracking {}".format(row_pos)) # promising 하지 않는다면 재귀함수에 따라 backtracking

    def csp(self):
        self.dfs(0)
        if self.solutions:
            return self.solutions
        else:
            pass # return null






