# 파이썬의 장점을 살린 퀵 정렬 소스코드
# 시간 측면에서 Quick_Sort_1보다 비효율적이지만 더 직관적임.

# 평균적인 시간복잡도는 O(NlogN) 최악의 경우 O(n^2)
# 데이터가 이미 정렬되어 있는 경우 매우 느리게 동작. 삽입 정렬과 반대임.
# 데이터가 굉장히 무작위적으로 정렬되어 있을 때가 최적임.

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))