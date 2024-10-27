# 우리는 1부터 N까지의 숫자가 차례대로 적힌 N장의 카드 묶음을 가지고 있다.

# 그런 데 이 카드 묶음을 옮기는 중 실수로 땅에 떨어뜨려 그 중 한 장을 잃어버렸다.

# 여러 분은 땅에 떨어진 카드 묶음을 읽어서 빠진 하나의 카드 번호를 찾아 출력해야 한다.

try:
    n = int(input())
    cards = list(range(1, n + 1))

    for _ in range(n - 1):
        cards.remove(int(input()))

    print(cards[0])
except Exception as e:
    print(e)