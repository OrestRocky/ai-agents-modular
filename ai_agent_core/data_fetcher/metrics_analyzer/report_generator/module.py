def fetch_market_data():
    """
    Псевдо-функція, яка імітує отримання ринкових даних з криптобіржі.
    Пізніше тут буде реальний API-запит (наприклад, до Binance).
    """
    sample_data = {
        "BTC": {
            "price": 64800,
            "volume": 238401,
            "change_24h": -0.7
        },
        "ETH": {
            "price": 3350,
            "volume": 193284,
            "change_24h": +1.2
        }
    }
    return sample_data
