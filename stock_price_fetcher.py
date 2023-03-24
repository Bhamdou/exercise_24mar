import requests

def get_stock_data(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()
    return data["Global Quote"]

def main():
    api_key = "GKMFQAGDF949HM2A"  # Replace with your actual API key
    stock_symbol = input("Enter the stock symbol (e.g., MSFT for Microsoft): ").upper()

    try:
        stock_data = get_stock_data(stock_symbol, api_key)
        print(f"Stock Symbol: {stock_data['01. symbol']}")
        print(f"Latest Trading Day: {stock_data['07. latest trading day']}")
        print(f"Previous Close: {stock_data['08. previous close']}")
        print(f"Change: {stock_data['09. change']}")
        print(f"Change Percent: {stock_data['10. change percent']}")
    except Exception as e:
        print("Error fetching stock data:", e)

if __name__ == "__main__":
    main()
