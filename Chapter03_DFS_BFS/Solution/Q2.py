# 미로 탈출
# 동빈이 (1,1)에 있고 1로 된 경로로만 탈출할 수 있음(0엔 괴물 존재)
# 탈출에 필요한 최소 거리 구하기
# 시작 칸 마지막 칸 개수 세야 함
# 힌트 : BFS는 가장 가까운 노드부터 탐색하므로 최소 거리 구하기 적합.

# 위치를 이동할 때마다 노드의 가중치(간선 값)를 늘려가는 방식으로 코드 짜기
# bfs는 큐를 활용하기(큐에 넣은 값 바로 빼서 써먹어야 되니까)

from collections import deque

n,m = map(int,input().split()) # 좌표 크기 입력 받기
The_Map = [[int(i) for i in input()] for j in range(m)] # 2차원 리스트로 입력 받기

# 동서남북 확인할 수 있는 로직을 만들면 좋을 듯.
# 구현에서도 자주 쓰는 로직인 것 같던데
# 책에서도 동서남북 확인 로직 쓰는 거 보면 이해하고 기억해두면 좋을 듯.

# 동서남북 확인 로직 [위,아래,오른쪽,왼쪽]
# x,y축은 수학이랑 반대라 생각하면 편한 듯.
dx = [1,-1,0,0] # 열 기준
dy = [0,0,1,-1] # 행 기준

# 너비 우선 탐색 메서드 만들기
# 기능은
def bfs(x,y):
    queue = deque() # 큐를 위한 데큐 라이브러리 사용
    queue.append((x,y)) # 큐 안에 (x,y) 추가 해줌.

    while queue: # 큐가 전부 다 빌 때까지 반복.(큐에서 추출할 값이 없을 때까지 진행)
        x,y = queue.popleft() # 큐에 있던 좌표를 빼서 x,y에 넣기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 이탈 시 무시
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 벽 만나도 무시
            if The_Map[nx][ny] == 0:
                continue
            # 길을 찾을 시
            if The_Map[nx][ny] == 1:
                The_Map[nx][ny] = The_Map[x][y] + 1 # 위치 값(거리)에 1을 더해주기
                queue.append((nx,ny))
    return The_Map[n-1][m-1] # 반복문이 종료되면 최종 위치의 거리를 반환

print(bfs(0,0))