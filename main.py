import os
import requests
import time
from datetime import datetime
from zoneinfo import ZoneInfo

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("WEBHOOK_URL not set")

ROLE_TAG = "<@&1498680118565011498>"

colors = {
    "📦 Air Drop": 3447003,
    "🏪 งัดร้าน": 16776960,
    "🦌 บอส": 15158332
}

schedule = {
    "08:30": "📦 Air Drop",
    "10:45": "🏪 งัดร้าน",
    "11:30": "📦 Air Drop",
    "14:30": "📦 Air Drop",
    "15:45": "🏪 งัดร้าน",
    "16:30": "📦 Air Drop",
    "17:15": "🦌 บอส",
    "18:30": "📦 Air Drop",
    "19:45": "🏪 งัดร้าน",
    "20:15": "🦌 บอส",
    "21:30": "📦 Air Drop",
    "22:45": "🏪 งัดร้าน",
    "23:15": "🦌 บอส",
    "00:30": "📦 Air Drop",
    "02:30": "📦 Air Drop",
    "04:45": "🏪 งัดร้าน",
    "05:30": "📦 Air Drop",
}

def send(event, time_now):
    color = colors.get(event, 16777215)

    data = {
        "content": ROLE_TAG,
        "embeds": [
            {
                "title": "🔔 แจ้งเตือนกิจกรรม : ลงมาเล่นกันด้วย",
                "description": f"🏆 กิจกรรม : {event}\n⏰ เวลา : {time_now}",
                "color": color,
                "footer": {
                    "text": "Extreme City : Bot By. Zens"
                }
            }
        ]
    }

    try:
        r = requests.post(WEBHOOK_URL, json=data, timeout=5)
        print(f"[OK] {event} {time_now} | {r.status_code}")
    except Exception as e:
        print("[ERROR]", e)

sent_today = set()

print("✅ Bot started...")

while True:
    try:
        now = datetime.now(ZoneInfo("Asia/Bangkok")).strftime("%H:%M")

        if now == "07:00":
            sent_today.clear()
            print("🔄 Reset sent list")

        if now in schedule and now not in sent_today:
            send(schedule[now], now)
            sent_today.add(now)

        time.sleep(20)

    except Exception as e:
        print("Loop Error:", e)
        time.sleep(10)
