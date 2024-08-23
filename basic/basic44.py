# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

str_input = input("임의의 정수 2개(띄어쓰기로 구분): ").split(" ")

if len(str_input) != 2:
    print("2개의 정수만 입력하세요")
else:
    try:
        a = int(str_input[0])
        b = int(str_input[1])

        if b == 0:
            print("두번째 정수는 0이 될 수 없습니다")
        else:
            print(f"a + b = {a + b}")
            print(f"a - b = {a - b}")
            print(f"a * b = {a * b}")
            print(f"a // b = {a // b}")
            print(f"a % b = {a % b}")
            print(f"a / b = {a / b}")
    except ValueError:
        print("정수를 입력하세요")