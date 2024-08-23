# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

# 어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.

str_input = input("'hh:mm:ss 형식의 시간 입력 : ")

if len(str_input) != 8:
    print("형식에 맞게 입력하세요")
else:
    try:
        m = int(str_input.split(":")[1])

        print(m)
    except ValueError:
        print("정수 형태의 자료를 입력하세요")