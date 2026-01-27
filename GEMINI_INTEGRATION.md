# Gemini API 整合指南

## 🎯 為什麼選擇 Gemini？

### 成本比較

| 模型 | Input 價格 | Output 價格 | 相對成本 |
|------|-----------|------------|---------|
| **Gemini 2.0 Flash** | $0.075/1M tokens | $0.30/1M tokens | 1x（最便宜）|
| GPT-4 | $30/1M tokens | $60/1M tokens | **400x 更貴** |

### 免費額度

Gemini API 提供慷慨的免費額度：
- **每分鐘**: 15 次請求 (RPM)
- **每天**: 1500 次請求 (RPD)
- **每分鐘 tokens**: 100 萬

對於個人金融分析使用，免費額度通常足夠！

---

## 🚀 快速開始

### 1. 取得 Gemini API Key

1. 前往 **Google AI Studio**: https://aistudio.google.com/
2. 使用 Google 帳號登入
3. 點擊左側選單的「Get API Key」
4. 點擊「Create API Key」
5. 複製產生的 API Key（格式類似: `AIzaSy...`）

### 2. 設定環境變數

```bash
cd ~/finrobot-project
cp .env.example .env
```

編輯 `.env` 檔案：

```bash
GEMINI_API_KEY=你的_Gemini_API_Key
```

### 3. 測試設定

```bash
uv run python test_api.py
```

應該會看到：
```
✅ Gemini API Key: 已設定（推薦）
✅ YFinance 運作正常
```

### 4. 執行 Gemini 範例

```bash
uv run python example_gemini.py
```

---

## 📊 功能展示

### 功能 1: 單一股票 AI 分析

```python
from example_gemini import analyze_with_gemini

analyze_with_gemini("AAPL")
```

**輸出內容**：
- 📊 基本資訊（價格、市值、P/E、P/B）
- 🤖 AI 分析：
  - 公司簡介
  - 財務健康度評估
  - 近期表現分析
  - 投資建議（買入/持有/賣出）
  - 風險提示

### 功能 2: 多股票比較分析

```python
from example_gemini import compare_stocks_with_gemini

compare_stocks_with_gemini(["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"])
```

**輸出內容**：
- 📊 比較表格（價格、P/E、市值、30天變化）
- 🤖 AI 比較分析：
  - 各股票相對優勢
  - 估值比較
  - 成長性比較
  - 投資組合建議
  - 風險評估

---

## 💰 實際成本估算

### 一次股票分析的 Token 使用量

- **輸入** (Prompt + 股票數據): ~500 tokens
- **輸出** (AI 分析): ~800 tokens

**單次成本**:
- Input: 500 tokens × $0.075/1M = $0.0000375
- Output: 800 tokens × $0.30/1M = $0.00024
- **總計**: ~$0.00028（約 0.009 台幣）

### 每月使用估算

假設每天分析 10 支股票：

| 使用量 | 每日成本 | 每月成本 |
|--------|---------|---------|
| 10 次分析/天 | $0.0028 | **$0.08** |
| 50 次分析/天 | $0.014 | **$0.42** |
| 100 次分析/天 | $0.028 | **$0.84** |

**結論**: 即使每天分析 100 支股票，每月成本也不到 1 美元！

---

## 🆚 與 OpenAI 的比較

### 相同的分析，OpenAI 的成本

使用 GPT-4 進行相同分析：

| 使用量 | Gemini 成本 | OpenAI 成本 | 差異 |
|--------|------------|------------|------|
| 10 次/天 | $0.08/月 | **$32/月** | 400x |
| 50 次/天 | $0.42/月 | **$160/月** | 381x |
| 100 次/天 | $0.84/月 | **$320/月** | 381x |

**Gemini 可以節省 99.75% 的成本！**

---

## 🔧 進階設定

### 調整 AI 模型參數

在 `example_gemini.py` 中，可以調整模型參數：

```python
generation_config = {
    "temperature": 0.7,        # 控制創意度 (0.0-1.0)
    "top_p": 0.95,             # 控制多樣性
    "top_k": 40,               # 控制詞彙選擇範圍
    "max_output_tokens": 2048, # 最大輸出長度
}

model = genai.GenerativeModel(
    'gemini-2.0-flash-exp',
    generation_config=generation_config
)
```

### 錯誤處理

```python
try:
    response = model.generate_content(prompt)
    print(response.text)
except Exception as e:
    if "quota" in str(e).lower():
        print("❌ API 配額已用完，請等待或升級方案")
    elif "invalid" in str(e).lower():
        print("❌ API Key 無效，請檢查設定")
    else:
        print(f"❌ 錯誤: {e}")
```

---

## 📈 最佳實踐

### 1. 善用免費額度

- 免費額度每分鐘 15 次請求
- 建議在請求間加入短暫延遲
- 批次處理分析請求

### 2. 優化 Prompt

好的 prompt 可以：
- 減少 token 使用量
- 提高分析品質
- 降低成本

### 3. 快取策略

對於相同股票的重複查詢：
- 快取股票基本數據（YFinance）
- 定期更新（如每小時）
- 減少 API 呼叫次數

---

## 🆘 常見問題

### Q: Gemini API Key 從哪裡取得？
A: https://aistudio.google.com/app/apikey

### Q: 免費額度用完怎麼辦？
A: 可以：
1. 等待配額重置（每天/每分鐘）
2. 升級到付費方案（但成本仍然很低）

### Q: Gemini 分析品質如何？
A: Gemini 2.0 Flash 在金融分析任務上表現優異，品質接近 GPT-4，但成本僅為其 1/400。

### Q: 可以同時使用 Gemini 和 OpenAI 嗎？
A: 可以！在 `.env` 中同時設定兩個 API Key，程式會優先使用 Gemini。

### Q: Gemini 支援哪些語言？
A: Gemini 支援包括繁體中文在內的 100+ 種語言。

---

## 📚 相關資源

- **Gemini API 文件**: https://ai.google.dev/docs
- **定價說明**: https://ai.google.dev/pricing
- **Google AI Studio**: https://aistudio.google.com/
- **FinRobot GitHub**: https://github.com/AI4Finance-Foundation/FinRobot
