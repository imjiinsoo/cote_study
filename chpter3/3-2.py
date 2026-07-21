# 큰 수의 법칙
# 특정 숫자 리스트가 있을 때 주어진 수들을 이용해서 가장 큰 수를 만드는 법칙
# 주어진 수를 M번 더하되, 특정 인덱스의 숫자를 K번 초과하여 연속으로 쓸 수 없다
# 첫줄에 N, M, K가 주어지고 두번째 줄에 N개의 자연수가 주어짐
# K는 M보다 항상 작거나 같다

# idea: 입력받는 애들 중에서 가장 큰 숫자를 k번 더하고 두번째로 큰 수를 한번 더하고 또 다시 큰 숫자 k번 더하길 반복
N,M,K = map(int,input().split()) # N = 5, M = 8, K = 3
nlist = list(map(int,input().split()))

# 오름차순으로 정렬. nlist = [2,4,4,5,6]
nlist.sort()

# 젤큰수를 a, 두번째로 큰 수를 b로
a,b = nlist[-1], nlist[-2]

sum = 0
cnt = 0
# a를 K번 더하고 b를 한번 더하는 식으로 M(8)번 반복
for i in range(M):
    if cnt < K:
        sum += a
        cnt += 1
    else:
        sum += b
        cnt = 0

print(sum)