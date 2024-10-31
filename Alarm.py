import os
import time
import pandas_datareader as web
from terminal_notifier import Notification, audio

import pandas_datareader as web
tickers = ["AAPL", "FB", "NVDA"]
upper_limits = [160.4, 220, 240]
lower_limits = [160.2, 130, 140]

while True:
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)  # To verify prices are fetched correctly
    time.sleep(1)

    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id="NeuralNine Stock Alarm Bot",
                                 title="Price Alert For " + tickers[i],
                                 message=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to sell.",
                                 duration="long")
            
            toast.add_actions(label="Go to Stockbroker", launch="https://www.google.com/")
            toast.set_audio(audio.LoopingAlarm6, loop=True)
            toast.show()

        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id="NeuralNine Stock Alarm Bot",
                                 title="Price Alert For " + tickers[i],
                                 message=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to buy.",
                                 duration="long")
            
            toast.add_actions(label="Go to Stockbroker", launch="https://www.google.com/")
            toast.set_audio(audio.LoopingAlarm8, loop=True)
            toast.show()

    time.sleep(1)
