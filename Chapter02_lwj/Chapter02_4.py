# 게임 개발
# NxM 크기의 배열
# 0: 육지, 1: 바다
# 육지만 이동 가능
# 북:0, 동:1, 남:2, 서:3
# 왼쪽(반시계) 방향으로 회전하고 안 가본 육지면 캐릭터를 이동
# 가본 좌표는 넘겨야 함

# 2차원 배열의 x,y 길이 입력 받기
N, M = map(int,input().split())

# A는 북쪽에서 떨어진 칸 수 만큼, B는 서쪽에서 떨어진 칸수 만큼, d로 캐릭터가 바라보는 방향 입력 받기
A,B,d = map(int,input().split())

# 2차원 배열 입력 받기
array_d = [[int(i) for i in input().split()]for j in range(N)]

# 방문한 좌표 기록하기
visited = [[0] * M for _ in range(N)]
visited[A][B] = 1 # 이미 지나간 건 1로 표시(못 가게 하기 위함)

# 북,동,남,서 이동 시 A,B 바뀌는 좌표를 정리
dA = [-1,0,1,0]
dB = [0,1,0,-1]

# 방문한 칸의 개수
count = 1

# 왼쪽으로 회전하는 기능을 담은 함수
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

turn_time = 0 # 회전 4번이면 뒷방향으로 이동시키기 위함

while True:
    turn_left() # 회전
    nA = A + dA[d] # 기존 위치에서 바라보는 방향에 따라 이동한 좌표의 위치
    nB = B + dB[d]
    if array_d[nA][nB] == 0 and visited[nA][nB] == 0: # 육지이고 방문하지 않은 경우
        visited[nA][nB] = 1 # 다시 못 가게
        A = nA # 위치 이동 후 갱신
        B = nB
        count += 1
        turn_time = 0 # 회전 수 갱신
    else:
        turn_time += 1 # 회전해서 찾은 칸이 바다일 경우 turn_time 1씩 증가

    if turn_time == 4: # 동서남북 전부 바다 일 때
        oA = A - dA[d] # 뒷칸 좌표 찾기
        oB = B - dB[d]

        if array_d[oA][oB] == 0: # 뒷칸이 육지일 때
            A = oA
            B = oB
            turn_time = 0
        else:
            break


print(count)