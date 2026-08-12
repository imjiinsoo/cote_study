# 2가지 방식으로 구현하는 팩토리얼

# 첫번째, 반복분
def fac_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 두번째, 재귀
def fac_recur(n):
    if n <= 1:
        return 1
    return n * fac_recur(n-1)

# 두가지 다 출력
print(fac_iter(5))
print(fac_recur(5))