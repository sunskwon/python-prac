# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

# 예시
# ...
# for i in range(1, n+1) :
#   for j in range(1, m+1) :
#     print(i, j)
# ...

# 참고
# 위 코드는
# 바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에
# 안쪽의 j 값이 다시 1부터 m까지 변하며 출력되는 코드이다.

# 조건선택 실행구조 안에 다른 조건선택 실행구조를 넣어 처리할 수 있는 것과 마찬가지로
# 반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.

# 원하는 형태로 실행 구조를 결합하거나 중첩시킬 수 있다.

try:
    x = int(input("임의의 정수1: "))
    y = int(input("임의의 정수2: "))

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(i, j)
except Exception as e:
    print(e)