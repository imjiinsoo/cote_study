# 프로그래머스 BFS/DFS 고득점 알고리즘 kit
# 타겟 넘버
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성
# 예 numbers == [1,1,1,1,1], target == 3, 반환값은 5(5가지 경우로 타겟값 완성)

# 계획은 모든 경우의 수를 구하고 경우를 충족하는 경우에 정답을 하나씩 갱신하기

numbers = [1,1,1]
target = 1
cnt = 0

def bfs(start, total):
    global cnt

    if start == len(numbers):
        if total == target:
            cnt += 1
        return cnt


    bfs(start+1, total + numbers[start])
    bfs(start+1, total - numbers[start])

    return cnt

print(dfs(0,0))

