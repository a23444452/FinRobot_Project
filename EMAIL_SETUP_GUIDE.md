# 郵件通知功能設定指南

## 📧 功能說明

FinRobot 支援在每次股票分析後，自動將精美的 HTML 格式分析報告發送到你的電子郵件信箱。

### 報告內容包含

**單一股票分析報告**:
- 完整的股票基本資訊表格（價格、市值、P/E、P/B 等）
- AI 生成的專業分析與投資建議
- 精美的 HTML 排版，易於閱讀

**多股票比較報告**:
- 股票比較表格（並排顯示所有關鍵數據）
- AI 生成的比較分析與投資組合建議
- 視覺化顯示漲跌幅（綠色/紅色）

---

## 🚀 快速設定

### 步驟 1: 選擇郵件服務商

本指南以 **Gmail** 為例（最常用且免費）。其他服務商（Outlook、Yahoo 等）設定方式類似。

### 步驟 2: 取得 Gmail App Password（應用程式密碼）

⚠️ **重要**: 不要使用你的 Gmail 登入密碼！必須使用「應用程式密碼」。

1. **開啟兩步驟驗證**（如果尚未開啟）:
   - 前往: https://myaccount.google.com/security
   - 找到「兩步驟驗證」並啟用

2. **產生應用程式密碼**:
   - 前往: https://myaccount.google.com/apppasswords
   - 應用程式: 選擇「郵件」
   - 裝置: 選擇「其他（自訂名稱）」，輸入「FinRobot」
   - 點擊「產生」
   - **複製產生的 16 位密碼**（格式: xxxx xxxx xxxx xxxx）

### 步驟 3: 設定環境變數

編輯 `.env` 檔案，加入以下設定：

```bash
# 啟用郵件功能
ENABLE_EMAIL=true

# Gmail 設定（必填）
EMAIL_SENDER=your_email@gmail.com          # 你的 Gmail 地址
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx         # 剛才產生的應用程式密碼
EMAIL_RECEIVER=recipient@example.com       # 接收報告的郵件地址

# SMTP 設定（Gmail 預設值，通常不用改）
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### 步驟 4: 測試郵件功能

```bash
cd ~/finrobot-project
uv run python email_service.py
```

如果設定正確，你會看到：
```
=== 郵件服務測試 ===
郵件功能啟用: True
設定狀態: ✅ 完整
SMTP 伺服器: smtp.gmail.com:587
發送者: your_email@gmail.com
接收者: recipient@example.com

📧 發送測試郵件...
✅ 分析報告已發送到: recipient@example.com
```

檢查你的收件匣，應該會收到一封測試報告。

### 步驟 5: 執行股票分析（會自動發送郵件）

```bash
uv run python example_gemini.py
```

分析完成後，報告會自動發送到你的郵箱！

---

## 🔧 其他郵件服務商設定

### Outlook / Hotmail

```bash
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
EMAIL_SENDER=your_email@outlook.com
EMAIL_PASSWORD=your_password
```

### Yahoo Mail

```bash
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
EMAIL_SENDER=your_email@yahoo.com
EMAIL_PASSWORD=your_app_password
```

**注意**: Yahoo 也需要使用「應用程式密碼」，不能使用登入密碼。

### 自訂 SMTP 伺服器

如果你有自己的郵件伺服器：

```bash
SMTP_SERVER=mail.yourdomain.com
SMTP_PORT=587  # 或 465（SSL）、25（不加密）
EMAIL_SENDER=noreply@yourdomain.com
EMAIL_PASSWORD=your_password
```

---

## ❓ 常見問題

### Q1: 郵件發送失敗，顯示「Authentication failed」？

**A**: 最常見的原因是密碼錯誤。
- **Gmail**: 確認使用「應用程式密碼」，不是登入密碼
- **其他**: 檢查是否需要開啟「允許較不安全的應用程式」選項

### Q2: 顯示「Connection timed out」？

**A**: SMTP 伺服器或埠號設定錯誤。
- 確認 `SMTP_SERVER` 和 `SMTP_PORT` 正確
- Gmail: `smtp.gmail.com:587`
- Outlook: `smtp-mail.outlook.com:587`

### Q3: 不想每次都發送郵件怎麼辦？

**A**: 設定 `ENABLE_EMAIL=false` 即可關閉郵件功能。

```bash
ENABLE_EMAIL=false  # 關閉郵件發送
```

### Q4: 可以發送給多個收件者嗎？

**A**: 目前版本僅支援單一收件者。如需多個收件者，可以使用郵件轉寄規則。

### Q5: 報告在垃圾郵件匣？

**A**: 第一次使用時可能會被判定為垃圾郵件。
- 將發送者加入「通訊錄」或「安全寄件者清單」
- 將郵件標記為「非垃圾郵件」

### Q6: 郵件內容是純文字還是 HTML？

**A**: 郵件使用精美的 **HTML 格式**，包含表格、顏色、排版等。所有現代郵件客戶端都能完美顯示。

---

## 🔒 安全性注意事項

1. **絕不提交 .env 檔案到 Git**
   - `.env` 已在 `.gitignore` 中排除
   - 只提交 `.env.example` 範本

2. **使用應用程式密碼，不是登入密碼**
   - Gmail/Yahoo 都支援應用程式密碼
   - 更安全，可隨時撤銷

3. **定期更換密碼**
   - 建議每 3-6 個月更換一次應用程式密碼

4. **不要在公開場合展示 .env 內容**
   - 螢幕分享時注意遮蔽
   - 不要截圖包含密碼的設定

---

## 📊 郵件報告範例

### 單一股票報告

```
主旨: 📊 AAPL 股票分析報告 - 2026-01-27 15:30

