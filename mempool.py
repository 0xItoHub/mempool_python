import requests
from bs4 import BeautifulSoup
import schedule
import time

def fetch_top_addresses():
    url = "https://www.mempool.space"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 仮のセレクタ例。実際にはmempoolのHTML構造に基づいて調整する必要があります。
    addresses = soup.select('div.some-class-for-address')
    balances = soup.select('div.some-class-for-balance')
    
    top_addresses = []
    for address, balance in zip(addresses, balances):
        top_addresses.append({
            "address": address.text.strip(),
            "balance": balance.text.strip()
        })
    
    print("Top 10 BTC Addresses:")
    for i, address_info in enumerate(top_addresses[:10], start=1):
        print(f"{i}: {address_info['address']} - {address_info['balance']} BTC")

# 毎日9時に実行するスケジュール設定
schedule.every().day.at("09:00").do(fetch_top_addresses)

# 無限ループでスケジュールを待機
while True:
    schedule.run_pending()
    time.sleep(1)
