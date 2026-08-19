# 교재 182p. 실전문제 4
# 두 배열의 원소 교체
# N개의 원소, K번 바꿔치기,
# k번 서로 다른 배열의 원소를 교체할 때 배열의 각 원소의 합이 최댓값이 될 때 최댓값 출력

n, k= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Sorted_A = sorted(A)
Reverse_Sorted_B = sorted(B, reverse=True)
for i in range(k):
    if Sorted_A[i] < Reverse_Sorted_B[i]:
        Sorted_A[i], Reverse_Sorted_B[i] = Reverse_Sorted_B[i], Sorted_A[i]
    else:
        break

print(sum(Sorted_A))