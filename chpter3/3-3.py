# 숫자 카드 게임 M=행의 수 / N= 열의 수
# 행에서 가장 낮은 카드중에서 제일 큰 수 찾기
n,m = map(int,input().split()) # 2행 4열 가정
ans = 0 # 정답 담을 변수
for i in range(n): # 모든 행에서 반복
    row = list(map(int,input().split())) # 예: 입력 = 3 1 2 / row = [3,1,2]
    rowMin = min(row)
    ans = max(rowMin,ans) # 작은 놈들 중에서 제일 큰 놈이 ans

print(ans)