# 프로그래머스 완전탐색 모의고사
# 답이 주어지면 가장 맞춘 사람이 출력됨. 맞춘 개수가 같으면 오름차순으로 출력함
# 1번 : 1,2,3,4,5 반복
# 2번 : 2,1,2,3,2,4,2,5 반복
# 3번 : 3,3,1,1,2,2,4,4,5,5 반복
# answers가 리스트로 입력이 되고
# 출력값고 리스트로 반환해야 함.
# 리스트에 인자 하나 추가는 append(), 두 개 이상 추가는 extend([])


def solution(answers):
    no_1 = [1,2,3,4,5]*2000
    cnt_1 = 0 # 1번 수포자 답 맞춘 개수

    no_2 = [2,1,2,3,2,4,2,5]*(10000//8)
    cnt_2 = 0

    no_3 = [3,3,1,1,2,2,4,4,5,5]*1000
    cnt_3 = 0

    answer = []
    for i in range(len(answers)):
        if no_1[i] == answers[i]:
            cnt_1 += 1
        if no_2[i] == answers[i]:
            cnt_2 += 1
        if no_3[i] == answers[i]:
            cnt_3 += 1
    cnt_list = [cnt_1,cnt_2,cnt_3]
    if max(cnt_list) == cnt_1:
        if cnt_1 == cnt_2 == cnt_3:
            answer.extend([1,2,3])
        elif cnt_1 == cnt_2 != cnt_3:
            answer.extend([1,2])
        elif cnt_1 == cnt_3 != cnt_2:
            answer.extend([1,3])
        elif cnt_1 != cnt_2 and cnt_1 != cnt_3:
            answer.append(1)
    if max(cnt_list) == cnt_2:
        if cnt_2 == cnt_3 != cnt_1:
            answer.extend([2,3])
        elif cnt_2 != cnt_3 and cnt_2 != cnt_1:
            answer.append(2)
    if max(cnt_list) == cnt_3:
        if cnt_3 != cnt_1 and  cnt_3 != cnt_2:
            answer.append(3)
    return answer

answers = [1,3,2,4,2]
print(solution(answers))
# 노가다 안 하는 방법 없나