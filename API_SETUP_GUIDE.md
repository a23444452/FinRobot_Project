# FinRobot API 設定指南

## 必要 API：選擇一個 AI Provider

### 選項 1: Google Gemini API（推薦，更便宜）

- **註冊網址**: https://aistudio.google.com/
- **取得 API Key**: https://aistudio.google.com/app/apikey
- **模型**: Gemini 2.0 Flash
- **定價**:
  - Input: $0.075/1M tokens (GPT-4 的 1/400)
  - Output: $0.30/1M tokens (GPT-4 的 1/200)
  - 免費額度: 每分鐘 15 RPM, 每天 1500 RPD
- **優勢**: 成本極低，速度快，免費額度充足

**設定步驟:**
1. 前往 Google AI Studio (https://aistudio.google.com/)
2. 使用 Google 帳號登入
3. 點擊「Get API Key」
4. 複製 API 金鑰
5. 貼到 `.env` 檔案的 `GEMINI_API_KEY`

### 選項 2: OpenAI API

- **註冊網址**: https://platform.openai.com/signup
- **取得 API Key**: https://platform.openai.com/api-keys
- **定價**: GPT-4: $0.03/1K tokens (input), $0.06/1K tokens (output)
- **建議**: 設定使用限額避免超支

**設定步驟:**
1. 註冊 OpenAI 帳號
2. 進入 API Keys 頁面
3. 點擊「Create new secret key」
4. 複製金鑰（只顯示一次！）
5. 貼到 `.env` 檔案的 `OPENAI_API_KEY`

---

## 選用 API：金融數據源

### 2. Finnhub (即時市場數據)
- **註冊網址**: https://finnhub.io/register
- **免費額度**: 60 calls/minute
- **功能**: 即時股價、新聞、市場數據

**設定步驟:**
1. 註冊免費帳號
2. Dashboard 中找到 API Key
3. 貼到 `.env` 的 `FINNHUB_API_KEY`

### 3. Financial Modeling Prep (財報數據)
- **註冊網址**: https://site.financialmodelingprep.com/developer
- **免費額度**: 250 calls/day
- **功能**: 財務報表、估值、同業比較

**設定步驟:**
1. 註冊免費帳號
2. Dashboard 取得 API Key
3. 貼到 `.env` 的 `FMP_API_KEY`

### 4. SEC API (公司申報文件)
- **註冊網址**: https://sec-api.io/
- **免費額度**: 10 calls/minute
- **功能**: 10-K、10-Q、8-K 等 SEC 文件

**設定步驟:**
1. 註冊免費帳號
2. 取得 API Key
3. 貼到 `.env` 的 `SEC_API_KEY`

---

## 設定 .env 檔案

複製範例檔案並填入你的金鑰：

```bash
cp .env.example .env
```

編輯 `.env` 檔案：

```bash
# AI Provider (選一個)
GEMINI_API_KEY=xxxxxxxxxxxxx        # 推薦：更便宜
# OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx  # 或使用 OpenAI

# Optional (可以先不填，用到再設定)
FINNHUB_API_KEY=xxxxxxxxxxxxx
FMP_API_KEY=xxxxxxxxxxxxx
SEC_API_KEY=xxxxxxxxxxxxx
```

**重要**: `.env` 檔案已加入 `.gitignore`，不會被提交到 git。

---

## 功能與 API 對照

| 功能 | 需要的 API |
|------|-----------|
| 基本股價分析 | Gemini/OpenAI + YFinance（免費）|
| 即時市場數據 | Gemini/OpenAI + Finnhub |
| 財務報表分析 | Gemini/OpenAI + FMP |
| SEC 文件分析 | Gemini/OpenAI + SEC API |
| 完整功能 | 所有 API |

---

## 成本估算（每月）

### 方案 A：使用 Gemini（推薦）
- **最小配置**:
  - Gemini: ~$0-2（免費額度通常夠用）
  - YFinance: $0
  - **總計: $0-2/月** ⭐

- **完整配置**:
  - Gemini: ~$2-5
  - Finnhub: $0（免費 60 calls/min）
  - FMP: $0（免費 250 calls/day）
  - SEC API: $0（免費 10 calls/min）
  - **總計: $2-5/月** ⭐

### 方案 B：使用 OpenAI
- **最小配置**:
  - OpenAI: ~$5-10
  - YFinance: $0
  - **總計: $5-10/月**

- **完整配置**:
  - OpenAI: ~$10-20
  - Finnhub: $0（免費 60 calls/min）
  - FMP: $0（免費 250 calls/day）
  - SEC API: $0（免費 10 calls/min）
  - **總計: $10-20/月**

---

## 驗證 API 設定

執行測試腳本檢查 API 是否正確設定：

```bash
uv run python test_api.py
```
