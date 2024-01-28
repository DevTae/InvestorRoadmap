# pip install yahoo_fin

from yahoo_fin import stock_info


def get_nasdaq_tickers():
    # 나스닥 지수의 구성 종목을 가져옴
    nasdaq_tickers = stock_info.tickers_nasdaq()

    return nasdaq_tickers


if __name__ == "__main__":
    nasdaq_tickers = get_nasdaq_tickers()
    print(nasdaq_tickers)

# 이후 시가총액 조회
