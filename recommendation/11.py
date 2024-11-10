# 성근이는 오름차순과 내림차순에 대한 공부를 하고 있다.

# 어떤 수 n개가 주어지면 그 수열이 오름차순인지, 내림차순인지, 섞여 있는지 판단하시오.

try:
    n = int(input())
    inputs = input().split()

    org = []
    
    for i in range(n):
        org.append(int(inputs[i]))
    
    comp = org.copy()

    if org == sorted(comp):
        print("오름차순")
    elif org == sorted(comp, reverse=True):
        print('내림차순')
    else:
        print('섞임')
    
except Exception as e:
    print(e)
