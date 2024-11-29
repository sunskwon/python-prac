# 학생의 번호와 수학, 정보 점수를 가진 데이터가 있다.

# 우리는 이를 정렬하려고 한다.

# 정렬 기준은 수학점수가 높은 순으로 정렬하되, 수학점수가 같으면 정보점수가 높은 순, 정보점수도 같으면 번호가 빠른 순서로 정렬하려고 한다.

try:
    n = int(input())    
    scores = []

    for _ in range(n):
        num = input().split()
        score = list(int(i) for i in num)
        scores.append(score)
    
    scores = sorted(scores, reverse=True)
    
    for i in range(len(scores)):
        print(i + 1, scores[i][0], scores[i][1])
except Exception as e:
    print(e)