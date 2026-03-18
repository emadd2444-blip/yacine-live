import requests
import json

def main():
    bot_results = []
    # مصادر متنوعة وشاملة (أفلام، مسلسلات، قنوات عربية)
    sources = [
        {"url": "https://iptv-org.github.io/iptv/languages/ara.json", "type": "live"},
        {"url": "https://raw.githubusercontent.com/yacine-tv/api/main/vod.json", "type": "movie"},
        {"url": "https://raw.githubusercontent.com/TheBeastApps/Lists/master/Movies.json", "type": "movie"}
    ]
    
    print("جاري صيد المكتبة الضخمة...")
    for src in sources:
        try:
            res = requests.get(src['url'], timeout=15)
            if res.status_code == 200:
                data = res.json()
                items = data if isinstance(data, list) else data.get('movies', [])
                for item in items:
                    bot_results.append({
                        "name": item.get('name') or item.get('title', 'بدون اسم'),
                        "url": item.get('url') or item.get('link', ''),
                        "img": item.get('logo') or item.get('poster') or 'https://via.placeholder.com/300x450/111/00d2ff?text=ASIM+PRO',
                        "type": src['type']
                    })
        except: continue

    with open('bot_data.json', 'w', encoding='utf-8') as f:
        json.dump(bot_results, f, ensure_ascii=False, indent=4)
    print("Done!")

if __name__ == "__main__":
    main()
