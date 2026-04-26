import json

def uploaddata(nickname, link, description):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    data["users"].append({
        "nickname": nickname,
        "website": link,
        "description": description
    })

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)