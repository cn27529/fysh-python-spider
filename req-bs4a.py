import requests
from bs4 import BeautifulSoup

# url = "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
url = "https://books.toscrape.com/"  # 替換為您要抓取的網站 URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    print(f"網頁標題：{title}")
    print("所有連結：")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)
else:
    print(f"無法取得網頁內容，狀態碼：{response.status_code}")
