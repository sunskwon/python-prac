# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

# 예시
# a = input() 
# b = input()
# a=int(a)
# b=int(b)
# print(a)
# print(b)
# 과 같은 방법으로 가능하다.

str_input = input("정수 2개 입력(띄어쓰기로 구분) : ").split(" ")
int_input = []

if len(str_input) > 2 or len(str_input) < 1:
    print("2개만 입력하세요")
else:
    try:
        for item in str_input:
            int_input.append(int(item))
        
        print(int_input[0])
        print(int_input[1])
    except ValueError:
        print("정수만 입력하세요")
