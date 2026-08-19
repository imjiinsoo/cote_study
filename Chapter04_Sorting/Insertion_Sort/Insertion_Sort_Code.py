# 삽입 정렬 소스 코드
# 시간복잡도는 이중 반복문이므로 대개 O(N^2)이지만
# 배열이 거의 정렬되어있는 경우라면 시간복잡도는 O(N)임.
# 최선의 시간복잡도는 O(N)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 두번째 인덱스부터 시작함.
    for j in range(i,0,-1): # i부터 0으로 역순으로 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] # 왼쪽으로 자리를 바꾸어나감.
        else:
            break

print(array)

