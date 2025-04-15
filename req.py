import requests

url = "https://books.toscrape.com/"
# url = "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
response = requests.get(url)
response.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

if response.status_code == 200:
    print("成功取得網頁內容")
    print(response.text)
else:
    print(f"無法取得網頁內容，狀態碼：{response.status_code}")
    # print()
