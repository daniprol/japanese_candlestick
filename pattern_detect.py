import talib
import yfinance as yf

symbol = "SPY"
data = yf.download(symbol, start="2021-01-01", end="2021-05-01")

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]
morningstar_days = data[data['Morning Star'] != 0]

print('-'*24)
print('Morning Start Indicator for {}'.format(symbol))
print('-'*24)
print(morningstar_days)
print('-'*24)
print('Engulfing Indicator for {}'.format(symbol))
print('-'*24)
print(engulfing_days)
