# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

# 참고
# 입력되는 값은 기본적으로 문자열로 인식된다.

# 숫자로 구성된 문자열이나 정수를 실수(real number) 값으로 바꾸기 위해서는 float( ) 를 사용할 수 있다.
# 소숫점(.)은 그 위치가 정해져있지 않고 이리저리 둥둥 떠다니므로, floating point라고 부른다.

str_input = input("임의의 실수 2개(띄어쓰기로 구분) : ").split(" ")

if len(str_input) != 2:
    print("2개의 실수만 입력하세요")
else:
    try:
        a = float(str_input[0])
        b = float(str_input[1])
        
        print(a + b)
    except ValueError:
        print("실수를 입력하세요")