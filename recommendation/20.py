# 주현이 엄마는 '기억력 테스트 6'이 너무 가혹해서인지 이번에는 좀 쉬운 테스트를 하기로 했다.

# 이번에도 n개의 숫자를 불러 주고, m개의 질문을 한다.

# 질문은 두 수 a, b를 이야기 하는데, a번째와 b번째 사이에 불렀던 수들의 합을 묻는다.

# 예를 들어, 3 5 2 1 4 3 의 숫자를 불러주고,  2, 4라고 질문하면 2번째에서 4번째 불렀던 숫자들의 합인 8을 대답해야한다.

# 이번 테스트를 무사히 통과하면 '닌자 고'의 4종 캐릭터 장난감을 받을 수 있다.

try:
    n, m = input().split()
    nums = input().split()
    q = []
    for _ in range(int(m)):
        q.append(input().split())
    

    for i in range(len(q)):
        answer = 0
        for j in range(int(q[i][0]) - 1, int(q[i][1])):
            answer += int(nums[j])
        print(answer)
except Exception as e:
    print(e)