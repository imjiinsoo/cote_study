# 큰 수의 법칙

# 다양한 수로 이루어진 배열이 있을 떄 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없음.

# 예 [1,2,3,4,5], [3,2,4,1,5]
# k = 3, m = 8
# 5*3 + 4 + 5*3 + 4


n,m,k = map(int,input().split())

Data = list(map(int,input().split()))

# 가장 큰 수 및 그 수의 인덱스 구하기
max_i = 0
for i in range(n):
    if Data[i] != max(Data):
        i += 1
    else:
        max_i = i

# 두 번째 큰 수의 인덱스 구하기
# 슬라이싱 활용

second_max = max(Data[:max_i]+Data[(max_i+1):])

# 출력

# k가 m보다 작으면 최댓값에 m을 곱한 값
if m <= k:
    print(max(Data) * m)
    
# m이 k보다 클 때
elif m > k:
    print(((max(Data) * k) + second_max) * (m // (k+1)) + (max(Data)*(m%(k+1))))