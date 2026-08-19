n = 5
computers = [[1,1,0,1,0],[1,1,0,0,0],[0,0,1,0,0],[1,0,0,1,1],[0,0,0,1,1]]
# 0번부터 4번 노드까지 5개의 노드가 있다고 치자.


visited = [False] * n # 방명록임.
total = 0
def dfs(start):
    global total
    visited[start] = True # 다녀간 해당 노드는 True로 바꿔줌.

    for i in range(n):
        if not visited[i] and computers[start][i] == 1: # 안 다녀간 노드 중에 연결된 노드로 가기.
            total += 1 # 연결된 노드의 수
            dfs(i) # 연결된 노드로 탐색하러 감.
    return n-total # 전체 컴퓨터 중 연결된 노드의 수를 빼면 총 네트워크 수를 구할 수 있음.


print(dfs(0))


