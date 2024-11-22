# 큰 수를 표현할 때 자릿수를 쉽게 구분하기 위해 천단위 구분 기호인 콤마(,)를 사용한다.

# 어떤 수가 입력되면 천단위 구분 기호를 넣어 그 수를 다시 출력하는 프로그램을 작성하시오.

try:
    n = int(input())
    num = input()

    answer = ''

    while len(num) > 0:
        if len(num) < 3:
            answer = num + answer
            num = ''
        else:
            answer = ',' + num[-3:] + answer
            num = num[:-3]
    
    print(answer)
except Exception as e:
    print(e)