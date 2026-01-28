#!/bin/bash

# FinRobot Telegram Bot 停止腳本

set -e

# 顏色輸出
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PID_FILE="$HOME/telegram-bot.pid"

if [ ! -f "$PID_FILE" ]; then
    echo -e "${RED}❌ Bot 未在運行${NC}"
    exit 1
fi

BOT_PID=$(cat "$PID_FILE")

if ps -p "$BOT_PID" > /dev/null 2>&1; then
    echo -e "${GREEN}🛑 正在停止 Bot (PID: $BOT_PID)...${NC}"
    kill "$BOT_PID"

    # 等待程序結束
    sleep 2

    if ps -p "$BOT_PID" > /dev/null 2>&1; then
        echo -e "${RED}⚠️  正常停止失敗,強制終止...${NC}"
        kill -9 "$BOT_PID"
    fi

    rm -f "$PID_FILE"
    echo -e "${GREEN}✅ Bot 已停止${NC}"
else
    echo -e "${RED}❌ Bot 未在運行 (PID 檔案過期)${NC}"
    rm -f "$PID_FILE"
fi
