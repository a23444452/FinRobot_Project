# FinRobot 金融分析專案

使用 FinRobot 和 LLMs 進行股票分析與金融研究。

## 專案結構

```
finrobot-project/
├── .env.example             # API 金鑰範本
├── .env                     # 實際 API 金鑰（不提交）
├── API_SETUP_GUIDE.md       # API 設定詳細指南
├── EMAIL_SETUP_GUIDE.md     # 📧 郵件通知設定指南
├── MOBILE_TRIGGER_GUIDE.md  # 📱 手機觸發完整指南
├── IOS_SHORTCUT_GUIDE.md    # 📱 iOS 捷徑詳細教學
├── test_api.py              # API 金鑰測試腳本
├── example_basic.py         # 基本範例（無需付費 API）
├── example_gemini.py        # Gemini AI 分析範例
├── email_service.py         # 📧 郵件服務模組
├── run_analysis.sh          # 📱 執行腳本（SSH 觸發用）
├── main.py                  # 主程式
├── pyproject.toml           # 專案配置
└── README.md                # 本檔案
```

## 快速開始

### 1. 設定 API 金鑰

參閱 `API_SETUP_GUIDE.md` 取得詳細說明。

**推薦使用 Gemini API（更便宜）**：

```bash
cp .env.example .env
# 編輯 .env，填入 GEMINI_API_KEY
```

或使用 **OpenAI API**：

```bash
cp .env.example .env
# 編輯 .env，填入 OPENAI_API_KEY
```

### 2. 測試 API 設定

```bash
uv run python test_api.py
```

### 3. 執行範例

不需要任何 API，使用 YFinance：

```bash
uv run python example_basic.py
```

使用 Gemini AI 分析（推薦）：

```bash
uv run python example_gemini.py
```

### 4. 設定郵件通知（選用）

想要收到精美的 HTML 分析報告郵件？

```bash
# 參閱詳細設定指南
cat EMAIL_SETUP_GUIDE.md

# 快速設定：編輯 .env
ENABLE_EMAIL=true
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=recipient@example.com
```

### 5. 手機觸發設定（選用）

**方案 A: Telegram Bot（推薦）⭐**
```bash
# 1. 在 Telegram 搜尋 @BotFather 建立 Bot
# 2. 設定 .env
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_ALLOWED_USERS=your_user_id

# 3. 啟動 Bot
./start_telegram_bot.sh

# 4. 在 Telegram 中使用
/analyze AAPL
/compare AAPL MSFT GOOGL
```

**方案 B: iOS 捷徑**
1. Mac 啟用「遠端登入」
2. iPhone 建立捷徑，SSH 指令: `~/finrobot-project/run_analysis.sh AAPL analyze`
3. 點擊執行，30 秒完成！

**查看所有方案**：
- `TELEGRAM_BOT_SETUP.md` - Telegram Bot 完整指南（推薦）
- `IOS_SHORTCUT_GUIDE.md` - iOS 捷徑教學
- `MOBILE_TRIGGER_GUIDE.md` - 4 種手機觸發方案比較

## ✨ 功能特色

- 📊 **即時股票數據**：使用 YFinance 免費取得市場數據
- 🤖 **AI 智能分析**：Google Gemini 2.0 Flash 提供專業分析
- 💰 **超低成本**：API 成本僅為 OpenAI 的 1/400
- 📈 **深度分析**：單一股票完整評估（財務、風險、建議）
- 🔍 **比較分析**：多股票並排比較與投資組合建議
- 📧 **郵件通知**：自動發送精美 HTML 報告到信箱
- 📱 **手機觸發**：iOS 捷徑、Telegram Bot、API 等多種方式
- 🇹🇼 **繁體中文**：完整中文介面與分析報告

## 常用命令

```bash
# 執行腳本
uv run python <script>.py

# 安裝新套件
uv add <package-name>

# 更新環境
uv sync
```

## 學習資源

- FinRobot 官網: https://finrobot.ai
- FinRobot GitHub: https://github.com/AI4Finance-Foundation/FinRobot
