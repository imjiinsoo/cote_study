# 계수 정렬
# 데이터의 개수 N, 최댓값의 크기 K -> 시간복잡도는 O(N+K)
# 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을 때 유리.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1) # 가장 큰 수만큼 배열의 인덱스가 늘어남

for i in range(len(array)):
    count[array[i]] += 1 # 데이터 크기에 맞는 인덱스에 1씩 증가시켜줌.

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end =' ') # 띄어쓰기 기준으로 등장 횟수만큼 인덱스 출력.