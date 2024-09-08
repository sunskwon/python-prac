# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

try:
    n = int(input("임의의 정수: "))

    if n < 0 or n > 100:
        print("0부터 100 사이의 정수를 입력하세요")
    else:
        i = 0
        while i <= n:
            print(i)
            i += 1
except Exception as e:
    print(e)