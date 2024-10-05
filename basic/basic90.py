# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

# 예를 들어
# 1 -1 3 -5 11 -21 43 ... 은
# 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.

# 이런 이상한 수열을 알게 된 영일이는 또 궁금해졌다.
# "그럼.... 13번째 나오는 수는 뭘까?"

# 영일이는 물론 수학을 아주 잘하지만 이런 문제는 본 적이 거의 없었다...
# 그래서 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램을 만들어보자.

str_input = input("a, m, d, n: ").split()

if len(str_input) == 4:
    try:
        a = int(str_input[0])
        m = int(str_input[1])
        d = int(str_input[2])
        n = int(str_input[3])

        result = 0
        
        for i in range(n + 1):
            if i == 1:
                result = a
            else:
                result *= m
                result += d

        print(result)
    except Exception as e:
        print(e)
else:
    print("input error")