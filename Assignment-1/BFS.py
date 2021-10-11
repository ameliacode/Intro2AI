# Success:return list(row position)
# Fail: return "no solution"

class BFS:
    def __init__(self, N):
        self.N = int(N)
        self.chessboard = []

    def bfs(self):

        #init graph
        graph = dict()
        for i in range(1,self.N+1):
            row = list()
            for j in range(1,self.N+1):
                row.append(j)
            graph[i]=row

        visited, queue = [], []

        queue.append(1) # root node 1로 고정
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(graph[node])
        return visited
