# 어떠한 수 N이 1이 될 때까지 다음의 연산을 수행
# N에서 1을 뺀다
# N을 K로 나눈다.
# 연산 횟수 출력

N, K = map(int, input().split())
count = 0

while True:
    if (N % K != 0):
        N -= 1
        count += 1
        if N == 1:
            break
    else:
        N /= K
        count += 1
        if N == 1:
            break


print(count)