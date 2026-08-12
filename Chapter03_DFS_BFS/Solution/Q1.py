# 음료수 얼려 먹기
# N x M 크기의 얼음 틀이 있음 (세로x가로)
# 구멍이 뚫려 있으면 0, 칸막이 존재는 1
# 한 번에 생성할 수 있는 아이스크림 개수 출력
# 아이스크림 생성 기준 책에 제대로 안 써있네 시부레
# 아이스크림 생성 기준은 0 한 뭉탱이임.

# 00110
# 00011
# 11111
# 00000
# 3


N,M = map(int,input().split()) # 행렬 크기 입력 받기
ice_frame = [[int(i) for i in input()] for j in range(N)] # 이중리스트로 입력 받기

cnt = 0 # 결과값

def dfs(n,m):
    if n <= -1 or n >= N or m >= M or m <= -1: # 범위 이탈 시 False 반환
        return False
    if ice_frame[n][m] == 0: # 구멍 칸에 있을 시
        ice_frame[n][m] = 1 # 왔다갔다고 기록해주고
        dfs(n-1,m) #상
        dfs(n,m-1) #좌
        dfs(n+1,m) #하
        dfs(n,m+1) #우
        # 상하좌우 0,1 여부 확인하면서 탐색
        # 상하좌우 자동 탐색을 위해선 재귀호출이 가장 좋음
        # 상하좌우 각각 재귀 함수를 만들고 구멍 칸 찾으면 dfs(n,m)에 True 반환
        return True
    return False # 주변에 구멍 칸 아예없으면 False반환

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt += 1 # 연결된 0 덩어리 하나를 전부 탐색했다면 아이스크림 개수를 하나씩 늘림.

print(cnt)

# 탐색이 필요한 문제는 DFS, BFS 중 하나를 선택하고
# DFS가 필요하다 판단되면 재귀함수를 어떻게 사용할 지 생각해야 함.
# 위 문제는 상하좌우를 탐색하면서 연결지어진 0 덩어리의 개수를 찾는 것이기 때문에
# 한 칸씩 상하좌우의 좌표값을 확인해야함.
# 확인은 재귀를 통해 자동으로 탐색함.