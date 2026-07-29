# n,k 입력받아서 n이 1이 될때까지 -1을 하거나 k로 나누기
# 최소 몇번안에 1이 만들어지는지 계산

n,k = map(int,input().split())
cnt = 0

# k의 배수가 되기 전까지 -1하기
while True:
    if n % k == 0:
        break
    n -= 1
    cnt += 1

# k의 배수가 되었으니 k로 계속 나누기
while True:
    if n == 1:
        break
    n = n//k
    cnt += 1

print(cnt)