# N개의 입력 데이터가 주어지면 정렬해서 출력하시오.

 

# 입력 예)

# 5

# 2 5 8 1 2

# 출력 예)

# 1 2 2 5 8

try:
    n = int(input())
    nums = input().split()
    answer = []

    for i in range(n):
        answer.append(int(nums[i]))
        
    nums = sorted(nums)

    print(' '.join(nums))
except Exception as e:
    print(e)