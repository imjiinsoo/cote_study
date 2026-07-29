# 그리디 알고리즘 복습
# 프로그래머스 그리디 알고리즘 체육복 문제
# 체육복은 앞번호 혹은 뒷번호 학생에게만 빌릴 수 있다. 체육 수업을 들을 수 있는 최댓값을 return하는 함수 solution을 만들어라
# n = 학생 수 | lost = 체육복을 도난당한 사람의 수 | reserve = 여벌의 체육복이 있는 학생

def solution(n, lost, reserve):
    answer = 0

    # 여벌의 체육복이 있지만 도난을 당한 학생까지 고려해서 처음에 두 배열 필터링해놓기 1,3,5 | 2,3(여벌)
    for i in lost[:]:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    # 본 로직 시작
    for n in range(1, n+1):
        if n in lost: # 만약 학생이 체육복이 없다면?
            for i in [n-1,n+1]: # n번 학생 앞뒤로 체육복 있는지 체크
                if i in reserve: # 앞뒤 학생중 한명이라도 여벌 체육복 있는지 확인. 있다면 answer에 1추가하고 reserve에서 빌려준 학생 빼기
                    answer += 1
                    reserve.remove(i)
                    break
                else: continue
        else:
            answer += 1
            continue # 체육복 있으면 answer에 그대로 1추가하고 넘어가
    return answer

print(solution(5,[2,4],[4]))