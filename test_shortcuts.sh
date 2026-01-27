#!/bin/bash

# 測試 iOS 捷徑腳本

echo "=== FinRobot iOS 捷徑測試 ==="
echo ""

# 測試 1: 單一股票分析
echo "測試 1: 分析 AAPL"
echo "執行: ~/finrobot-project/run_analysis.sh AAPL analyze"
echo ""

# 測試 2: 多股票比較
echo "測試 2: 比較 AAPL,MSFT,GOOGL"  
echo "執行: ~/finrobot-project/run_analysis.sh AAPL,MSFT,GOOGL compare"
echo ""

# 顯示日誌檔案位置
echo "日誌檔案: ~/finrobot-logs.txt"
echo ""

# 提示
echo "💡 將以上指令複製到 iOS 捷徑的 SSH 指令欄位中"
echo "💡 記得替換 IP 位址、使用者名稱和密碼"
