# 실전 문제3. 180p
# 성적이 낮은 순서대로 학생 이름 출력하기
# 학생 이름, 성적(띄어쓰기 기준) -> 성적을 기준으로(오름차순) 이름만 출력
# <입력 예시>
# 2
# 홍길동 95
# 이순신 77
# <출력 예시>
# 이순신 홍길동

n = int(input())

array = []*n

for i in range(n):
    L = input().split() # L은 리스트임. -> ['홍길동', '95'] 이렇게 됨.
    print(L)
    array.append((L[0],int(L[1])))

def setting(data):
    return data[1]

sorted_array = sorted(array,key=setting) # key 라이브러리 활용
for i in range(n):
    print(sorted_array[i][0], end=' ')  # 이름만 출력하기

# array = sorted(array,key=lambda student:student[1])
# for student in array:
#     print(student[0], end=' ')