def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f'Средняя цена: {average_price:.2f} USD')


def notify_if_strong_fluctuations(data, threshold: float):
    max_price = data['Close'].max()
    min_price = data['Close'].min()

    percent_change = ((max_price - min_price) / min_price) * 100

    if percent_change > threshold:
        print(f'Произошли сильные колебания по цене {percent_change:.2f}%. '
              f'Максимальная цена: {max_price:.2f} USD. Минимальная цена: {min_price:.2f} USD.')