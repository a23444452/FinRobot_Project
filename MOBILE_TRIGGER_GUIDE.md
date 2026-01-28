# 📱 手機觸發執行指南

使用手機 App 觸發 FinRobot 股票分析，並自動收到郵件報告。

---

## 🎯 方案比較

| 方案 | 難度 | 成本 | 優點 | 缺點 |
|------|------|------|------|------|
| **1. iOS 捷徑 + SSH** | ⭐⭐ | 免費 | 簡單快速、原生整合 | 需要電腦保持開機 |
| **2. Telegram Bot** | ⭐⭐⭐ | 免費 | 跨平台、即時互動 | 需要設定 Bot |
| **3. FastAPI + Railway** | ⭐⭐⭐⭐ | $5/月 | 完全雲端、隨時使用 | 需要部署維護 |
| **4. GitHub Actions** | ⭐⭐⭐ | 免費 | 雲端執行、版本控制 | 手動觸發較慢 |

---

## 方案 1: iOS 捷徑 + SSH（推薦初學者）⭐

最簡單的方案，使用 iPhone/iPad 內建的「捷徑」App。

### 前置需求

1. **Mac 電腦**（保持開機或休眠喚醒）
2. **iPhone/iPad**（iOS 13+）
3. **同一 WiFi 網路**（或設定遠端 SSH）

### 步驟 1: 在 Mac 上啟用遠端登入

1. 開啟「系統偏好設定」→「共享」
2. 勾選「遠端登入」
3. 記下你的使用者名稱和 Mac 的 IP 位址

### 步驟 2: 使用執行腳本

專案已包含 `run_analysis.sh` 腳本，支援自訂股票代號：

```bash
# 腳本已存在於專案中
~/finrobot-project/run_analysis.sh

# 使用方式：
~/finrobot-project/run_analysis.sh TICKER ACTION
# TICKER: 股票代號（例如：AAPL）
# ACTION: analyze（分析）或 compare（比較）
```

測試執行：
```bash
# 分析單一股票
~/finrobot-project/run_analysis.sh AAPL analyze

# 比較多支股票（用逗號分隔）
~/finrobot-project/run_analysis.sh AAPL,MSFT,GOOGL compare
```

查看日誌：
```bash
tail ~/finrobot-logs.txt
```

### 步驟 3: 建立 iOS 捷徑

1. 開啟 iPhone 的「捷徑」App
2. 點擊「+」建立新捷徑
3. 搜尋並加入「透過 SSH 執行指令」
4. 設定：
   - **主機**: 你的 Mac IP（例如 192.168.1.100）
   - **使用者**: 你的 Mac 使用者名稱
   - **密碼**: 你的 Mac 登入密碼
   - **指令**: `~/finrobot-project/run_analysis.sh AAPL analyze`
5. 命名為「📊 股票分析」

**進階**: 使用變數讓使用者輸入股票代號
- 加入「詢問輸入」動作
- 指令改為: `~/finrobot-project/run_analysis.sh [變數:股票代號] analyze`

### 步驟 4: 加入到主畫面

1. 長按捷徑 → 「詳細資訊」
2. 「加入主畫面」
3. 自訂圖示與名稱

現在你可以一鍵執行分析！📱

**詳細的 iOS 捷徑設定請參考**: `IOS_SHORTCUT_GUIDE.md`

---

## 方案 2: Telegram Bot（推薦進階使用者）⭐⭐⭐

建立一個 Telegram Bot，透過聊天訊息觸發分析。

### 優點

- ✅ 跨平台（iOS、Android、桌面版）
- ✅ 即時互動、支援多種指令
- ✅ 可以發送分析結果到 Telegram
- ✅ 不需要電腦保持開機（如果部署到雲端）

### 實作步驟

#### 步驟 1: 建立 Telegram Bot

1. 在 Telegram 搜尋 `@BotFather`
2. 傳送 `/newbot` 建立新 Bot
3. 設定名稱（例如：FinRobot Stock Analyzer）
4. 記下 **Bot Token**（例如：`123456:ABC-DEF...`）

#### 步驟 2: 安裝套件

```bash
cd ~/finrobot-project
uv add python-telegram-bot
```

#### 步驟 3: 建立 Bot 程式

建立 `telegram_bot.py`：

