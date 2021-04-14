import sys
def dfs(graph, v):
    visited = []
    stack=[v]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i in range(len(graph[node])-1, -1, -1):
                if graph[node][i] == 1:
                    stack.append(i)
    return visited

def bfs(graph, v):
    visited = []
    queue = [v]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for i in range(len(graph[node])):
                if graph[node][i]==1:
                    queue.append(i)
    return visited

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y= map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

print(' '.join(map(str,dfs(graph, V))))
print(' '.join(map(str,bfs(graph, V))))