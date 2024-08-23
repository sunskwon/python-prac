# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

str_input = input("임의의 정수 2개(띄어쓰기로 구분): ").split(" ")

if len(str_input) != 2:
    print("2개만 입력하세요")
else:
    try:
        a = int(str_input[0])
        b = int(str_input[1])

        print(bool(a and b) or bool(not a and not b))
    except ValueError:
        print("정수를 입력하세요")