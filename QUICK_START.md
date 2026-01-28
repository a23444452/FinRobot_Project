# FinRobot 快速開始指南

## 🎯 立即可用（無需 API）

```bash
cd ~/finrobot-project
uv run python example_basic.py
```

這會：
- 分析 Apple (AAPL) 股票
- 比較 5 家科技公司
- 完全免費，使用 YFinance

---

## 📋 下一步：設定 API 金鑰

### 方案 A：使用 Gemini API（推薦，更便宜）⭐

只需 Google Gemini API，即可使用 AI 分析功能。成本約為 OpenAI 的 1/200！

1. **註冊 Google AI Studio**: https://aistudio.google.com/
2. **取得 API Key**: https://aistudio.google.com/app/apikey
3. **設定環境變數**:

```bash
cd ~/finrobot-project
cp .env.example .env
# 編輯 .env，填入 GEMINI_API_KEY
```

4. **測試設定**:

```bash
uv run python test_api.py
```

5. **執行 Gemini 範例**:

```bash
uv run python example_gemini.py
```

### 方案 B：使用 OpenAI API

1. **註冊 OpenAI**: https://platform.openai.com/signup
2. **取得 API Key**: https://platform.openai.com/api-keys
3. **設定環境變數**:

```bash
cd ~/finrobot-project
cp .env.example .env
# 編輯 .env，填入 OPENAI_API_KEY
```

4. **測試設定**:

```bash
uv run python test_api.py
```

---

## 🚀 完整功能（所有免費 API）

參閱 `API_SETUP_GUIDE.md` 設定：

1. **Finnhub** (即時數據) - 免費 60 calls/min
2. **FMP** (財報數據) - 免費 250 calls/day
3. **SEC API** (申報文件) - 免費 10 calls/min

---

## 💡 範例腳本

### 終端機執行

```bash
# 基本股票分析（免費，無需 API）
uv run python example_basic.py

# 使用 Gemini AI 分析（推薦）
uv run python example_gemini.py

# API 測試
uv run python test_api.py

# 使用執行腳本（支援自訂股票代號）
cd ~/finrobot-project
./run_analysis.sh AAPL analyze          # 分析 Apple
./run_analysis.sh AAPL,MSFT compare     # 比較兩支股票
```

### 📱 手機執行

**iOS 捷徑**（最簡單）：
1. 查看 `IOS_SHORTCUT_GUIDE.md` 詳細教學
2. 快速參考 `QUICK_REFERENCE.md`

**其他方案**：
- 查看 `MOBILE_TRIGGER_GUIDE.md` 了解 Telegram Bot、API 等方案

---

## 📊 可分析的內容

### 目前可用（YFinance）
- ✅ 股價歷史數據
- ✅ 公司基本資訊
- ✅ 估值指標（P/E、P/B）
- ✅ 多股票比較

### 需要 Gemini 或 OpenAI API
- 🤖 AI 市場預測
- 🤖 智能投資建議
- 🤖 風險分析
- 🤖 多股票比較分析

### 需要完整 API
- 📈 即時市場數據
- 📊 深度財報分析
- 📄 SEC 文件解析
- 📝 自動生成研究報告

---

## ⚠️ 成本提醒

| 配置 | 月費 | 功能 |
|------|------|------|
| 只用 YFinance | $0 | 基本分析 |
| + Gemini API | ~$0-2 | AI 分析（推薦）⭐ |
| + OpenAI API | ~$10 | AI 分析 |
| Gemini + 所有免費 API | ~$2-5 | 完整功能（推薦）⭐ |
| OpenAI + 所有免費 API | ~$15 | 完整功能 |

---

## 🆘 遇到問題？

1. **API 錯誤**：執行 `uv run python test_api.py` 檢查設定
2. **套件問題**：執行 `uv sync` 重新同步
3. **Python 版本**：本專案使用 Python 3.12

---

## 📚 完整文件

| 文件 | 說明 |
|------|------|
| `README.md` | 專案總覽 |
| `QUICK_START.md` | 快速開始（本文件）|
| `API_SETUP_GUIDE.md` | API 詳細設定 |
| `EMAIL_SETUP_GUIDE.md` | 郵件通知設定 |
| `TELEGRAM_BOT_SETUP.md` | Telegram Bot 設定（推薦）⭐ |
| `MOBILE_TRIGGER_GUIDE.md` | 手機觸發方案（4 種）|
| `IOS_SHORTCUT_GUIDE.md` | iOS 捷徑教學 |
| `QUICK_REFERENCE.md` | 快速參考 |
| `GEMINI_INTEGRATION.md` | Gemini 整合說明 |
| `DOCUMENTATION_INDEX.md` | 文件導覽索引 |

## 🔗 外部資源

- **官方文件**: https://finrobot.ai
- **GitHub**: https://github.com/AI4Finance-Foundation/FinRobot
