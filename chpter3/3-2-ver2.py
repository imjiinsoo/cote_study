# 수학적 요소 살짝 첨가한 ver2 (시간복잡도 개선)
# k+1의 주기로 수열이 반복됨 3-2의 문제의 예시에서는 6,6,6,5가 4의 크기의 주기로 반복
# k가 더해지는 횟수 = int(M / K+1) * K + M % (K+1) <- 뒤에 M % (K+1)는 M이 K+1로 나누어 떨어지지 않는 경우에 K가 그 나머지만큼 또 더해져야됨
N,M,K = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort()
a,b = nlist[-1], nlist[-2] # 이까진 동일

# 가장 큰 수 a가 더해지는 횟수 계산
cnt = int(M / (K+1))*K + M % (K+1)

result = 0
result += cnt * a # 젤 큰 수 더하기
result += (M-cnt) * b # 두번째 큰 수 더하기. 총 횟수 M에서 a가 더해진 cnt만큼만 빼면 b가 더해진 횟수
print(result)