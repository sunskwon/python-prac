# 두 정수 a, b의 약수를 모두 출력하는 프로그램을 작성하시오.

nums = input().split()

try:
    a = int(nums[0])
    b = int(nums[1])

    answer = []

    if a >= b:
        for i in range(1, a + 1):
            if a % i == 0:
                answer.append(i)
            if b % i == 0:
                answer.append(i)
    else:
        for i in range(1, b + 1):
            if a % i == 0:
                answer.append(i)
            if b % i == 0:
                answer.append(i)
    
    answer = list(set(answer))
    
    for i in range(len(answer)):
        print(answer[i], end=' ')
except Exception as e:
    print(e)