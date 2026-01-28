# 📚 FinRobot 文件索引

完整的文件導覽與使用指南。

---

## 🎯 快速開始

| 文件 | 用途 | 適合對象 |
|------|------|---------|
| **README.md** | 專案總覽與快速設定 | 所有使用者 |
| **QUICK_START.md** | 5 分鐘快速開始 | 初次使用者 |
| **QUICK_REFERENCE.md** | 常用指令快速參考 | 已設定好的使用者 |

---

## 🔧 設定指南

### API 設定

| 文件 | 說明 | 必要性 |
|------|------|--------|
| **API_SETUP_GUIDE.md** | 完整的 API 設定教學 | 必要 |
| **GEMINI_INTEGRATION.md** | Gemini API 詳細說明 | 推薦閱讀 |

**閱讀順序**：
1. API_SETUP_GUIDE.md - 了解需要哪些 API
2. GEMINI_INTEGRATION.md - 深入了解 Gemini（推薦使用）

### 郵件通知設定

| 文件 | 說明 | 必要性 |
|------|------|--------|
| **EMAIL_SETUP_GUIDE.md** | 郵件通知完整設定 | 選用 |

**包含內容**：
- Gmail App Password 設定
- 其他郵件服務商設定
- 6 個常見問題解答
- 安全性注意事項

### 手機觸發設定

| 文件 | 說明 | 適合對象 |
|------|------|---------|
| **MOBILE_TRIGGER_GUIDE.md** | 四大手機觸發方案比較 | 想用手機觸發的使用者 |
| **IOS_SHORTCUT_GUIDE.md** | iOS 捷徑詳細教學 | iPhone/iPad 使用者 |

**方案選擇**：
- 只有 iPhone → 閱讀 IOS_SHORTCUT_GUIDE.md
- 想了解所有方案 → 閱讀 MOBILE_TRIGGER_GUIDE.md
- 想用 Telegram Bot → 閱讀 MOBILE_TRIGGER_GUIDE.md 方案 2

---

## 📖 按使用情境選擇文件

### 情境 1: 第一次使用

```
1. README.md (了解專案)
   ↓
2. QUICK_START.md (快速開始)
   ↓
3. API_SETUP_GUIDE.md (設定 API)
   ↓
4. 開始使用！
```

### 情境 2: 想用手機執行

```
1. IOS_SHORTCUT_GUIDE.md (iOS 使用者)
   或
   MOBILE_TRIGGER_GUIDE.md (了解所有方案)
   ↓
2. 按照步驟設定
   ↓
3. QUICK_REFERENCE.md (查詢指令)
```

### 情境 3: 想收郵件報告

```
1. EMAIL_SETUP_GUIDE.md (完整教學)
   ↓
2. 設定 Gmail App Password
   ↓
3. 更新 .env 設定
   ↓
4. 測試郵件功能
```

### 情境 4: 遇到問題

```
1. QUICK_REFERENCE.md (檢查執行方式)
   ↓
2. 對應的設定指南 (API/Email/iOS)
   ↓
3. 查看常見問題章節
```

---

## 📋 文件詳細說明

### 1. README.md
**專案總覽與快速設定**

內容：
- ✅ 專案簡介
- ✅ 檔案結構
- ✅ 快速開始步驟
- ✅ 功能特色
- ✅ 常用命令

適合：
- 第一次看到專案的人
- 想快速了解專案功能
- 需要快速設定指引

---

### 2. QUICK_START.md
**5 分鐘快速開始指南**

內容：
- ✅ 無需 API 立即可用
- ✅ Gemini API 設定（推薦）
- ✅ OpenAI API 設定
- ✅ 範例腳本
- ✅ 成本估算
- ✅ 完整文件索引

適合：
- 想立即開始使用
- 需要 API 設定指引
- 想了解成本

---

### 3. QUICK_REFERENCE.md
**常用指令快速參考**

內容：
- ✅ 正確的執行方式（./前綴）
- ✅ 常用指令範例
- ✅ 為什麼需要 ./ 的解釋
- ✅ iOS 捷徑 SSH 指令
- ✅ 疑難排解
- ✅ 別名設定
- ✅ 台股範例

適合：
- 已經設定好的使用者
- 忘記指令的使用者
- 遇到「command not found」錯誤

---

### 4. API_SETUP_GUIDE.md
**完整的 API 設定教學**

內容：
- ✅ Gemini API 詳細設定
- ✅ OpenAI API 設定
- ✅ Finnhub、FMP、SEC API 設定
- ✅ 功能與 API 對照表
- ✅ 成本估算（兩種方案）

適合：
- 第一次設定 API
- 想了解各 API 功能
- 需要完整功能（財報、SEC 文件等）

---

### 5. GEMINI_INTEGRATION.md
**Gemini API 詳細說明**

內容：
- ✅ 為什麼選擇 Gemini
- ✅ 成本比較（vs OpenAI）
- ✅ 快速開始步驟
- ✅ 功能展示
- ✅ 實際成本估算
- ✅ 進階設定
- ✅ 最佳實踐
- ✅ 常見問題

