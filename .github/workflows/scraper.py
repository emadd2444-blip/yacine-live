import requests
import json

def fetch_yacine_links():
    # هذا مصدر جديد وقوي جداً وتحديثه تلقائي
    url = "https://raw.githubusercontent.com/Fm-Live/Yacine-TV-API/main/yacine.json"
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            return response.json()
    except:
        return None

data = fetch_yacine_links()

if data and isinstance(data, dict) and len(data) > 0:
    with open('channels.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم صيد القنوات بنجاح!")
else:
    # إذا فشل، لا تحفظ ملفاً تالفاً
    print("❌ فشل الصيد، المصدر قد يكون متوقف.")
