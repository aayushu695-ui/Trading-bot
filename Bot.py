import time
import requests
import os
from datetime import datetime

class DeltaTradingBot:
    def __init__(self):
        self.api_key = os.getenv('DELTA_API_KEY')
        self.secret_key = os.getenv('DELTA_SECRET_KEY')
        
    def start_bot(self):
        print("🚀 Trading Bot Started!")
        while True:
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"✅ Bot Running... {current_time}")
                time.sleep(60)
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(30)

if __name__ == "__main__":
    bot = DeltaTradingBot()
    bot.start_bot()