```python
"""
Telegram Bot for FinRobot
使用 /analyze AAPL 指令觸發分析
"""

import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from example_gemini import analyze_with_gemini, compare_stocks_with_gemini
from email_service import EmailService

load_dotenv()

# 設定
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = os.getenv("TELEGRAM_ALLOWED_USERS", "").split(",")  # 限制使用者

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """歡迎訊息"""
    await update.message.reply_text(
        "📊 FinRobot 股票分析 Bot\n\n"
        "指令:\n"
        "/analyze AAPL - 分析單一股票\n"
        "/compare AAPL MSFT GOOGL - 比較多支股票\n"
        "/help - 顯示說明"
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """分析單一股票"""
    # 檢查權限
    user_id = str(update.effective_user.id)
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ 未授權使用")
        return
    
    # 檢查參數
    if not context.args:
        await update.message.reply_text("請提供股票代號，例如: /analyze AAPL")
        return
    
    ticker = context.args[0].upper()
    
    # 發送處理中訊息
    msg = await update.message.reply_text(f"🔍 正在分析 {ticker}...")
    
    try:
        # 執行分析（會自動發送郵件）
        analyze_with_gemini(ticker)
        
        await msg.edit_text(
            f"✅ {ticker} 分析完成！\n"
            f"📧 報告已發送到你的郵箱"
        )
    except Exception as e:
        await msg.edit_text(f"❌ 分析失敗: {str(e)}")

async def compare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """比較多支股票"""
    user_id = str(update.effective_user.id)
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ 未授權使用")
        return
    
    if len(context.args) < 2:
        await update.message.reply_text(
            "請提供至少 2 支股票代號\n"
            "例如: /compare AAPL MSFT GOOGL"
        )
        return
    
    tickers = [t.upper() for t in context.args]
    
    msg = await update.message.reply_text(f"🔍 正在比較 {', '.join(tickers)}...")
    
    try:
        compare_stocks_with_gemini(tickers)
        
        await msg.edit_text(
            f"✅ 比較分析完成！\n"
            f"📊 股票: {', '.join(tickers)}\n"
            f"📧 報告已發送到你的郵箱"
        )
    except Exception as e:
        await msg.edit_text(f"❌ 分析失敗: {str(e)}")

def main():
    """啟動 Bot"""
    if not BOT_TOKEN:
        print("❌ 請在 .env 設定 TELEGRAM_BOT_TOKEN")
        return
    
    # 建立 Application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # 註冊指令
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("compare", compare))
    
    # 啟動 Bot
    print("🤖 Telegram Bot 已啟動...")
    app.run_polling()

if __name__ == "__main__":
    main()
```

#### 步驟 4: 設定環境變數

在 `.env` 加入：

```bash
# Telegram Bot
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...
TELEGRAM_ALLOWED_USERS=your_telegram_user_id  # 可選，限制使用者
```

取得你的 User ID：傳送訊息給 `@userinfobot`

#### 步驟 5: 執行 Bot

```bash
uv run python telegram_bot.py
```

保持終端機執行，或使用 `tmux` / `screen` 在背景執行。

#### 使用方式

在 Telegram 中：
- `/analyze AAPL` - 分析 Apple
- `/compare AAPL MSFT GOOGL` - 比較三支股票

分析完成後會收到通知，同時郵件報告也會寄到信箱！

---

## 方案 3: FastAPI + Railway 部署（推薦專業使用者）⭐⭐⭐⭐

建立一個 Web API，部署到雲端，隨時隨地使用。

### 優點

- ✅ 完全雲端，不需要本機電腦
- ✅ 提供 Web 介面和 API
- ✅ 可整合到其他 App（iOS Shortcuts、IFTTT）
- ✅ 支援排程自動執行

### 實作步驟

#### 步驟 1: 建立 FastAPI 應用

安裝套件：
```bash
uv add fastapi uvicorn
```

建立 `api.py`：

