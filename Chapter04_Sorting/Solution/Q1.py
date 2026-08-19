# 위에서 아래로
# 내림차순 정렬(띄어쓰기를 기준으로)

n = int(input()) # 받을 숫자의 개수
L = []*n

for i in range(n):
    L.append(int(input())) # 원소 하나씩 받기

# 내림차순 출력

# result = sorted(L)
# ans = []*n
# for i in range(n):
#     ans.append(result[n-1-i])
#     print(ans[i],end=' ') -> 복잡함.

result = sorted(L, reverse=True) # 정렬 라이브러리 활용하기

for i in result:
    print(i, end= ' ')
