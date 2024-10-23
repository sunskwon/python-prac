# 5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.

a = []

for i in range(5):
    a.append(int(input()))

print(max(a))
print(min(a))