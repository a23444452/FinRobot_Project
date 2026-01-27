"""
FinRobot API 測試腳本
檢查所有 API 金鑰是否正確設定
"""

import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

def test_api_keys():
    """測試 API 金鑰設定"""

    print("=" * 60)
    print("FinRobot API 金鑰檢查")
    print("=" * 60)
    print()

    # 檢查 AI Provider（至少需要一個）
    gemini_key = os.getenv("GEMINI_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    has_ai_provider = False

    if gemini_key and len(gemini_key) > 10:
        print("✅ Gemini API Key: 已設定（推薦）")
        has_ai_provider = True
    else:
        print("⚠️  Gemini API Key: 未設定")
        print("   請到 https://aistudio.google.com/app/apikey 取得")

    if openai_key and openai_key.startswith("sk-"):
        print("✅ OpenAI API Key: 已設定")
        has_ai_provider = True
    else:
        print("⚠️  OpenAI API Key: 未設定")
        print("   請到 https://platform.openai.com/api-keys 取得")

    print()

    if not has_ai_provider:
        print("❌ 錯誤: 至少需要設定 Gemini 或 OpenAI 其中一個 API")
        print("   建議使用 Gemini（更便宜且有免費額度）")
        print()

    print()
    print("選用 API（可稍後設定）:")
    print("-" * 60)

    # 檢查選用的 API
    finnhub_key = os.getenv("FINNHUB_API_KEY")
    if finnhub_key and len(finnhub_key) > 10:
        print("✅ Finnhub API Key: 已設定")
    else:
        print("⚠️  Finnhub API Key: 未設定（選用）")

    fmp_key = os.getenv("FMP_API_KEY")
    if fmp_key and len(fmp_key) > 10:
        print("✅ FMP API Key: 已設定")
    else:
        print("⚠️  FMP API Key: 未設定（選用）")

    sec_key = os.getenv("SEC_API_KEY")
    if sec_key and len(sec_key) > 10:
        print("✅ SEC API Key: 已設定")
    else:
        print("⚠️  SEC API Key: 未設定（選用）")

    print()
    print("=" * 60)
    print()

    # 測試 YFinance（不需要 API）
    print("測試 YFinance（免費，無需 API）...")
    try:
        import yfinance as yf
        ticker = yf.Ticker("AAPL")
        info = ticker.info
        print(f"✅ YFinance 運作正常")
        print(f"   範例: Apple (AAPL) 目前價格約 ${info.get('currentPrice', 'N/A')}")
    except Exception as e:
        print(f"❌ YFinance 測試失敗: {e}")

    print()
    print("=" * 60)

if __name__ == "__main__":
    test_api_keys()
