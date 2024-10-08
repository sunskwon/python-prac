# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# 예시
# ...
# if a%2==0 :
#   print("even")
# else :
#   print("odd") 
# ...

# 참고 
# if 조건식 :  #조건식을 평가해서...
#   실행1      #True 인 경우 실행시킬 명령들...
#   실행2
# else :        
#   실행3      #False 인 경우 실행시킬 명령들...
#   실행4
# 실행5       #조건식과 상관없는 다음 명령
# ...

# else 는 if 없이 혼자 사용되지 않는다.
# 또한, else 다음에는 조건식이 없는 이유는? True(참)가 아니면 False(거짓)이기 때문에... 
# 조건식의 평가 결과는 True 아니면 False 로 계산되기 때문이다.

# python 에서는 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확하게 해주어야 한다.

str_input = input("임의의 정수 3개(띄어쓰기로 구분): ").split()

if len(str_input) != 3:
    print("3개만 입력하세요")
else:
    try:
        for i in range(len(str_input)):
            temp = int(str_input[i])

            if temp % 2 == 0:
                print("even")
            else:
                print("odd")
    except ValueError:
        print("정수를 입력하세요")