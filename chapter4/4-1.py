# 상하좌우 문제
# n = 정사각형 변 길이 | 아랫줄은 이동 방향 R,L,U,D

n = int(input("정사각형의 크기: "))
d = list(input().split())
ans = [1,1]
for i in d:
    if i == "R":
        if ans[1] == n:
            continue
        ans[1] += 1
    elif i == "L":
        if ans[1] == 1:
            continue
        ans[1] -= 1
    elif i == "U":
        if ans[0] == 1:
            continue
        ans[0] -= 1
    else:
        if ans[0] == n:
            continue
        ans[0] += 1
print(f"{ans[0]} {ans[1]}")