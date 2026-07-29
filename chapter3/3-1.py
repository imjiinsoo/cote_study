# 거슬러줄 최소의 동전 개수
# 입력 거스름돈 1260원
n = 1260
# 동전 수 카운터
cnt = 0

# 동전 종류
coins = [500,100,50,10]

for c in coins:
    cnt += n//c
    n = n%c

print(f'받은 동전의 수 = {cnt}')