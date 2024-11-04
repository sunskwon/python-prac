# 콜라츠의 추측, 3n+1 문제, 우박수 문제라고 불리는 이 문제는 다음과 같다.

# 1, 어떤 자연수 n이 입력되면,

# 2. n이 홀수이면 3n+1을 하고,

# 3. n이 짝수이면 n/2를 한다.

# 4. 이 n이 1이 될때까지 2~3과정을 반복한다.

# 예를 들어 5는 5 → 16 → 8 → 4 → 2 → 1 이 된다.

# 여기서 5가 1이되기 위해 6개의 숫자를 나열하게 된다. 이것을 길이라고 하면 5의 길이는 6이된다.

# 시작수와 마지막 수가 입력되면 그 두 사이게 길이가 가장긴 우박수와 그 길이를 출력하시오.

try:
    inputs = input().split()

    ans_num = 0
    ans_repeat = 0

    for i in range(int(inputs[0]), int(inputs[1]) + 1):
        
        num = i
        repeat = 1

        while num > 1:
            if num % 2 == 0:
                num = num // 2
                repeat += 1
            else:
                num = num * 3 + 1
                repeat += 1

        if repeat > ans_repeat:
            ans_num = i
            ans_repeat = repeat
    
    print(ans_num, ans_repeat)

except Exception as e:
    print(e)
