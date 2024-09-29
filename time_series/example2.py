import pandas as pd
from autots import AutoTS

date_rng = pd.date_range(start='1/1/2018', end='1/08/2018', freq='H')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = pd.Series(range(len(df)))

model = AutoTS(forecast_length=3, frequency='infer', ensemble='simple')
model = model.fit(df, date_col='date', value_col='data', id_col=None)

prediction = model.predict()
forecast = prediction.forecast
print(f"forecast: {forecast}")