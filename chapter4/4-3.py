# 왕실의 나이트

# 좌표 일단 입력받기 ex. b3
position = input()

# 좌표계산은 숫자로 해야되니까 아스키코드 사용해서 알파벳(column)도 숫자 좌표로 변환
col = ord(position[0])-ord('a')+1 # ex. ord('b')-ord('a')+1 = 2니까 b는 2로 취급 가능해짐
row = int(position[1]) # ex. 3받아서 int형으로 변환

# 움직이는 경우의 수 담아놓기
next = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]

# 정답 담을 카운터
cnt = 0

# 입력받은 시작 위치에서 각 next값으로 움직여보고 벗어나는지 확인
for n in next:
    nextCol = col + n[0]
    nextRow = row + n[1]
    # 행, 열이 이동 후에 1이상 8이하면 가능한 경우니까 카운터 추가
    if nextCol >= 1 and nextCol <= 8 and nextRow >= 1 and nextRow <= 8:
        cnt += 1

print(cnt)

