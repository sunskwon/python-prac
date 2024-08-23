# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

# 참고
# y, m, d = input().split('.')
# 과 같이 변수들을 순서대로 나열하면 구분기호를 기준으로 잘라 순서대로 저장한다.

str_input = input("yyyy.mm.dd : ").split(".")

try:
    y = int(str_input[0])
    m = int(str_input[1])
    d = int(str_input[2])

    if y * m * d == 0 or m > 12 or d > 31:
        print("연.월.일에 적합하지 않은 값입니다")
    elif m in [2, 4, 6, 9, 11] and d > 30:
        print("연.월.일에 적합하지 않은 값입니다")
    else:
        print(d, m, y, sep="-")
except ValueError:
    print("정수 타입의 연.월.일 값을 입력하세요")