```python
"""
FinRobot FastAPI
提供 HTTP API 供手機 App 呼叫
"""

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from example_gemini import analyze_with_gemini, compare_stocks_with_gemini

load_dotenv()

app = FastAPI(title="FinRobot API", version="1.0.0")

# API Key 驗證（安全性）
API_KEY = os.getenv("API_KEY", "your-secret-api-key")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return True

class AnalyzeRequest(BaseModel):
    ticker: str
    
class CompareRequest(BaseModel):
    tickers: List[str]

@app.get("/")
async def root():
    return {
        "message": "FinRobot API",
        "version": "1.0.0",
        "endpoints": {
            "POST /analyze": "分析單一股票",
            "POST /compare": "比較多支股票"
        }
    }

@app.post("/analyze")
async def analyze(
    request: AnalyzeRequest,
    authenticated: bool = Depends(verify_api_key)
):
    """分析單一股票"""
    try:
        analyze_with_gemini(request.ticker)
        return {
            "status": "success",
            "ticker": request.ticker,
            "message": "分析完成，報告已發送到郵箱"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare")
async def compare(
    request: CompareRequest,
    authenticated: bool = Depends(verify_api_key)
):
    """比較多支股票"""
    if len(request.tickers) < 2:
        raise HTTPException(status_code=400, detail="至少需要 2 支股票")
    
    try:
        compare_stocks_with_gemini(request.tickers)
        return {
            "status": "success",
            "tickers": request.tickers,
            "message": "比較分析完成，報告已發送到郵箱"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 步驟 2: 本機測試

```bash
uv run python api.py
```

開啟瀏覽器: http://localhost:8000/docs

#### 步驟 3: 部署到 Railway

1. 註冊 Railway: https://railway.app/
2. 連結 GitHub repository
3. 新增專案 → 選擇你的 repository
4. 設定環境變數（在 Railway Dashboard）:
   ```
   GEMINI_API_KEY=your_key
   ENABLE_EMAIL=true
   EMAIL_SENDER=...
   API_KEY=your-secret-api-key
   ```
5. Railway 會自動部署

#### 步驟 4: 使用 iOS 捷徑呼叫 API

在 iPhone 捷徑中：

1. 加入「取得 URL 內容」
2. 設定：
   - **URL**: `https://your-app.railway.app/analyze`
   - **方法**: POST
   - **標頭**:
     - `Content-Type`: `application/json`
     - `X-API-Key`: `your-secret-api-key`
   - **本文**: JSON
     ```json
     {"ticker": "AAPL"}
     ```

---

## 方案 4: GitHub Actions 手動觸發

簡單但功能有限的雲端方案。

### 實作步驟

建立 `.github/workflows/analyze.yml`：

```yaml
name: Stock Analysis

on:
  workflow_dispatch:
    inputs:
      ticker:
        description: '股票代號 (例如: AAPL)'
        required: true
        default: 'AAPL'
      action:
        description: '動作類型'
        required: true
        type: choice
        options:
          - analyze
          - compare

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      
      - name: Install uv
        run: pip install uv
      
      - name: Install dependencies
        run: uv sync
      
      - name: Run analysis
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          ENABLE_EMAIL: true
          EMAIL_SENDER: ${{ secrets.EMAIL_SENDER }}
          EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
          EMAIL_RECEIVER: ${{ secrets.EMAIL_RECEIVER }}
        run: |
          uv run python -c "from example_gemini import analyze_with_gemini; analyze_with_gemini('${{ inputs.ticker }}')"
```

在 GitHub 手機 App 中：
1. 前往 Actions 頁面
2. 選擇 "Stock Analysis"
3. 點擊 "Run workflow"
4. 輸入股票代號
5. 執行

---

## 📊 方案選擇建議

### 我該選哪個？

| 使用情境 | 推薦方案 |
|---------|---------|
| 只有 iPhone，Mac 常開機 | 方案 1: iOS 捷徑 + SSH |
| 需要跨平台，喜歡聊天介面 | 方案 2: Telegram Bot |
| 需要隨時隨地使用，預算充足 | 方案 3: FastAPI + Railway |
| 不想花錢，可接受手動觸發 | 方案 4: GitHub Actions |

### 組合使用

可以同時實作多個方案：
- **日常**: 用 iOS 捷徑快速分析
- **外出**: 用 Telegram Bot 遠端觸發
- **自動化**: 用 GitHub Actions 定時執行

---

## 🔒 安全性提醒

1. **API Key 保護**
   - 不要將 API Key 寫死在程式碼中
   - 使用環境變數或 Secrets 管理

2. **限制存取**
   - Telegram Bot: 限制 User ID
   - FastAPI: 使用 API Key 驗證
   - SSH: 使用金鑰認證而非密碼

3. **成本控制**
   - 設定 Gemini API 使用限額
   - 監控郵件發送數量

---

需要更詳細的實作教學嗎？我可以幫你建立完整的範例程式碼！
