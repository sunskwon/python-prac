# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

# 참고
# s = input()
# print(s[0:2])

# 를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다.
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
# 다른 자르기 방법도 있다.

str_input = input("6자리 연월일(YYMMDD) : ")

if len(str_input) != 6:
    print("6자리 형식으로 입력하세요")
else:
    try:
        y = str_input[:2]
        m = str_input[2:4]
        d = str_input[4:]

        print(y, m, d, sep=" ")
    except ValueError:
        print("정수 형태의 값을 입력하세요")