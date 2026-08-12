# 숫자 카드 게임
# 2 4 라 하면 배열 2개 생성에 4개의 수를 입력 받음.

# 행, 열 수 입력받기
n, m = map(int, input().split())

# 2차원 배열로 행 입력 받기
# 1차원 배열을 행의 수(n)만큼 받음
array = [[int(i) for i in input().split()] for j in range(n)]

# 각 행 마다 최솟값을 구해 배열에 삽입
min_array = [0] * n
for i in range(n):
    min_array[i] = min(array[i])

# 각 행의 최솟값 중 제일 큰 값 출력
result = max(min_array)

print(result)