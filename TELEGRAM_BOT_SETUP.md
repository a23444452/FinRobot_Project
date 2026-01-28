# 📱 Telegram Bot 設定指南

使用 Telegram Bot 觸發 FinRobot 股票分析,跨平台支援 iOS、Android、桌面版。

---

## 🎯 優點

- ✅ **跨平台**: iOS、Android、Windows、macOS、Linux 都能使用
- ✅ **即時互動**: 聊天介面,指令簡單直觀
- ✅ **遠端觸發**: 不需要在同一網路
- ✅ **免費**: Telegram 完全免費,無使用限制
- ✅ **安全**: 可限制特定使用者存取
- ✅ **背景執行**: Bot 在伺服器背景運行,隨時可用

---

## 📋 前置需求

1. **Telegram 帳號** (手機 App 或桌面版)
2. **FinRobot 專案** 已完成基本設定
3. **郵件通知** 已啟用 (可選,但建議開啟)
4. **Mac/Linux 主機** 保持開機 (或使用雲端伺服器)

---

## 🚀 快速設定 (5 分鐘)

### 步驟 1: 建立 Telegram Bot

1. 在 Telegram 搜尋 **@BotFather**
2. 傳送 `/newbot` 指令
3. 按照指示設定:
   - **Bot 顯示名稱** (例如: FinRobot Stock Analyzer)
   - **Bot 用戶名** (必須以 `bot` 結尾,例如: `finrobot_stock_bot`)
