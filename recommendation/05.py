# 별 모양 도형 출력하기에 재미를 붙인 철수는 이번에는 조금 어려운 빗금 친 사각형을 만들어 보기로 했다.

# n
# ∗
# n
#  사각형에서 k간격 마다 빗금을 친 사각형을 출력하는 프로그램을 작성하시오.

# 예를 들어, n=10, k=3이면,

# **********
# **  *  * *
# *  *  *  *
# * *  *  **
# **  *  * *
# *  *  *  *
# * *  *  **
# **  *  * *
# *  *  *  *
# **********
# 윗변을 기준으로 왼쪽에서 부터 k간격마다 ↙방향으로 빗금을 그으시오.

# 10 3인경우,

# **********
#   |  |  |
#  이 위치들(즉, 3의 배수)

try:
    dim = input().split()
    n = int(dim[0])
    k = int(dim[1])

    print('*'*n)
    for i in range(n - 2):
        for j in range(n):
            if j == 0:
                print('*', end='')
            elif j == n-1:
                print('*')
            else:
                if (i + j) % k == 1:
                    print('*', end='')
                else:
                    print(' ', end='')
    print('*'*n)
except Exception as e:
    print(e)