import requests
import json

def main():
    bot_results = []
    # مصادر القنوات والأفلام
    sources = [
        "https://iptv-org.github.io/iptv/languages/ara.json",
        "https://raw.githubusercontent.com/yacine-tv/api/main/vod.json"
    ]
    
    for url in sources:
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                data = res.json()
                if isinstance(data, list):
                    for item in data:
                        bot_results.append({
                            "name": item.get('name', 'بدون اسم'),
                            "url": item.get('url', ''),
                            "img": item.get('logo', 'https://via.placeholder.com/300x450/111/00d2ff?text=ASIM+TV'),
                            "type": "live" if "languages" in url else "movie"
                        })
        except: continue

    with open('bot_data.json', 'w', encoding='utf-8') as f:
        json.dump(bot_results, f, ensure_ascii=False, indent=4)
    print("Done!")

if __name__ == "__main__":
    main()
