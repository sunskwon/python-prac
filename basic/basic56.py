# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = bool(int(a))
# d = bool(int(b))
# print((c and (not d)) or ((not c) and d))

# 참고
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.

# 논리연산자는 사칙(+, -, *, /) 연산자와 마찬가지로 여러 번 중복해서 사용할 수 있는데, 
# 사칙 연산자와 마찬가지로 계산 순서를 표시하기 위해 괄호 ( )를 사용할 수 있다.
# 괄호를 사용하면 계산 순서를 명확하게 표현할 수 있다.

# 수학 식에서는 소괄호 (), 중괄호 {}, 대괄호 []를 사용하기도 하지만, 프로그래밍언어에서는 소괄호 ( ) 만 사용한다.

# ** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.

str_input = input("임의의 정수 2개(띄어쓰기로 구분): ").split(" ")

if len(str_input) != 2:
    print("2개만 입력하세요")
else:
    try:
        a = int(str_input[0])
        b = int(str_input[1])

        print((a and not b) or (not a and b))
    except ValueError:
        print("정수만 입력하세요")