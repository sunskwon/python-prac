# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

# 예시
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# 참고
# 입력되는 값은 기본적으로 문자열로 인식된다.

# 문자열 + 문자열은 두 문자열을 합친 문자열을 만든다.
# 숫자로 구성된 문자열이나 실수를 정수(integer) 값으로 바꾸기 위해서는 int( ) 를 사용할 수 있다.
# 수 + 수의 결과는 합(addition)이 계산된다.

str_input = input("임의의 정수 2개(띄어쓰기로 구분) :").split(" ")

if len(str_input) > 2:
    print("2개의 정수만 입력하세요")
else:
    try:
        a = int(str_input[0])
        b = int(str_input[1])

        print(a + b)
    except ValueError:
        print("정수 형태의 숫자를 입력하세요")