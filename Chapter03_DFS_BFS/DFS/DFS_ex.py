# DFS 메서드 정의(깊이 우선 탐색)

# 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함.
# 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 위 과정을 더 이상 수행할 수 없을 때까지 반복.

def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문(스택으로 이용하므로 재귀 호출 활용)
    for i in graph[v]:
        if not visited[i]: # == True 생략된거임.
            dfs(graph, i, visited)

    # for i in graph[1] == [2,3,8]
    # i는 2,3,8 중 하나
    # i가 2일 때, if not visited[2] => if not [1,7] -> dfs(graph,2,visited) -> visited[2] = True -> print(2, end=' ')
    # for i in graph[2] => for i in [1,7] -> if not visited[1] 은 조건문에 해당이 안되므로 if not visited[7]로 넘어감.
    # dfs(graph,7,visited) -> 반복.
    # 즉, 방문 처리를 리스트로 저장하고(인덱스에 True로 저장) 방문 처리된 노드를 재귀를 통해 출력함.
    # 방문 처리된 노드를 제외하고, 방문을 하지 않은 노드를 찾게끔 조건문을 통해 필터링.

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [], # 0은 없으므로 공란
    [2,3,8], # 1에 연결된 노드
    [1,7], # 2에 연결된 노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 데이터 개수가 n개일 때 시간 복잡도는 O(N)