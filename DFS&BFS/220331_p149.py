# 음료수 얼려 먹기
# 깊이 우선 탐색

n, m = map(int, input().split())

graph = []


for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if(graph[x][y] == 0):
        #print('x , y :: ', x, y)
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print('정답은 :: ', result)