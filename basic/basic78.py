# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

try:
    c = input("임의의 영문자: ")

    while c != 'q':
        print(c)
        c = input("다시 입력하세요: ")
    
    print(c)
except Exception as e:
    print(e)