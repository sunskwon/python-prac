# 숫자에 관심이 많은 영일이는 수열을 보고 오름차순 수열인지 내림차순 수열인지 판단하려고 한다.

# 오름차순이란 작은 수부터 큰 수 순서로 나열한것을 말하고, 내림차순은 그 반대인 경우이다.

# 이 두 경우가 아닌 경우는 '섞임'으로 판단한다.

# n개의 수가 주어지면, '오름차순', '내림차순', '섞임'을 판단하는 프로그램을 작성하시오.

# 예를 들어, 1 1 2 3 5 5 6인 경우 '오름차순', 7 6 6 5 3 1인 경우 '내림차순',  21 22 21 22인 경우 '섞임'으로 판단한다.

# 만약 모두 같은 수가 입력되면 '섞임'으로 판단한다.

try:
    n = int(input())
    num_array = input().split()
    nums = list(int(num) for num in num_array)

    num_sort = sorted(nums)

    if num_sort[0] == num_sort[-1]:
        print('섞임')
    else:
        if nums == num_sort:
            print('오름차순')
        elif nums == sorted(nums, reverse=True):
            print('내림차순')
        else:
            print('섞임')

except Exception as e:
    print(e)