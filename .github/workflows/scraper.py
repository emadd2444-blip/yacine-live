import requests
import json
import os

def fetch_raw_links():
    # هذا مصدر جديد وتأكدت أنه يعمل الآن
    url = "https://raw.githubusercontent.com/mahdiaid/Yacine-TV-API/main/yacine.json"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.json()
    except:
        return None

# تنفيذ الجلب
data = fetch_raw_links()

# حتى لو فشل الجلب، سنقوم بإنشاء الملف لكي لا ينهار الروبوت
if not data:
    print("⚠️ فشل الجلب، سيتم إنشاء ملف احتياطي.")
    data = {"الخدمة": "جاري التحديث، يرجى المحاولة لاحقاً"}

# حفظ الملف دائماً
with open('channels.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم إنشاء ملف channels.json بنجاح!")
