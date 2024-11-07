# SuperSum 함수는 다음과 같이 정의된다.
      
# SuperSum(0, n) = n (n은  모든 양의 정수)
      
# SuperSum(k, n) = SuperSum(k − 1, 1) + SuperSum(k − 1, 2) + ... + SuperSum(k − 1, n)

# k와 n이 여러개 주어진다. SuperSum의 값을 각각 출력하시오.

inputs = input().split()

def SuperSum(k, n):

    result = 0

    if k > 1:
        for i in range(1, n + 1):
            result += SuperSum(k - 1, i)

    if k == 1:
        for i in range(1, n + 1):
            result += i

    return result

try:
    k = int(inputs[0])
    n = int(inputs[1])

    print(k, n)
 
    answer = SuperSum(k, n)

    print(answer)
except Exception as e:
    print(e)