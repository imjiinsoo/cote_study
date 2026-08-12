# 미로 탈출 문제
# 최단 경로는 bfs로. 범위가 점차 n=1,2,3.. 이렇게 넓어지는 구조니까 최단으로 값이 나옴

# 첫 셋팅
from collections import deque
n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 구현
def bfs(row, col):
    # 첫 위치 큐에 넣기
    queue = deque()
    queue.append((row,col))

    while queue:
        # 큐에 값 있으면 꺼내서 상하좌우 이동 가능하면 그 지점까지 도달하는 최단 거리 +1 시키기
        row, col = queue.popleft()
        for i in range(4):
            nx = row+dx[i]
            ny = col+dy[i]
            # 그래프 범위 벗어나면 pass
            if nx >= n or nx < 0 or ny < 0 or ny >= m:
                continue
            # 괴물 있는 곳은 못 가니까 pass
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 곳이고 안 가본 곳(값이 1)이면 이전까지 왔던 최단거리 +1 하고 큐에 넣기(다음 bfs에서 돌아야됨)
            # (내 코드 기준) row,col = 현 위치 / nx,ny 상하좌우 bfs 이동하는 위치
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[row][col] + 1
                queue.append((nx,ny))
    # 다 끝나면 마지막 위치의 값 꺼내기 = 그게 최단 이동 거리
    return graph[n-1][m-1]

print(bfs(0,0))