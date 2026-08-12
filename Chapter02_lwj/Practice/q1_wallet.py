# 명함 지갑 만들기

# 가로 세로 중 큰 값을 w에 작은 값을 h로 자리 이동을 시켜주고 각 변수의 최대값끼리 곱하면 끗.

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

# changed_list = sizes 이 로직은 두 리스트가 같은 메모리를 쓰고 있기 때문에 changed_list값이 바뀌면 sizes도 같이 변함.
# 즉, 변수명만 다를 뿐 메모리도 같은 리스트임. 리스트는 이런 걸 조심해야 함.

# 리스트 슬라이싱을 활용해야 함.
changed_list = []
for row in sizes:
    changed_list.append(row[:])
# changed_list = [row[:] for row in sizes] 로 컴프리헨션 할 수 있음.

w_list = [0] * len(sizes)
h_list = [0] * len(sizes)

for i in range(len(sizes)):
    if sizes[i][0] < sizes[i][1]:
        changed_list[i][0] = sizes[i][1]
        changed_list[i][1] = sizes[i][0]
    w_list[i] = changed_list[i][0]
    h_list[i] = changed_list[i][1]
answer = max(w_list) * max(h_list)

print(answer)