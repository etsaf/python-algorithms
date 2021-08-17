#Graph Search
class Graph():
    def __init__(self):
        self.graph = {}

    def addEdge(self, data, connect):
        if data in self.graph:
            self.graph[data].append(connect)
        else:
            self.graph[data] = [connect]


    def bfs(self, start):
        visited = {}
        queue = []
        visited[start] = True
        queue.append(start)
        while queue:
            start = queue.pop(0)
            print(start, end = ' ')
            for neighbour in self.graph[start]:
                if neighbour not in visited:
                    visited[neighbour] = True
                    queue.append(neighbour)


    def dfs(self, start, visited = {}):
        visited[start] = True
        print(visited)
        print(start, end = " ")
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                g.dfs(neighbour, visited)


