# 프로그래머스 완전탐색 최소직사각형 문제

def solution(sizes):
    # 모든 가로세로 sort로 정렬하기
    for s in sizes:
        s.sort()

    # 오름차순으로 정렬됐으니까 1번 인덱스 중에서 제일 큰 애 찾기
    width = 0
    for s in sizes:
        if s[1] > width:
            width = s[1]

    # 이제 0번 인덱스 중에서 제일 큰 애를 세로로
    height = 0
    for s in sizes:
        if s[0] > height:
            height = s[0]

    # 리턴값 계산
    answer = width*height
    return answer

# test case
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))