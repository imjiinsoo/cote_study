# 프로그래머스 알고리즘 고득점 kit 네트워크 문제

# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
# 예시 : n = 3 , computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]], return값 : 2

def solution(n,computers):
    visited = [False] * n  # 방명록임.

    def dfs(start):
        visited[start] = True  # 다녀간 해당 노드는 True로 바꿔줌.

        for i in range(n):
            if not visited[i] and computers[start][i] == 1:  # 안 다녀간 노드 중에 연결된 노드로 가기.
                dfs(i)  # 연결된 노드로 탐색하러 감.

    answer = 0
    for j in range(n): # 코드 동작 시작
        if not visited[j]: # 방문하지 않은 노드일 때
            dfs(j) # j번의 노드 방문 기록해주고, j번 노드와 연결된 노드를 탐색하기.
            answer += 1 # 탐색을 다 마치고 오면 1증가
    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])


# 코테에서는 재귀함수를 쓰는 문제가 나오면 전역변수는 지양하는게 좋은 듯.

