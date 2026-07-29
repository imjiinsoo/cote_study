# 시각 문제
# 정수 n을 입력하면, 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하기
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k) # ex. 24930(2시 49분 30초) 형식의 문자열로 나옴
            if "3" in time:
                cnt += 1

print(cnt)
