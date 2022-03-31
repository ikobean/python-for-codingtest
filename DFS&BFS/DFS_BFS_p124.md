# 탐색
많은 데이터 중에서 원하는 데이터를 찾는 과정

overflow : 특정 자료구조가 수용할 수 있는 데이터 크기를 over해서 삽입을 시도할 경우
underflow : 자료구조에 데이터가 없는데 삭제를 시도할 경우

# Stack
박스 쌓기.
FILO

```python
stack = []
stack.apppend(5)
stack.apppend(4)
stack.apppend(3)
stack.pop()

print(stack) 

// [5,4] 출력

# Queue
대기줄
FIFO

from collections import deque
queue = deque()
queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft()

print(queue)
// [4,3] 출력

queue.reverse()
print(queue)

// [3,4] 출력

deque => list
list(queue)
```

스택 자료구조를 활용해야 하는 상당수 알고리즘은
재귀 함수를 이용해서 간편하게 구현 가능

```python


# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: return 1
    # n*n-1을 그대로 코드로 작성
    return n * factorial_recursive(n - 1)


```

# DFS
Depth-First Search, 깊이 우선 탐색  
인접 행렬 
- 2차원 배열에 각 노드가 연결된 형태를 기록
- 리스트를 이용해 구현. (다른 언어에서는 array)

인접 리스트  
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
- 리스트를 이용해 구현. (다른 언어에서는 연결 리스트)



```python
# 인접 행렬
INF = 99999999
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
```

```python
# 인접 리스트
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _in range(3)]

# 노드 0에 연결한 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장
graph[2].append((0,5))
```

특정 노드와 연겨된 모든 인접 노드를 순회해야 하는 경우   
: 인접 리스트

DFS는 스택
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스태의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


```python
# DFS 템플릿

def dfs(graph v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```


# BFS
Breadth First Search, 너비 우선 탐색
가까운 노드부터 탐색
queue 사용

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2를 더 할 수 없을 때 까지 반복

```python
# BFS 템플릿
from collections import deque

# BFS 함수 정의


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print('브이', v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            print('visited[i]:: ', i, visited[i])
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

```


