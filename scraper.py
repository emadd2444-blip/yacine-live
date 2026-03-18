import requests
import json

def fetch_yacine_sports():
    # قائمة المصادر الموثوقة التي توفر روابط ياسين تيفي الرياضية حالياً
    sources = [
        "https://raw.githubusercontent.com/rabilmgh/Yacine-TV-API/main/yacine.json",
        "https://raw.githubusercontent.com/Fm-Live/Yacine-TV-API/main/yacine.json",
        "https://raw.githubusercontent.com/Ashraf7mod/yacine-tv-api/main/channels.json"
    ]
    
    for url in sources:
        try:
            print(f"جاري فحص مصدر الرياضة: {url}")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    return data
        except:
            continue
    return {}

def main():
    # 1. جلب الرياضية أولاً (الأولوية القصوى)
    sports_channels = fetch_yacine_sports()
    
    # 2. جلب القنوات المفتوحة (كإضافة لكي لا يكون الموقع فارغاً)
    open_channels = {}
    try:
        res = requests.get("https://iptv-org.github.io/iptv/languages/ara.json", timeout=10)
        if res.status_code == 200:
            for ch in res.json():
                name, url = ch.get('name'), ch.get('url')
                if name and url:
                    open_channels[name] = url
    except:
        pass

    # 3. دمج القنوات (الرياضية تظهر أولاً)
    # نستخدم قاموس جديد يضع الرياضية في البداية
    final_list = {}
    final_list.update(sports_channels)
    
    # إضافة القنوات المفتوحة التي لا توجد في قائمة الرياضة
    for name, url in open_channels.items():
        if name not in final_list:
            final_list[name] = url

    # 4. الحفظ في ملف channels.json
    if final_list:
        with open('channels.json', 'w', encoding='utf-8') as f:
            json.dump(final_list, f, ensure_ascii=False, indent=4)
        print(f"✅ مبروك! تم جلب {len(sports_channels)} قناة رياضية ومئات القنوات المفتوحة.")
    else:
        print("❌ فشل جلب أي قنوات.")

if __name__ == "__main__":
    main()
