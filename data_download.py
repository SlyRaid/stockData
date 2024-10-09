import yfinance as yf


def fetch_stock_data(ticker, period, date_start=None, date_end=None):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    if date_start is None:
        return data
    else:
        data = stock.history(start=date_start, end=date_end)
        return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def rsi(data, periods=14, ema=True):
    close_delta = data['Close'].diff()

    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema == True:
        ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    else:
        ma_up = up.rolling(window=periods, adjust=False).mean()
        ma_down = down.rolling(window=periods, adjust=False).mean()

    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))

    data['RSI'] = rsi
