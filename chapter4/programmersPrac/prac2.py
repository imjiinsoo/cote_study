# 프로그래머스 완전탐색 모의고사 문제

def solution(answers):
    answer = []

    # 학생들이 찍는 방법
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]

    # 각 학생 맞은 수 카운터
    s1Cnt, s2Cnt, s3Cnt = 0,0,0

    for i in range(len(answers)):
        if answers[i] == stu1[i%len(stu1)]:
            s1Cnt += 1
        if answers[i] == stu2[i%len(stu2)]:
            s2Cnt += 1
        if answers[i] == stu3[i%len(stu3)]:
            s3Cnt += 1

    # 고득점자 색출을 위해 for문을 쓸 예정이니까 카운터들을 리스트로 묶기
    cntList = [s1Cnt, s2Cnt, s3Cnt]

    # 고득점자 색출
    # 제일 고득점자 점수 high_grade 변수에 담기
    high_grade = max(cntList)

    # high_grade 값과 같은 애들은 리스트에 다 넣기
    for c in range(len(cntList)):
        if high_grade == cntList[c]:
            answer.append(c+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

