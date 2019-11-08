import requests
import time
import matplotlib.pyplot as plt
xValues = []
yValues = []
timeWait = 5
timeCount = 0
for x in range(0,11):
    yValues.append(float(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").json()["data"]["amount"]))
    xValues.append(timeCount);
    time.sleep(timeWait)
    timeCount = timeCount + timeWait
minimum = min(yValues)
maximum = max(yValues)
plt.plot(xValues, yValues)
plt.axis([0, timeCount - timeWait, minimum - 1, maximum + 1])
plt.ylabel('Bitcoin price')
plt.xlabel('Time')
plt.show()
