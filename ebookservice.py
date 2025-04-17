import requests
from bs4 import BeautifulSoup

# 台灣雲端書庫@新北市
url = "https://www.ebookservice.tw/nt/category/TCL320"  # 替換為您要抓取的網站 URL
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