內容:
┌─────────────────────────────────┐
│  📊 AAPL 股票分析報告            │
│  2026年01月27日 15:30            │
└─────────────────────────────────┘

【基本資訊】
公司名稱: Apple Inc.
產業: Technology / Consumer Electronics
目前價格: $255.41
市值: $3,774,028,185,600
本益比 (P/E): 35.2
近30天變化: +5.2%

【🤖 AI 分析報告】
1. 公司簡介
   Apple Inc. 是全球領先的科技公司...

2. 財務健康度評估
   - P/E 比率 35.2，略高於產業平均...

3. 投資建議
   建議: 持有
   理由: ...
```

### 多股票比較報告

```
主旨: 📊 多股票比較分析 (AAPL, MSFT, GOOGL) - 2026-01-27 15:35

內容:
┌─────────────────────────────────┐
│  📊 多股票比較分析報告           │
│  AAPL, MSFT, GOOGL              │
│  2026年01月27日 15:35            │
└─────────────────────────────────┘

【股票比較表】
代號  │ 公司名稱      │ 價格    │ P/E  │ 市值         │ 30天變化
AAPL  │ Apple Inc.    │ $255.41 │ 35.2 │ $3.77T      │ +5.2%
MSFT  │ Microsoft...  │ $410.25 │ 38.5 │ $3.05T      │ +3.8%
GOOGL │ Alphabet Inc. │ $175.30 │ 27.1 │ $2.15T      │ +7.1%

【🤖 AI 比較分析】
1. 估值角度
   - GOOGL 的 P/E 最低，估值最具吸引力...

2. 成長性分析
   - GOOGL 30天漲幅最高(+7.1%)...

3. 投資組合建議
   建議配置: GOOGL 40%, AAPL 35%, MSFT 25%
```

---

## 💡 進階功能

### 自訂郵件模板

如果你想客製化郵件外觀，可以編輯 `email_service.py` 中的：
- `_create_report_body()` - 單一股票報告模板
- `_create_comparison_body()` - 比較報告模板

支援完整的 HTML/CSS 自訂！

### 整合到其他程式

```python
from email_service import EmailService

# 初始化服務
email_service = EmailService()

# 發送自訂報告
email_service.send_analysis_report(
    ticker_symbol='AAPL',
    stock_data={...},
    analysis_text='你的分析內容'
)
```

---

## 📞 需要幫助？

如果遇到問題：
1. 確認 `.env` 設定正確（特別是應用程式密碼）
2. 執行測試程式：`uv run python email_service.py`
3. 檢查錯誤訊息，通常會明確指出問題所在
4. 查看本文件的「常見問題」章節

開始享受自動化的股票分析報告吧！📊📧
