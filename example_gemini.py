"""
FinRobot 使用 Google Gemini API 進行股票分析
使用 Gemini 2.0 Flash 模型（成本極低，速度快）
"""

import os
import yfinance as yf
from datetime import datetime, timedelta
from dotenv import load_dotenv
import google.generativeai as genai

# 載入環境變數
load_dotenv()

# 設定 Gemini API
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    print("❌ 錯誤: 請先設定 GEMINI_API_KEY 在 .env 檔案中")
    print("   註冊: https://aistudio.google.com/")
    exit(1)

genai.configure(api_key=gemini_key)

# 使用 Gemini 2.0 Flash 模型
model = genai.GenerativeModel('gemini-2.0-flash-exp')

def get_stock_data(ticker_symbol):
    """取得股票基本資料"""
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    
    # 歷史數據（近30天）
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    hist = ticker.history(start=start_date, end=end_date)
    
    return {
        'ticker': ticker_symbol,
        'name': info.get('longName', 'N/A'),
        'sector': info.get('sector', 'N/A'),
        'industry': info.get('industry', 'N/A'),
        'currentPrice': info.get('currentPrice', 'N/A'),
        'marketCap': info.get('marketCap', 0),
        'pe_ratio': info.get('trailingPE', 'N/A'),
        'pb_ratio': info.get('priceToBook', 'N/A'),
        'dividend_yield': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
        'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 'N/A'),
        'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 'N/A'),
        'hist_start_price': float(hist['Close'].iloc[0]) if not hist.empty else 0,
        'hist_end_price': float(hist['Close'].iloc[-1]) if not hist.empty else 0,
        'price_change_pct': ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0] * 100) if not hist.empty else 0
    }

def analyze_with_gemini(ticker_symbol):
    """使用 Gemini AI 分析股票"""
    
    print(f"\n{'='*60}")
    print(f"🤖 使用 Gemini 2.0 Flash 分析: {ticker_symbol}")
    print(f"{'='*60}\n")
    
    # 取得股票數據
    print("📊 正在取得股票數據...")
    data = get_stock_data(ticker_symbol)
    
    # 顯示基本資訊
    print(f"\n基本資訊:")
    print(f"  公司: {data['name']}")
    print(f"  產業: {data['sector']} / {data['industry']}")
    print(f"  目前價格: ${data['currentPrice']}")
    print(f"  市值: ${data['marketCap']:,.0f}")
    print(f"  本益比: {data['pe_ratio']}")
    print(f"  近30天變化: {data['price_change_pct']:+.2f}%")
    
    # 建立 Gemini 分析提示
    prompt = f"""
你是一位專業的金融分析師。請根據以下股票數據提供簡潔的分析：

股票代號: {data['ticker']}
公司名稱: {data['name']}
產業: {data['sector']} / {data['industry']}
目前價格: ${data['currentPrice']}
市值: ${data['marketCap']:,.0f}
本益比 (P/E): {data['pe_ratio']}
股價淨值比 (P/B): {data['pb_ratio']}
殖利率: {data['dividend_yield']:.2f}%
52週最高: ${data['fiftyTwoWeekHigh']}
52週最低: ${data['fiftyTwoWeekLow']}
近30天變化: {data['price_change_pct']:+.2f}%

請提供：
1. 公司簡介（2-3句話）
2. 財務健康度評估（考慮 P/E、P/B、市值）
3. 近期表現分析（基於30天價格變化）
4. 投資建議（買入/持有/賣出，並說明理由）
5. 風險提示（1-2點）

請用繁體中文回答，保持專業且簡潔。
"""
    
    print("\n🤖 Gemini AI 正在分析...")
    print("-" * 60)
    
    try:
        # 呼叫 Gemini API
        response = model.generate_content(prompt)
        
        # 顯示 AI 分析結果
        print(response.text)
        
    except Exception as e:
        print(f"❌ Gemini API 錯誤: {e}")
        print("   請檢查 API Key 是否正確設定")
    
    print(f"\n{'='*60}\n")

def compare_stocks_with_gemini(tickers):
    """使用 Gemini AI 比較多支股票"""
    
    print(f"\n{'='*60}")
    print(f"🤖 使用 Gemini 2.0 Flash 比較股票")
    print(f"{'='*60}\n")
    
    # 取得所有股票數據
    print("📊 正在取得股票數據...")
    stocks_data = []
    for ticker in tickers:
        data = get_stock_data(ticker)
        stocks_data.append(data)
        print(f"  ✓ {ticker}: {data['name']}")
    
    # 建立比較表格
    print(f"\n{'股票':<8} {'價格':<12} {'P/E':<10} {'市值':<15} {'30天變化':<10}")
    print("-" * 60)
    for data in stocks_data:
        print(f"{data['ticker']:<8} ${data['currentPrice']:<11.2f} {data['pe_ratio']:<10.2f} ${data['marketCap']:>13,.0f} {data['price_change_pct']:>+9.2f}%")
    
    # 建立 Gemini 比較提示
    stocks_summary = "\n".join([
        f"{i+1}. {data['ticker']} ({data['name']}): "
        f"價格 ${data['currentPrice']}, P/E {data['pe_ratio']}, "
        f"市值 ${data['marketCap']:,.0f}, 30天變化 {data['price_change_pct']:+.2f}%"
        for i, data in enumerate(stocks_data)
    ])
    
    prompt = f"""
你是一位專業的投資顧問。請比較以下股票並提供投資建議：

{stocks_summary}

請提供：
1. 各股票的相對優勢與劣勢
2. 從估值角度（P/E ratio）的比較
3. 從成長性角度（30天表現）的比較
4. 投資組合建議（如何分配資金）
5. 整體市場風險評估

請用繁體中文回答，保持專業且實用。
"""
    
    print("\n🤖 Gemini AI 正在比較分析...")
    print("-" * 60)
    
    try:
        response = model.generate_content(prompt)
        print(response.text)
        
    except Exception as e:
        print(f"❌ Gemini API 錯誤: {e}")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    # 範例 1: 單一股票分析
    analyze_with_gemini("AAPL")  # Apple
    
    # 範例 2: 多股票比較
    compare_stocks_with_gemini(["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"])
    
    print("\n💡 提示:")
    print("  - Gemini 2.0 Flash 成本約為 GPT-4 的 1/200")
    print("  - 免費額度: 每分鐘 15 次請求, 每天 1500 次")
    print("  - 適合頻繁的金融分析任務")
