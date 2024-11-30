# 테스트 3을 무사히 마친 주현이는 테스트 4에 도전하게 되었다.

# 주현이 엄마는 이번에 무작위로 숫자 N개를 불러준다음, M개의 질문을 하기로 했다.

# 질문으로 그 숫자가 있었으면 그 숫자를 몇 번째로 불렀는지 출력하고, 없었다면 -1을 출력한다.

# 이 테스트에는 주현이가 좋아하는 '또봇 X, Y, Z'가 걸려있다.

# 주현이를 도와줄수 있는 프로그램을 만드시오.

try:
    n = int(input())
    nums = input().split()
    m = int(input())
    q = input().split()

    for i in range(len(q)):
        if q[i] in nums:
            print(nums.index(q[i]) + 1, end=' ')
        else:
            print('-1', end=' ')
except Exception as e:
    print(e)
