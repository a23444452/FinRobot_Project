"""
FinRobot Telegram Bot
使用 Telegram Bot 觸發股票分析並接收郵件報告

使用方式:
1. 在 Telegram 搜尋 @BotFather 建立 Bot
2. 設定 .env 中的 TELEGRAM_BOT_TOKEN
3. 執行: uv run python telegram_bot.py
4. 在 Telegram 中傳送指令給 Bot

指令:
/start - 顯示歡迎訊息
/analyze AAPL - 分析單一股票
/compare AAPL MSFT GOOGL - 比較多支股票
/help - 顯示說明
"""

import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from example_gemini import analyze_with_gemini, compare_stocks_with_gemini

# 載入環境變數
load_dotenv()

# 設定
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = os.getenv("TELEGRAM_ALLOWED_USERS", "").split(",")  # 限制使用者

# 移除空字符串
ALLOWED_USERS = [user.strip() for user in ALLOWED_USERS if user.strip()]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """歡迎訊息"""
    welcome_message = """
📊 **FinRobot 股票分析 Bot**

我可以幫你分析股票並發送報告到郵箱！

**可用指令:**
/analyze AAPL - 分析 Apple 股票
/compare AAPL MSFT GOOGL - 比較多支股票
/help - 顯示說明

**範例:**
`/analyze TSLA`
`/compare AAPL MSFT NVDA`

⚠️ 分析需要 10-30 秒，請耐心等待
📧 報告會自動發送到您設定的郵箱
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """說明訊息"""
    help_message = """
📖 **使用說明**

**單一股票分析:**
`/analyze TICKER`
範例: `/analyze AAPL`

**多股票比較:**
`/compare TICKER1 TICKER2 TICKER3`
範例: `/compare AAPL MSFT GOOGL`

**支援的股票代號:**
- 美股: AAPL, MSFT, GOOGL, TSLA 等
- 台股: 2330.TW, 2317.TW 等 (需加 .TW)

**注意事項:**
✅ 分析時間約 10-30 秒
✅ 報告會發送到郵箱 (如已啟用)
✅ 每次請求會消耗少量 API 配額
"""
    await update.message.reply_text(help_message, parse_mode='Markdown')

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """分析單一股票"""
    # 檢查權限
    user_id = str(update.effective_user.id)
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text(
            "❌ 未授權使用\n"
            "請聯繫管理員將您的 Telegram ID 加入白名單\n"
            f"您的 ID: `{user_id}`",
            parse_mode='Markdown'
        )
        return

    # 檢查參數
    if not context.args:
        await update.message.reply_text(
            "❌ 請提供股票代號\n"
            "範例: `/analyze AAPL`",
            parse_mode='Markdown'
        )
        return

    ticker = context.args[0].upper()

    # 發送處理中訊息
    msg = await update.message.reply_text(
        f"🔍 正在分析 **{ticker}**...\n"
        f"⏱️ 預計需要 10-30 秒\n"
        f"📧 報告將發送到郵箱",
        parse_mode='Markdown'
    )

    try:
        # 在背景執行分析(避免阻塞)
        await asyncio.to_thread(analyze_with_gemini, ticker)

        await msg.edit_text(
            f"✅ **{ticker}** 分析完成！\n\n"
            f"📊 股票代號: {ticker}\n"
            f"📧 報告已發送到您的郵箱\n"
            f"⏰ 完成時間: {asyncio.get_event_loop().time():.1f}s",
            parse_mode='Markdown'
        )
    except Exception as e:
        error_msg = str(e)
        await msg.edit_text(
            f"❌ 分析失敗\n\n"
            f"**股票代號:** {ticker}\n"
            f"**錯誤訊息:** `{error_msg[:200]}`\n\n"
            f"💡 可能原因:\n"
            f"• 股票代號不存在\n"
            f"• API 配額用完\n"
            f"• 網路連線問題",
            parse_mode='Markdown'
        )

async def compare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """比較多支股票"""
    user_id = str(update.effective_user.id)
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text(
            "❌ 未授權使用\n"
            f"您的 ID: `{user_id}`",
            parse_mode='Markdown'
        )
        return

    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ 請提供至少 2 支股票代號\n"
            "範例: `/compare AAPL MSFT GOOGL`",
            parse_mode='Markdown'
        )
        return

    tickers = [t.upper() for t in context.args]
    ticker_str = ", ".join(tickers)

    msg = await update.message.reply_text(
        f"🔍 正在比較分析...\n\n"
        f"📊 股票: **{ticker_str}**\n"
        f"⏱️ 預計需要 20-60 秒\n"
        f"📧 報告將發送到郵箱",
        parse_mode='Markdown'
    )

    try:
        # 在背景執行比較分析
        await asyncio.to_thread(compare_stocks_with_gemini, tickers)

        await msg.edit_text(
            f"✅ 比較分析完成！\n\n"
            f"📊 分析股票: {ticker_str}\n"
            f"📈 共 {len(tickers)} 支股票\n"
            f"📧 報告已發送到您的郵箱",
            parse_mode='Markdown'
        )
    except Exception as e:
        error_msg = str(e)
        await msg.edit_text(
            f"❌ 比較分析失敗\n\n"
            f"**股票:** {ticker_str}\n"
            f"**錯誤:** `{error_msg[:200]}`",
            parse_mode='Markdown'
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """錯誤處理"""
    print(f"❌ Telegram Bot 錯誤: {context.error}")

    if update and update.message:
        await update.message.reply_text(
            "❌ 發生錯誤，請稍後再試\n"
            "或執行 /help 查看使用說明"
        )

def main():
    """啟動 Bot"""
    if not BOT_TOKEN:
        print("❌ 錯誤: 請在 .env 設定 TELEGRAM_BOT_TOKEN")
        print("\n📝 設定步驟:")
        print("1. 在 Telegram 搜尋 @BotFather")
        print("2. 傳送 /newbot 建立新 Bot")
        print("3. 按照指示設定 Bot 名稱")
        print("4. 複製 Bot Token 到 .env 檔案")
        print("\n範例 .env 設定:")
        print("TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz")
        return

    print("🤖 正在啟動 Telegram Bot...")
    print(f"📱 Bot Token: {BOT_TOKEN[:10]}...")

    if ALLOWED_USERS:
        print(f"🔒 限制使用者: {', '.join(ALLOWED_USERS)}")
    else:
        print("⚠️  警告: 未設定 TELEGRAM_ALLOWED_USERS，所有人都可使用")

    # 建立 Application
    app = Application.builder().token(BOT_TOKEN).build()

    # 註冊指令
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("compare", compare))

    # 註冊錯誤處理
    app.add_error_handler(error_handler)

    # 啟動 Bot
    print("✅ Telegram Bot 已啟動！")
    print("💡 按 Ctrl+C 可停止")
    print("\n📱 在 Telegram 中搜尋您的 Bot 並傳送 /start 開始使用")

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
