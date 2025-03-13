import requests

response = requests.get("https://www.example.com")
# response = requests.get("https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")

if response.status_code == 200:
    # print("成功取得網頁內容")
    print(response.text)
else:
    # print(f"無法取得網頁內容，狀態碼：{response.status_code}")
    #print()
