import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.DataFrame({
    'ds': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'y': [10, 11, 9, 12]
})
df['ds'] = pd.to_datetime(df['ds'])

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=365)

forecast = model.predict(future)

fig = model.plot(forecast)
plt.show()

predictions = forecast[forecast['ds'].isin(df['ds'])]['yhat']
actuals = df['y']

mae = mean_absolute_error(actuals, predictions)
mse = mean_squared_error(actuals, predictions)
rmse = mean_squared_error(actuals, predictions, squared=False)
mape = np.mean(np.abs((actuals - predictions) / actuals)) * 100

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")