# 상하좌우
# N x N 크기의 정사각형 공간
# 시작 좌표는 항상 (1,1), 가장 오른쪽 아래의 좌표는 (N,N)
# L : 왼쪽으로 한 칸 이동, R : 오른쪽으로 한 칸 이동, U : 위로 한 칸 이동, D : 아래로 한 칸 이동
# 공간 밖으로 가는 명령은 무시

# 맵의 크기 입력 받기
N = map(int,input().split())

# 이동 계획 입력 받기(문자열 입력은 map 함수 안 씀)
m = list(input().split())

# 좌표 x,y에 현재 좌표 위치 입력
x = 1
y = 1

# 반복문을 활용해 좌표 이동
# 공간 밖으로 가는 명령 무시

for i in range(len(m)):
    if m[i] == 'R':
        if x != N:
            x += 1

    if m[i] == 'L':
        if x != 1:
            x -= 1

    if m[i] == 'D':
        if y != N:
            y += 1

    if m[i] == 'U':
        if y != 1:
            y -= 1

print(y," ", x)
