# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

char_a = input("첫 번째 문자 : ")
char_b = input("두 번째 문자 : ")

if len(char_a) * len(char_b) != 1:
    print("1자리의 문자를 입력하세요")
else:
    print(char_b)
    print(char_a)