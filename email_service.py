"""
郵件發送服務模組
支援將股票分析報告透過 Email 發送給使用者
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()


class EmailService:
    """郵件發送服務類別"""
    
    def __init__(self):
        """初始化郵件服務設定"""
        self.enabled = os.getenv("ENABLE_EMAIL", "false").lower() == "true"
        self.sender = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.receiver = os.getenv("EMAIL_RECEIVER")
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        
    def is_enabled(self):
        """檢查郵件功能是否啟用"""
        return self.enabled
    
    def is_configured(self):
        """檢查郵件設定是否完整"""
        if not self.enabled:
            return True  # 未啟用時視為正常
        
        missing = []
        if not self.sender:
            missing.append("EMAIL_SENDER")
        if not self.password:
            missing.append("EMAIL_PASSWORD")
        if not self.receiver:
            missing.append("EMAIL_RECEIVER")
        
        if missing:
            print(f"⚠️  郵件功能已啟用但設定不完整，缺少: {', '.join(missing)}")
            return False
        
        return True
    
    def send_analysis_report(self, ticker_symbol, stock_data, analysis_text):
        """
        發送股票分析報告郵件
        
        Args:
            ticker_symbol: 股票代號
            stock_data: 股票數據字典
            analysis_text: AI 分析內容
        """
        if not self.is_enabled():
            return
        
        if not self.is_configured():
            return
        
        try:
            # 建立郵件內容
            subject = f"📊 {ticker_symbol} 股票分析報告 - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            body = self._create_report_body(ticker_symbol, stock_data, analysis_text)
            
            # 發送郵件
            self._send_email(subject, body)
            print(f"✅ 分析報告已發送到: {self.receiver}")
            
        except Exception as e:
            print(f"❌ 郵件發送失敗: {e}")
    
    def send_comparison_report(self, tickers, stocks_data, analysis_text):
        """
        發送多股票比較報告郵件
        
        Args:
            tickers: 股票代號列表
            stocks_data: 股票數據列表
            analysis_text: AI 比較分析內容
        """
        if not self.is_enabled():
            return
        
        if not self.is_configured():
            return
        
        try:
            # 建立郵件內容
            tickers_str = ", ".join(tickers)
            subject = f"📊 多股票比較分析 ({tickers_str}) - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            body = self._create_comparison_body(tickers, stocks_data, analysis_text)
            
            # 發送郵件
            self._send_email(subject, body)
            print(f"✅ 比較分析報告已發送到: {self.receiver}")
            
        except Exception as e:
            print(f"❌ 郵件發送失敗: {e}")
    
    def _create_report_body(self, ticker_symbol, stock_data, analysis_text):
        """建立單一股票分析報告內容"""
        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .header {{ background-color: #4CAF50; color: white; padding: 20px; text-align: center; }}
        .content {{ padding: 20px; }}
        .section {{ margin-bottom: 20px; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        .data-table th {{ background-color: #f2f2f2; padding: 10px; text-align: left; border: 1px solid #ddd; }}
        .data-table td {{ padding: 10px; border: 1px solid #ddd; }}
        .analysis {{ background-color: #f9f9f9; padding: 15px; border-left: 4px solid #4CAF50; margin: 15px 0; }}
        .footer {{ text-align: center; color: #666; font-size: 12px; padding: 20px; border-top: 1px solid #ddd; }}
        .positive {{ color: #4CAF50; font-weight: bold; }}
        .negative {{ color: #f44336; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 {ticker_symbol} 股票分析報告</h1>
        <p>{datetime.now().strftime('%Y年%m月%d日 %H:%M')}</p>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>基本資訊</h2>
            <table class="data-table">
                <tr><th>項目</th><th>數值</th></tr>
                <tr><td>公司名稱</td><td>{stock_data['name']}</td></tr>
                <tr><td>產業</td><td>{stock_data['sector']} / {stock_data['industry']}</td></tr>
                <tr><td>目前價格</td><td>${stock_data['currentPrice']}</td></tr>
                <tr><td>市值</td><td>${stock_data['marketCap']:,.0f}</td></tr>
                <tr><td>本益比 (P/E)</td><td>{stock_data['pe_ratio']}</td></tr>
                <tr><td>股價淨值比 (P/B)</td><td>{stock_data['pb_ratio']}</td></tr>
                <tr><td>殖利率</td><td>{stock_data['dividend_yield']:.2f}%</td></tr>
                <tr><td>52週最高</td><td>${stock_data['fiftyTwoWeekHigh']}</td></tr>
                <tr><td>52週最低</td><td>${stock_data['fiftyTwoWeekLow']}</td></tr>
                <tr><td>近30天變化</td><td class="{'positive' if stock_data['price_change_pct'] >= 0 else 'negative'}">{stock_data['price_change_pct']:+.2f}%</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h2>🤖 AI 分析報告</h2>
            <div class="analysis">
                {analysis_text.replace(chr(10), '<br>')}
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>本報告由 FinRobot 使用 Google Gemini 2.0 Flash 生成</p>
        <p>⚠️ 免責聲明: 本報告僅供參考，不構成投資建議</p>
    </div>
</body>
</html>
"""
    
    def _create_comparison_body(self, tickers, stocks_data, analysis_text):
        """建立多股票比較報告內容"""
        # 建立比較表格
        rows = ""
        for data in stocks_data:
            change_class = "positive" if data['price_change_pct'] >= 0 else "negative"
            rows += f"""
                <tr>
                    <td><strong>{data['ticker']}</strong></td>
                    <td>{data['name']}</td>
                    <td>${data['currentPrice']:.2f}</td>
                    <td>{data['pe_ratio']}</td>
                    <td>${data['marketCap']:,.0f}</td>
                    <td class="{change_class}">{data['price_change_pct']:+.2f}%</td>
                </tr>
            """
        
        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .header {{ background-color: #2196F3; color: white; padding: 20px; text-align: center; }}
        .content {{ padding: 20px; }}
        .section {{ margin-bottom: 20px; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        .data-table th {{ background-color: #f2f2f2; padding: 10px; text-align: left; border: 1px solid #ddd; }}
        .data-table td {{ padding: 10px; border: 1px solid #ddd; }}
        .analysis {{ background-color: #f9f9f9; padding: 15px; border-left: 4px solid #2196F3; margin: 15px 0; }}
        .footer {{ text-align: center; color: #666; font-size: 12px; padding: 20px; border-top: 1px solid #ddd; }}
        .positive {{ color: #4CAF50; font-weight: bold; }}
        .negative {{ color: #f44336; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 多股票比較分析報告</h1>
        <p>{", ".join(tickers)}</p>
        <p>{datetime.now().strftime('%Y年%m月%d日 %H:%M')}</p>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>股票比較表</h2>
            <table class="data-table">
                <tr>
                    <th>代號</th>
                    <th>公司名稱</th>
                    <th>價格</th>
                    <th>P/E</th>
                    <th>市值</th>
                    <th>30天變化</th>
                </tr>
                {rows}
            </table>
        </div>
        
        <div class="section">
            <h2>🤖 AI 比較分析</h2>
            <div class="analysis">
                {analysis_text.replace(chr(10), '<br>')}
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>本報告由 FinRobot 使用 Google Gemini 2.0 Flash 生成</p>
        <p>⚠️ 免責聲明: 本報告僅供參考，不構成投資建議</p>
    </div>
</body>
</html>
"""
    
    def _send_email(self, subject, body):
        """發送 HTML 格式郵件"""
        # 建立郵件物件
        message = MIMEMultipart('alternative')
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = subject
        
        # 加入 HTML 內容
        html_part = MIMEText(body, 'html', 'utf-8')
        message.attach(html_part)
        
        # 發送郵件
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()  # 啟用 TLS 加密
            server.login(self.sender, self.password)
            server.send_message(message)


def test_email_service():
    """測試郵件服務"""
    service = EmailService()
    
    print("=== 郵件服務測試 ===")
    print(f"郵件功能啟用: {service.is_enabled()}")
    
    if service.is_enabled():
        print(f"設定狀態: {'✅ 完整' if service.is_configured() else '❌ 不完整'}")
        print(f"SMTP 伺服器: {service.smtp_server}:{service.smtp_port}")
        print(f"發送者: {service.sender}")
        print(f"接收者: {service.receiver}")
        
        if service.is_configured():
            print("\n📧 發送測試郵件...")
            test_data = {
                'ticker': 'TEST',
                'name': 'Test Company',
                'sector': 'Technology',
                'industry': 'Software',
                'currentPrice': 100.50,
                'marketCap': 1000000000,
                'pe_ratio': 25.5,
                'pb_ratio': 3.2,
                'dividend_yield': 1.5,
                'fiftyTwoWeekHigh': 120.0,
                'fiftyTwoWeekLow': 80.0,
                'price_change_pct': 5.2
            }
            service.send_analysis_report('TEST', test_data, '這是測試分析報告內容。')
    else:
        print("郵件功能未啟用（ENABLE_EMAIL=false）")


if __name__ == "__main__":
    test_email_service()
