stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

def average_closing_price(stock_symbol):
    average = "test"
    total = {}
    count = {}
    total.setdefault(stock_symbol, 0)
    count.setdefault(stock_symbol, 0)
    for stock, date, price in stock_data:
        stock.count(stock_symbol)
        if stock == stock_symbol:
            total[stock_symbol] += price
            count[stock_symbol] += 1
        if count[stock_symbol] != 0:
            average = total[stock_symbol] / count[stock_symbol]
    print(f"The average total of {stock_symbol} is {average}.")

average_closing_price("AAPL")