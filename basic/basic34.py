# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = a - b
# print(c)

# 참고
# 수 - 수는 차(subtraction)가 계산된다.

try:
    str_input = input("임의의 정수(띄어쓰기로 구분): ").split(" ")
    if len(str_input) != 2:
        print("2개의 정수를 입력하세요")
    else:
        a = int(str_input[0])
        b = int(str_input[1])
        print(a - b)
except ValueError:
    print("정수를 입력하세요")