適合：
- 想深入了解 Gemini API
- 需要成本優化
- 想了解進階功能

---

### 6. EMAIL_SETUP_GUIDE.md
**郵件通知完整設定**

內容：
- ✅ Gmail App Password 設定步驟
- ✅ Outlook、Yahoo 設定
- ✅ 自訂 SMTP 伺服器
- ✅ 6 個常見問題解答
- ✅ 安全性注意事項
- ✅ 郵件報告範例

適合：
- 想啟用郵件通知
- 遇到郵件發送問題
- 想自訂郵件模板

---

### 7. MOBILE_TRIGGER_GUIDE.md
**四大手機觸發方案比較**

內容：
- ✅ 四種方案完整比較表
- ✅ 方案 1: iOS 捷徑 + SSH（推薦初學者）
- ✅ 方案 2: Telegram Bot（推薦進階使用者）
- ✅ 方案 3: FastAPI + Railway（推薦專業使用者）
- ✅ 方案 4: GitHub Actions（最省錢）
- ✅ 每個方案的完整實作步驟
- ✅ 方案選擇建議

適合：
- 想用手機觸發分析
- 需要比較不同方案
- 想了解 Telegram Bot 或 API 方案

---

### 8. IOS_SHORTCUT_GUIDE.md
**iOS 捷徑詳細教學**

內容：
- ✅ 前置需求（Mac、iPhone 設定）
- ✅ 三種捷徑方案（簡單版、進階版、專業版）
- ✅ 逐步設定說明
- ✅ 加入主畫面教學
- ✅ 進階設定（SSH 金鑰、VPN、自動化）
- ✅ 5 個常見問題解答
- ✅ Siri 語音觸發
- ✅ 捷徑美化建議

適合：
- iPhone/iPad 使用者
- 想用一鍵執行分析
- 需要詳細的圖文教學

---

## 🔍 按主題搜尋

### API 相關
- 設定 Gemini API → `API_SETUP_GUIDE.md` 或 `GEMINI_INTEGRATION.md`
- 設定 OpenAI API → `API_SETUP_GUIDE.md`
- API 成本估算 → `GEMINI_INTEGRATION.md`
- API 錯誤排解 → `API_SETUP_GUIDE.md` 常見問題

### 執行相關
- 如何執行腳本 → `QUICK_REFERENCE.md`
- command not found 錯誤 → `QUICK_REFERENCE.md`
- 範例指令 → `QUICK_START.md` 或 `QUICK_REFERENCE.md`
- 台股分析 → `QUICK_REFERENCE.md` 台股範例

### 手機觸發
- iOS 捷徑設定 → `IOS_SHORTCUT_GUIDE.md`
- 所有手機方案比較 → `MOBILE_TRIGGER_GUIDE.md`
- SSH 設定 → `IOS_SHORTCUT_GUIDE.md` 前置需求
- Telegram Bot → `MOBILE_TRIGGER_GUIDE.md` 方案 2

### 郵件通知
- 設定郵件 → `EMAIL_SETUP_GUIDE.md`
- Gmail App Password → `EMAIL_SETUP_GUIDE.md` 步驟 2
- 郵件發送失敗 → `EMAIL_SETUP_GUIDE.md` 常見問題

---

## 📊 文件統計

| 文件 | 行數 | 主題 |
|------|------|------|
| README.md | ~150 | 專案總覽 |
| QUICK_START.md | ~150 | 快速開始 |
| QUICK_REFERENCE.md | ~230 | 執行參考 |
| API_SETUP_GUIDE.md | ~150 | API 設定 |
| GEMINI_INTEGRATION.md | ~280 | Gemini 詳解 |
| EMAIL_SETUP_GUIDE.md | ~280 | 郵件設定 |
| MOBILE_TRIGGER_GUIDE.md | ~550 | 手機方案 |
| IOS_SHORTCUT_GUIDE.md | ~300 | iOS 捷徑 |
| **總計** | **~2,090** | **8 份文件** |

---

## 💡 使用建議

### 新手路線
```
README.md → QUICK_START.md → API_SETUP_GUIDE.md → 開始使用
```

### 進階路線
```
GEMINI_INTEGRATION.md → EMAIL_SETUP_GUIDE.md → MOBILE_TRIGGER_GUIDE.md
```

### 問題排解
```
QUICK_REFERENCE.md → 對應的設定指南 → 常見問題章節
```

---

## 🔄 文件更新日誌

- **2026-01-28**: 新增 QUICK_REFERENCE.md、DOCUMENTATION_INDEX.md
- **2026-01-28**: 更新所有文件的執行方式說明
- **2026-01-27**: 新增 iOS 捷徑與手機觸發指南
- **2026-01-27**: 新增郵件通知功能與文件
- **2026-01-27**: 完成 Gemini API 整合

---

需要更多幫助？選擇最適合你的文件開始閱讀！📚
