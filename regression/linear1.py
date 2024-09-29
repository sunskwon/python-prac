from sklearn.datasets import make_regression

# 랜덤 데이터 셋 생성
# n_samples: 데이터 갯수
# n_features: 독립변수의 수
# n_target: 종속변수의 수
# bias: y절편
# noise: 분포
# random_state: 시드???
data = make_regression(n_samples = 1000, n_features = 1, bias = 1000, noise = 50, random_state = 333)

x_data = data[0]
y_data = data[1]

# python 데이터 조작 및 분석을 위한 라이브러리
import pandas as pd

random_df = pd.DataFrame()
random_df['x_data'] = x_data.flatten()
random_df['y_data'] = y_data

# print(random_df.head()): 첫 5개의 케이스 출력

# python 프로그래밍 언어 및 수학적 확장 NumPy 라이브러리를 활용한 플로팅 라이브러리
from matplotlib import pyplot as plt

plt.scatter(data[0], data[1])
# plt.show()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.2, shuffle = True)

from sklearn.linear_model import LinearRegression

hypothesis = LinearRegression()

# linear regression model에 train data 입력
model_linear = hypothesis.fit(x_train, y_train)

# print(f"weight: {model_linear.coef_}")
# print(f"bias: {model_linear.intercept_}")

# 시각화 도구?
import seaborn as sns

sns.regplot(x=x_train, y=y_train)

plt.title('regression plot (train)')
plt.xlabel('x_train')
plt.ylabel('y_label')
# plt.show()

sns.regplot(x=x_test, y=y_test)
plt.title('regression plot (test)')
plt.xlabel('x_test')
plt.ylabel('y_test')
# plt.show()

print(f"train data score: {model_linear.score(x_train, y_train):.2f}")
print(f"test data score: {model_linear.score(x_test, y_test):.2f}")

y_predict = model_linear.predict(x_test)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_predict)

import numpy as np

rmse = np.sqrt(mse)

print(f"mse: {mse:.3f}, rmse: {rmse:.3f}")

from sklearn.metrics import r2_score

print(f"r2: {r2_score(y_test, y_predict):.2f}")