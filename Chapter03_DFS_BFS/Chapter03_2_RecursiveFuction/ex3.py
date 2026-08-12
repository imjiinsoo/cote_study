# 재귀함수로 팩토리얼 구현
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)

print(recursive_factorial(5))

# 5*함수(4) -> 5*4*함수(3) -> ... -> 5*4*3*2*1