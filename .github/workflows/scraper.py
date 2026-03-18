import requests
import json
import os

# دالة لجلب الروابط من مصدر عام محدث (مؤقتاً لضمان النجاح)
def fetch_raw_links():
    # هذا الرابط يُحدث باستمرار من قبل مجتمعات الـ IPTV
    url = "https://raw.githubusercontent.com/man-of-war/yacine-api/main/live.json"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

# تنفيذ الجلب
data = fetch_raw_links()

if data:
    # حفظ البيانات في ملف channels.json داخل GitHub
    with open('channels.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم صيد الروابط بنجاح وحفظها في channels.json!")
else:
    print("❌ فشل صيد الروابط.")
