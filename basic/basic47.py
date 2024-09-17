# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

# 예시
# a = 2
# b = 10
# print(a << b)  #210 = 1024 가 출력된다.

# 참고
# 예를 들어 1 3 이 입력되면 1을 23(8)배 하여 출력한다.

str_input = input("임의의 정수 2개(띄어쓰기로 구분): ").split(" ")

if len(str_input) != 2:
    print("2개만 입력하세요")
else:
    try:
        a = int(str_input[0])
        b = int(str_input[1])

        print(a << b)
    except ValueError:
        print("정수형을 입력하세요")