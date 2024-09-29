import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

date_rng = pd.date_range(start='2020-01-01', end='2023-12-31', freq='ME')
np.random.seed(42)
data = np.random.randint(100, 200, size=len(date_rng))
ts = pd.Series(data, index=date_rng)

plt.figure(figsize=(10, 5))
plt.plot(ts)
plt.show()

adf_result = adfuller(ts)
print(f'ADF 통계량: {adf_result[0]}')
print(f'p-value: {adf_result[1]}')

model = ARIMA(ts, order=(1, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=12)
forecast_index = pd.date_range(start=ts.index[-1] + pd.DateOffset(1), periods=12, freq='ME')
forecast_series = pd.Series(forecast, index=forecast_index)

plt.figure(figsize=(10, 5))
plt.plot(ts, label='origin')
plt.plot(forecast_series, label='predict', color='red')
plt.show()
