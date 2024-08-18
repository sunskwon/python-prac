# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

# 예시
# w, n = input().split()
# print(w*int(n))

# 참고
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

try:
    str_input = input("단어와 반복 횟수(띄어쓰기로 구분): ").split(" ")

    if len(str_input) != 2:
        print("단어와 반복 횟수만 입력하세요")
    else:
        print(str_input[0] * int(str_input[1]))
except ValueError:
    print("반복 횟수는 정수형태로 입력하세요")