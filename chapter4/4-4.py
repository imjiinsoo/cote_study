# 게임 개발

# 맵 크기
n,m = map(int,input().split())

# 위치/바라보는 방향(dir) 입력
x,y,dir = map(int,input().split())

# 실제 맵 입력 (0 = ㄱㄴ / 1 = ㅂㄱㄴ)
gameMap = []
for i in range(n):
    gameMap.append(list(map(int,input().split())))

# 방명록 (방문했으면 1로 바꾸기)
visited = [[0]*m for i in range(n)]

# 방향 리스트 생성. 북동남서 = 0123로 인덱스 맞춰서. ex. 북 = 인덱스 1번 = (-1,0) = 위로 한칸 이동
# 근데 게임 로직에서 왼쪽으로 도는거라 인덱스가 1 증가가 아니라 1감소하게끔 반복문 실행해야됨 유념
directions = [(-1,0), (0,1), (1,0), (0,-1)]

# 게임 시작
cnt = 1 # 처음에 visited 0인곳에 떨궈지니까 일단 하나 방문했으니 cnt 1증가
visited[x][y] = 1 # 처음 떨궈진 곳 visited = 1로 바꾸기

# 한 자리에서 4바퀴 돌면 빠꾸해야되니까 turnCnt 생성
turnCnt = 0

# 갈 곳 없을때까지 반복
while True:
    # 왼쪽으로 돌고 그 값만큼 x,y 이동
    dir -= 1
    if dir == -1: # 음수 인덱스 가능하지만 가독성 좋게 인덱스가 -1되면 3으로 변환
        dir = 3
    # 새로 바라본 방향 기준으로 이동한 좌표인 nx, ny 생성
    nx = x + directions[dir][0]
    ny = y + directions[dir][1]

    # 그리고 그 이동한 좌표의 칸이 처음인지 + 육지인지 체크하고 이동할지 결정
    if gameMap[nx][ny] == 0 and visited[nx][ny] == 0: # 처음가고, 육지라면 이동 가능
        x,y = nx,ny
        visited[x][y] = 1
        cnt += 1
        turnCnt = 0

    # 이동하기 여의치 않은 경우에 다시 왼쪽으로 돌기
    else:
        turnCnt += 1

    # 한 자리에서 한바퀴 돌았는데도 갈 곳이 없으면 뒤로 빠꾸
    if turnCnt == 4:
        nx = x-directions[dir][0]
        ny = y-directions[dir][1]
        # 뒤에가 바다가 아니면 빠꾸 가능
        if gameMap[nx][ny] == 0:
            x,y = nx,ny
        # 뒤에마저 바다면 갈 곳 없음 게임 끝 ㅈㅈ
        else: break
        # 빠꾸했으면 가서 다시 또 돌아야되니까 turnCnt 초기화
        turnCnt = 0

print(cnt)
