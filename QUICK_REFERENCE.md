# 🚀 快速參考指南

## 執行方式

### ❌ 錯誤的執行方式
```bash
cd ~/finrobot-project
run_analysis.sh AAPL analyze
# 錯誤: zsh: command not found: run_analysis.sh
```

### ✅ 正確的執行方式

**方法 1: 使用 `./` 前綴（推薦）**
```bash
cd ~/finrobot-project
./run_analysis.sh AAPL analyze
```

**方法 2: 使用完整路徑**
```bash
~/finrobot-project/run_analysis.sh AAPL analyze
```

**方法 3: 使用 bash 直接執行**
```bash
cd ~/finrobot-project
bash run_analysis.sh AAPL analyze
```

---

## 常用指令

### 單一股票分析
```bash
# 分析 Apple
./run_analysis.sh AAPL analyze

# 分析 Microsoft
./run_analysis.sh MSFT analyze

# 分析 Tesla
./run_analysis.sh TSLA analyze
```

### 多股票比較
```bash
# 比較 3 支科技股
./run_analysis.sh AAPL,MSFT,GOOGL compare

# 比較 5 支科技股
./run_analysis.sh AAPL,MSFT,GOOGL,NVDA,TSLA compare

# 比較台股（需要加 .TW）
./run_analysis.sh 2330.TW,2317.TW compare
```

### 查看日誌
```bash
# 查看最近的執行日誌
tail -20 ~/finrobot-logs.txt

# 即時監看日誌
tail -f ~/finrobot-logs.txt

# 查看所有日誌
cat ~/finrobot-logs.txt
```

---

## 為什麼需要 `./` ？

在 Unix/Linux/macOS 系統中：

- `run_analysis.sh` - 系統會在 PATH 環境變數中尋找
- `./run_analysis.sh` - 執行當前目錄的腳本
- `~/finrobot-project/run_analysis.sh` - 使用絕對路徑

出於安全考量，當前目錄 (`.`) 通常不在 PATH 中，所以需要明確指定 `./`

---

## iOS 捷徑設定

### SSH 指令範例

**單一股票分析**:
```bash
~/finrobot-project/run_analysis.sh AAPL analyze
```

**多股票比較**:
```bash
~/finrobot-project/run_analysis.sh AAPL,MSFT,GOOGL compare
```

**使用變數（進階）**:
```bash
~/finrobot-project/run_analysis.sh [變數:股票代號] analyze
```

注意：在 SSH 中使用 `~` 或完整路徑，不需要 `./`

---

## 測試腳本

### 快速測試
```bash
cd ~/finrobot-project
./run_analysis.sh AAPL analyze
```

### 預期輸出
```
📊 FinRobot 股票分析
股票代號: AAPL
動作: analyze

🔍 正在分析 AAPL...

============================================================
🤖 使用 Gemini 2.0 Flash 分析: AAPL
============================================================

📊 正在取得股票數據...
...
✅ 分析完成！
📧 報告已發送到郵箱（如果啟用）
```

---

## 疑難排解

### 問題 1: `command not found`
```bash
# 錯誤
run_analysis.sh AAPL analyze

# 解決：加上 ./
./run_analysis.sh AAPL analyze
```

### 問題 2: `Permission denied`
```bash
# 檢查權限
ls -la run_analysis.sh

# 如果沒有執行權限，加上：
chmod +x run_analysis.sh
```

### 問題 3: `No such file or directory`
```bash
# 確認在正確的目錄
pwd
# 應該顯示: /Users/vincewang/finrobot-project

# 如果不在，切換到正確目錄
cd ~/finrobot-project
```

### 問題 4: 腳本執行但沒輸出
```bash
# 檢查日誌
tail ~/finrobot-logs.txt

# 直接執行 Python
cd ~/finrobot-project
uv run python example_gemini.py
```

---

## 別名設定（進階）

想要直接輸入 `analyze AAPL` 就執行？

在 `~/.zshrc` 或 `~/.bashrc` 加入：

```bash
# FinRobot 別名
alias analyze='~/finrobot-project/run_analysis.sh'
```

重新載入設定：
```bash
source ~/.zshrc
```

現在可以直接執行：
```bash
analyze AAPL analyze
analyze AAPL,MSFT,GOOGL compare
```

---

## 快速參考表

| 指令 | 說明 |
|------|------|
| `./run_analysis.sh AAPL analyze` | 分析 Apple |
| `./run_analysis.sh AAPL,MSFT compare` | 比較兩支股票 |
| `tail -20 ~/finrobot-logs.txt` | 查看最近 20 行日誌 |
| `uv run python example_gemini.py` | 直接執行範例程式 |
| `uv run python test_api.py` | 測試 API 設定 |
| `uv run python email_service.py` | 測試郵件服務 |

---

## 台股範例

```bash
# 分析台積電（2330）
./run_analysis.sh 2330.TW analyze

# 分析鴻海（2317）
./run_analysis.sh 2317.TW analyze

# 比較台股
./run_analysis.sh 2330.TW,2317.TW,2454.TW compare
```

---

需要更多幫助？查看完整文件：
- `IOS_SHORTCUT_GUIDE.md` - iOS 捷徑設定
- `EMAIL_SETUP_GUIDE.md` - 郵件通知設定
- `MOBILE_TRIGGER_GUIDE.md` - 手機觸發方案
