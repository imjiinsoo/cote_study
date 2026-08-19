# key의 역할은 sorted의 매개변수

# sorted(iterable, key=함수)
# iterable  # 정렬할 데이터
# key       # 어떤 기준으로 정렬할지 정하는 매개변수

array = [('바나나', 2),('사과', 5),('당근',3)]

def setting(data):
    return data[1] # data에 튜플이 하나씩 들어감. data[1]은 숫자값임.
result = sorted(array, key=setting) # 정렬의 기준은 setting값. 즉, 튜플 속 int값임.

print(result)