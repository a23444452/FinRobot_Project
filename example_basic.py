"""
FinRobot 基本範例：使用 YFinance 進行股票分析
不需要付費 API，適合初學者測試
"""

import yfinance as yf
from datetime import datetime, timedelta

def analyze_stock(ticker_symbol):
    """分析股票基本資訊"""

    print(f"\n{'='*60}")
    print(f"股票分析: {ticker_symbol}")
    print(f"{'='*60}\n")

    # 取得股票資料
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    # 基本資訊
    print("📊 基本資訊:")
    print(f"  公司名稱: {info.get('longName', 'N/A')}")
    print(f"  產業: {info.get('industry', 'N/A')}")
    print(f"  部門: {info.get('sector', 'N/A')}")
    print()

    # 價格資訊
    print("💰 價格資訊:")
    print(f"  目前價格: ${info.get('currentPrice', 'N/A')}")
    print(f"  52週最高: ${info.get('fiftyTwoWeekHigh', 'N/A')}")
    print(f"  52週最低: ${info.get('fiftyTwoWeekLow', 'N/A')}")
    print(f"  市值: ${info.get('marketCap', 0):,.0f}")
    print()

    # 估值指標
    print("📈 估值指標:")
    print(f"  本益比 (P/E): {info.get('trailingPE', 'N/A')}")
    print(f"  股價淨值比 (P/B): {info.get('priceToBook', 'N/A')}")
    print(f"  殖利率: {info.get('dividendYield', 0) * 100:.2f}%")
    print()

    # 歷史數據（近30天）
    print("📉 近30天價格走勢:")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    hist = ticker.history(start=start_date, end=end_date)

    if not hist.empty:
        print(f"  開始價格: ${hist['Close'].iloc[0]:.2f}")
        print(f"  結束價格: ${hist['Close'].iloc[-1]:.2f}")
        change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
        print(f"  變化: {change:+.2f}%")

    print(f"\n{'='*60}\n")

def compare_stocks(tickers):
    """比較多個股票"""

    print(f"\n{'='*60}")
    print(f"股票比較: {', '.join(tickers)}")
    print(f"{'='*60}\n")

    results = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        results.append({
            'ticker': ticker,
            'name': info.get('longName', 'N/A'),
            'price': info.get('currentPrice', 0),
            'pe': info.get('trailingPE', 0),
            'marketCap': info.get('marketCap', 0)
        })

    print(f"{'股票代號':<10} {'公司名稱':<30} {'價格':<12} {'P/E':<10} {'市值':<15}")
    print("-" * 80)

    for r in results:
        print(f"{r['ticker']:<10} {r['name']:<30} ${r['price']:<11.2f} {r['pe']:<10.2f} ${r['marketCap']:>13,.0f}")

    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    # 範例 1: 單一股票分析
    analyze_stock("AAPL")  # Apple

    # 範例 2: 比較科技股
    compare_stocks(["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"])
