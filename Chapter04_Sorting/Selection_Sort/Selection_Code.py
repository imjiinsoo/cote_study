# 삽입 정렬 소스 코드
# 시간복잡도는 O(N^2)
# 근거 1 : 근사치는 n*(n+1)/2
# 근거 2 : 이중배열

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j # 최솟값의 인덱스 위치를 반복문을 돌면서 갱신되고, 최소값을 가진 인덱스값이 min_index에 들어가게 됨.
    array[i], array[min_index] = array[min_index], array[i] # 스와핑(두 인덱스 자리 바꾸기) # 한 번 루프를 돌면 최소값이 맨 앞으로 오게 됨.


print(array)

# 가장 작은 데이터를 찾는 일이 코테에 빈번하다 함.
# 이 형태에 익숙해지라 함.