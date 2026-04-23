import httpx

sites = [
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.linkedin.com/in/",
    "https://www.youtube.com/@",
    "https://www.tiktok.com/@"
]

def checknickname():
    nickname = input("Write your nickname: ")
    found = []

    for site in sites:
        url = site + nickname
        try:
            r = httpx.get(url, timeout=5)

            if r.status_code == 200:
                print(f"[+] Found: {url}")
                found.append(url)
            else:
                print(f"[-] Not found on {site}")

        except httpx.RequestError:
            print(f"[!] Error connecting to {site}")

    return found

result = checknickname()
print("\nSummary:", result)