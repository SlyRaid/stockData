import data_download as dd
import data_plotting as dplt
import calculation as clc


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), "
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
          "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")

    date_start = input("Введите дату начала периода в формате YYYY-MM-DD (для периода по умолчанию, "
                           "нажмите Enter): ")
    date_end = input("Введите дату окончания периода в формате YYYY-MM-DD (для текущей даты или периода "
                             "по умолчанию, нажмите Enter): ")

    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    stock_data = dd.fetch_stock_data(ticker.upper(), period, date_start, date_end)

    threshold = float(input("Введите порог для уведомления: "))

    stock_data = dd.add_moving_average(stock_data)

    dd.rsi(stock_data)

    dplt.create_and_save_plot(stock_data, ticker, period)

    clc.calculate_and_display_average_price(stock_data)

    clc.notify_if_strong_fluctuations(stock_data, threshold)

    save_to_csv = input("Хотите сохранить данные? y/N: ")
    if save_to_csv == 'y':
        filename = input("Введите название файла: ")
        try:
            stock_data.to_csv(f'{filename}.csv', index=False)
        except Exception as e:
            print(f'Не удалось экспортировать данные в CSV. Ошибка: {e}')


if __name__ == "__main__":
    main()
