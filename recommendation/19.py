# 주현이 엄마는 주현이를 영재로 키우기 위해 매일 혹독한 기억력 테스트를 하고 있다.

# N개의 숫자를 먼저 말해주고, M개의 질문을 하면서 그 숫자를 몇 번째로 불렀는지 테스트한다.

# 이번 테스트가 어려울 것을 예상하여 N개의 데이터를 부를 때 오름차순으로 부른다.

# 이 테스트를 통과할 경우 주현이는 최신 장난감 "또봇 W 쉴드온"을 받을 수 있다.

# 주현이를 도와 줄수 있는 프로그램을 작성하시오.

try:
    n = int(input())
    nums = input().split()
    m = int(input())
    q = input().split()

    for i in range(m):
        if q[i] in nums:
            print(nums.index(q[i]) + 1, end=' ')
        else:
            print('-1 ', end='')
except Exception as e:
    print(e)