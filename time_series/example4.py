import numpy as np
from darts import TimeSeries
from darts.models import ExponentialSmoothing

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = TimeSeries.from_values(values=np.array(data))

model = ExponentialSmoothing(seasonal=None)
model.fit(series)

prediction = model.predict(n=3)

print(prediction.values())