"""
Helpful links:

Krakenex:
    https://github.com/veox/python3-krakenex/

Sqlite3:
    https://docs.python.org/3/library/sqlite3.html
"""
import requests
import sqlite3
import time

import krakenex


coins = {
        "bitcoin": "XBTCZUSD",
        "eth": "XETHZUSD",
        "litecoin": "XLTCZUSD"
}

kraken = krakenex.API()

conn = sqlite3.connect('file.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS coindata (name text, price real)')
conn.commit()

def main():
    while True:
        for coin in coins:
            try:
                data = kraken.query_public('OHLC', data = {'pair': coins[coin], 'since': time.time()})
                c.execute('INSERT INTO coindata VALUES (coin, float(data["result"][coins[coin]][0][1]))')  
                time.sleep(60)
                print("sleeping...")
            except: 
               print("Failed to collect data, retrying")

if __name__ == "__main__":
    main()
