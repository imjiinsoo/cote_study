# 퀵 소트 소스 코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end): # start랑 end는 배열의 범위.
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소임.
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 배열과 오른쪽 배열 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

# def quick_sort(pivot,start,end):
#
#     for i in range(1,len(array)):
#         left = array[i] # 피벗보다 큰 수를 작은 인덱스부터 큰 인덱스 순으로 찾기
#         right = array[len(array)-1] # 피벗보다 작은 수를 큰 인덱스에서 작은 인덱스 순으로 찾기
#         if left > pivot > right:
#             if i > (len(array) - 1):  # left랑 right가 엇갈렸을 때
#                 pivot, right = right, pivot # 피벗과 right 스와프
#                 quick_sort(pivot,)
#                 quick_sort(right,)
#             else:
#                 left, right = right, left # left랑 right가 안 엇갈렸을 땐 스와프
#
#
# quick_sort(array[0],0,len(array)-1) <- 혼자 만들다 실패한 코드