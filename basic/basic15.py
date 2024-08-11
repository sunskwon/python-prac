# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

# 예시
# a, b = input().split(':')
# print(a, b, sep=':')
# 와 같은 방법으로 가능하다.

# 참고
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
# sep 는 분류기호(seperator)를 의미한다.
try:
    str_input = input("hh:mm : ").split(":")
    a = int(str_input[0])
    b = int(str_input[1])

    if a > 24 or b > 60 or a * b == 0:
        print("시간 형식이 아닙니다")
    else:
        print(a, b, sep=":")
except ValueError:
    print("정수형의 시간을 입력하세요")