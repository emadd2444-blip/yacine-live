import requests
import json

def main():
    bot_results = []
    
    # قائمة المصادر العملاقة (قنوات عربية + أفلام + مسلسلات)
    sources = [
        # 1. قنوات عربية مفتوحة مستقرة جداً (الجزيرة، MBC، إلخ)
        {"url": "https://iptv-org.github.io/iptv/languages/ara.json", "type": "live"},
        
        # 2. مكتبة أفلام متنوعة (تحديث مستمر من GitHub)
        {"url": "https://raw.githubusercontent.com/TheBeastApps/Lists/master/Movies.json", "type": "movie"},
        
        # 3. مكتبة مسلسلات وأفلام كرتون
        {"url": "https://raw.githubusercontent.com/man-of-war/yacine-api/main/vod.json", "type": "movie"}
    ]
    
    print("🚀 جاري صيد المكتبة الشاملة لعيون عاصم...")
    for src in sources:
        try:
            res = requests.get(src['url'], timeout=15)
            if res.status_code == 200:
                data = res.json()
                # التعامل مع أنواع البيانات المختلفة (List أو Dict)
                items = data if isinstance(data, list) else data.get('movies', data.get('data', []))
                
                for item in items:
                    name = item.get('name') or item.get('title')
                    url = item.get('url') or item.get('link')
                    if name and url:
                        bot_results.append({
                            "name": name,
                            "url": url,
                            "img": item.get('logo') or item.get('poster') or 'https://via.placeholder.com/150/111/00d2ff?text=ASIM+TV',
                            "type": src['type']
                        })
        except: continue

    # حفظ كل شيء في ملف واحد
    with open('bot_data.json', 'w', encoding='utf-8') as f:
        json.dump(bot_results, f, ensure_ascii=False, indent=4)
    print(f"✅ مبروك! صيد اليوم: {len(bot_results)} مادة ترفيهية.")

if __name__ == "__main__":
    main()
