#!/bin/bash

# FinRobot 股票分析執行腳本
# 適用於 iOS 捷徑 + SSH 觸發

set -e  # 發生錯誤時停止執行

# 顏色輸出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 專案路徑
PROJECT_DIR="$HOME/finrobot-project"
LOG_FILE="$HOME/finrobot-logs.txt"

# 記錄開始時間
echo "$(date '+%Y-%m-%d %H:%M:%S') - 開始執行分析" >> "$LOG_FILE"

# 檢查專案目錄
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}❌ 專案目錄不存在: $PROJECT_DIR${NC}" | tee -a "$LOG_FILE"
    exit 1
fi

cd "$PROJECT_DIR"

# 解析參數
TICKER="${1:-AAPL}"  # 預設 AAPL
ACTION="${2:-analyze}"  # 預設 analyze (或 compare)

echo -e "${GREEN}📊 FinRobot 股票分析${NC}"
echo -e "${YELLOW}股票代號: $TICKER${NC}"
echo -e "${YELLOW}動作: $ACTION${NC}"
echo ""

# 記錄參數
echo "$(date '+%Y-%m-%d %H:%M:%S') - 參數: TICKER=$TICKER, ACTION=$ACTION" >> "$LOG_FILE"

# 執行分析
if [ "$ACTION" = "analyze" ]; then
    echo -e "${GREEN}🔍 正在分析 $TICKER...${NC}"
    uv run python -c "from example_gemini import analyze_with_gemini; analyze_with_gemini('$TICKER')"
    
elif [ "$ACTION" = "compare" ]; then
    # 多股票比較，參數用逗號分隔
    IFS=',' read -ra TICKERS <<< "$TICKER"
    echo -e "${GREEN}🔍 正在比較: ${TICKERS[*]}${NC}"
    
    # 建立 Python list 字串
    TICKER_LIST="["
    for i in "${!TICKERS[@]}"; do
        if [ $i -gt 0 ]; then
            TICKER_LIST+=", "
        fi
        TICKER_LIST+="'${TICKERS[$i]}'"
    done
    TICKER_LIST+="]"
    
    uv run python -c "from example_gemini import compare_stocks_with_gemini; compare_stocks_with_gemini($TICKER_LIST)"
    
else
    echo -e "${RED}❌ 未知的動作: $ACTION${NC}" | tee -a "$LOG_FILE"
    exit 1
fi

# 記錄完成時間
echo "$(date '+%Y-%m-%d %H:%M:%S') - 分析完成" >> "$LOG_FILE"
echo -e "${GREEN}✅ 分析完成！${NC}"
echo -e "${GREEN}📧 報告已發送到郵箱（如果啟用）${NC}"
