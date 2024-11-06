# 어떤 
# 10
# 진수 
# n
# 이 주어지면 
# 2
# 진수로 변환해서 출력하시오.

# 예)

# 10    ----->  1010

# 0    ----->  0

# 1    ----->  1

# 2    ----->  10

# 1024    ----->  10000000000

# 이 문제는 반복문을 이용하여 풀 수 없습니다.

try:
    n = int(input())
    answer = ''

    while n > 1:
        answer = str(n % 2) + answer
        n = n // 2

    answer = str(n % 2) + answer

    print(answer)
except Exception as e:
    print(e)