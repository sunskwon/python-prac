# 수호는 30분 전으로 돌아가고 싶은 1人 이다.

# 공백을 기준으로 시간과 분이 주어진다.

# 그러면 이 시간을 기준으로 30분전의 시간을 출력하시오.

# 예)

# 12 35  =====> 12 5

# 12 0 ======> 11 30

# 11 5 ======> 10 35

# 0 10 ======> 23 40

import datetime

time = input().split()

input_time = datetime.time(hour=int(time[0]), minute=int(time[1]))

answer = datetime.datetime.combine(datetime.date.today(), input_time) - datetime.timedelta(minutes=30)

print(answer.hour, answer.minute)