4. **記下 Bot Token** (格式: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 步驟 2: 取得您的 Telegram User ID

1. 在 Telegram 搜尋 **@userinfobot**
2. 傳送任意訊息
3. Bot 會回覆您的 User ID (例如: `123456789`)
4. **記下這個 ID** (用於限制使用者存取)

### 步驟 3: 設定環境變數

編輯 `.env` 檔案:

```bash
# Telegram Bot 設定
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_ALLOWED_USERS=123456789,987654321

# 確保郵件通知已啟用
ENABLE_EMAIL=true
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=your_email@gmail.com
```

**說明**:
- `TELEGRAM_BOT_TOKEN`: 從 @BotFather 取得的 Token
- `TELEGRAM_ALLOWED_USERS`: 允許使用的 User ID (逗號分隔,可設多個)
  - ⚠️ 強烈建議設定,否則所有人都能使用您的 Bot
  - 如果不設定此項,任何人都可以透過您的 Bot 消耗 API 配額

### 步驟 4: 啟動 Bot

```bash
cd ~/finrobot-project

# 方法 1: 背景執行 (推薦)
./start_telegram_bot.sh

# 方法 2: 前台執行 (用於測試)
uv run python telegram_bot.py
```

**背景執行的優點**:
- 關閉終端機後仍會繼續運行
- 自動記錄日誌到 `~/telegram-bot.log`
- 可隨時檢查狀態和停止

### 步驟 5: 測試 Bot

1. 在 Telegram 搜尋您的 Bot (用戶名)
2. 點擊「開始」或傳送 `/start`
3. Bot 會回覆歡迎訊息
4. 測試指令:
   ```
   /analyze AAPL
   ```
5. 等待 10-30 秒,檢查:
   - Telegram 中收到完成通知
   - 郵箱收到分析報告

---

## 💬 可用指令

### 基本指令

```
/start - 顯示歡迎訊息
/help - 顯示使用說明
```

### 分析指令

```bash
# 單一股票分析
/analyze AAPL          # Apple
/analyze TSLA          # Tesla
/analyze 2330.TW       # 台積電

# 多股票比較
/compare AAPL MSFT GOOGL         # 比較 3 支美股
/compare AAPL MSFT NVDA TSLA     # 比較 4 支科技股
/compare 2330.TW 2317.TW         # 比較 2 支台股
```

---

## 🔧 管理 Bot

### 查看 Bot 狀態

```bash
# 檢查是否在運行
ps aux | grep telegram_bot.py

# 查看日誌 (最近 20 行)
tail -20 ~/telegram-bot.log

# 即時監看日誌
tail -f ~/telegram-bot.log
```

### 停止 Bot

```bash
# 使用停止腳本
./stop_telegram_bot.sh

# 或手動停止
kill $(cat ~/telegram-bot.pid)
```

### 重啟 Bot

```bash
# 停止
./stop_telegram_bot.sh

# 等待 2 秒
sleep 2

# 啟動
./start_telegram_bot.sh
```

---

## 🌐 進階設定

### 部署到雲端伺服器 (24/7 運行)

如果您不想讓 Mac 一直開機,可以部署到雲端:

**選項 1: Railway (推薦)**
- 免費額度: $5/月
- 步驟: 參考 `MOBILE_TRIGGER_GUIDE.md` 方案 3

**選項 2: AWS EC2 Free Tier**
```bash
# 1. 建立 t2.micro EC2 instance
# 2. SSH 連線到 instance
# 3. 安裝依賴
sudo apt update
sudo apt install python3 python3-pip git
pip3 install uv

# 4. Clone 專案
git clone https://github.com/your-username/finrobot-project.git
cd finrobot-project

# 5. 設定 .env
nano .env
# (貼上您的 API keys)

# 6. 啟動 Bot
./start_telegram_bot.sh
```

### 使用 systemd 自動啟動 (Linux)

建立服務檔案 `/etc/systemd/system/telegram-bot.service`:

```ini
[Unit]
Description=FinRobot Telegram Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/home/your_username/finrobot-project
ExecStart=/home/your_username/.local/bin/uv run python telegram_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

啟用服務:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

### 限制 Bot 使用量

在 `.env` 中設定:

```bash
# 只允許特定使用者
TELEGRAM_ALLOWED_USERS=123456789,987654321

# 限制 API 請求頻率 (在 telegram_bot.py 中實作)
# 例如: 每個使用者每小時最多 10 次請求
```

---

## ❓ 常見問題

### Q1: Bot 沒有回應?

**檢查清單**:
1. Bot 是否在運行?
   ```bash
   ps aux | grep telegram_bot.py
   ```
2. Token 是否正確?
   ```bash
   cat .env | grep TELEGRAM_BOT_TOKEN
   ```
3. 查看錯誤日誌:
   ```bash
   tail -50 ~/telegram-bot.log
   ```
4. 重啟 Bot:
   ```bash
   ./stop_telegram_bot.sh && sleep 2 && ./start_telegram_bot.sh
   ```

### Q2: 收到「未授權使用」訊息?

**原因**: 您的 Telegram User ID 不在 `TELEGRAM_ALLOWED_USERS` 中

**解決**:
1. 取得您的 User ID (傳送訊息給 @userinfobot)
2. 編輯 `.env`:
   ```bash
   TELEGRAM_ALLOWED_USERS=123456789,你的UserID
   ```
3. 重啟 Bot:
   ```bash
   ./stop_telegram_bot.sh && ./start_telegram_bot.sh
   ```

### Q3: Bot 回應很慢?

**原因**: 股票分析需要呼叫 Gemini API,通常需要 10-30 秒

**改善方式**:
- 單一股票分析: ~15 秒
- 多股票比較: ~30-60 秒
- 使用更快的 API (但成本較高)

### Q4: 想在手機上隨時使用?

**兩種方案**:

**方案 A**: Mac 保持開機
- 設定 Mac 節能: 系統偏好設定 → 節能 → 勾選「喚醒以供 WiFi 網路存取」
- 優點: 免費
- 缺點: Mac 需要一直開著

**方案 B**: 部署到雲端 (推薦)
- 使用 Railway、AWS、GCP 等雲端服務
- 優點: 24/7 隨時可用
- 缺點: 每月 $0-5 費用

### Q5: 如何增加新功能?

編輯 `telegram_bot.py`,參考現有指令結構:

```python
async def your_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """您的自訂指令"""
    # 您的程式碼

# 在 main() 中註冊
app.add_handler(CommandHandler("yourcommand", your_command))
```

### Q6: 安全性考量?

**最佳實踐**:
1. ✅ **設定 TELEGRAM_ALLOWED_USERS** (必須)
2. ✅ 不要分享您的 Bot Token
3. ✅ 定期更換 API Keys
4. ✅ 監控 Bot 使用量
5. ✅ 設定郵件通知,掌握所有分析活動

---

## 🎯 使用範例

### 場景 1: 早上通勤時快速查看股票

```
1. 打開 Telegram
2. /analyze AAPL
3. 等待通知
4. 打開郵箱閱讀完整報告
```

### 場景 2: 比較多支科技股

```
/compare AAPL MSFT GOOGL NVDA TSLA
```

等待 ~60 秒後,收到包含 5 支股票比較的報告。

### 場景 3: 分析台股

```
/analyze 2330.TW
/compare 2330.TW 2317.TW 2454.TW
```

---

## 📊 成本估算

| 項目 | 成本 |
|------|------|
| Telegram Bot | $0 (免費) |
| Gemini API | ~$0-2/月 (免費額度) |
| Email (Gmail) | $0 (免費) |
| Mac 本機執行 | $0 |
| **雲端部署 (可選)** | |
| Railway | $5/月 |
| AWS EC2 t2.micro | $0 (前 12 個月免費) |

**推薦配置**: Telegram Bot + Gemini + Gmail = **完全免費** 🎉

---

## 🔄 與其他方案比較

| 功能 | Telegram Bot | iOS 捷徑 | FastAPI |
|------|-------------|----------|---------|
| **跨平台** | ✅ | ❌ (僅 iOS) | ✅ |
| **設定難度** | ⭐⭐ | ⭐ | ⭐⭐⭐⭐ |
| **需要電腦開機** | ✅ | ✅ | ❌ |
| **即時互動** | ✅ | ❌ | ❌ |
| **成本** | 免費 | 免費 | $5/月 |
| **適合對象** | 所有使用者 | iPhone 使用者 | 專業使用者 |

---

## 💡 下一步

完成設定後,您可以:

1. ✅ 自訂 Bot 指令 (編輯 `telegram_bot.py`)
2. ✅ 部署到雲端伺服器 (24/7 運行)
3. ✅ 設定自動化 (定時分析特定股票)
4. ✅ 整合其他資料源 (新聞、財報等)

---

需要幫助? 查看 `MOBILE_TRIGGER_GUIDE.md` 了解其他手機觸發方案!
