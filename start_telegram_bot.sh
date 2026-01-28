#!/bin/bash

# FinRobot Telegram Bot 啟動腳本
# 可在背景執行,即使關閉終端機也會繼續運行

set -e

# 顏色輸出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 專案路徑
PROJECT_DIR="$HOME/finrobot-project"
LOG_FILE="$HOME/telegram-bot.log"
PID_FILE="$HOME/telegram-bot.pid"

cd "$PROJECT_DIR"

# 檢查是否已在運行
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Bot 已在運行 (PID: $OLD_PID)${NC}"
        echo -e "${YELLOW}如需重啟,請先執行: ./stop_telegram_bot.sh${NC}"
        exit 1
    else
        # PID 檔案存在但程序不在運行,清除舊檔案
        rm -f "$PID_FILE"
    fi
fi

echo -e "${GREEN}🤖 正在啟動 Telegram Bot...${NC}"
echo -e "${YELLOW}📝 日誌檔案: $LOG_FILE${NC}"

# 在背景執行 Bot
nohup uv run python telegram_bot.py >> "$LOG_FILE" 2>&1 &
BOT_PID=$!

# 儲存 PID
echo "$BOT_PID" > "$PID_FILE"

# 等待啟動
sleep 2

# 檢查是否成功啟動
if ps -p "$BOT_PID" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Bot 已啟動！${NC}"
    echo -e "${GREEN}📱 PID: $BOT_PID${NC}"
    echo -e "${GREEN}📋 查看日誌: tail -f $LOG_FILE${NC}"
    echo -e "${GREEN}🛑 停止 Bot: ./stop_telegram_bot.sh${NC}"
    echo ""
    echo -e "${YELLOW}💡 現在可以在 Telegram 中使用您的 Bot 了！${NC}"
else
    echo -e "${RED}❌ Bot 啟動失敗${NC}"
    echo -e "${RED}查看日誌: cat $LOG_FILE${NC}"
    rm -f "$PID_FILE"
    exit 1
fi
