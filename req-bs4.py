from bs4 import BeautifulSoup

html_content = """
<html>
    <head><title>這一個網頁標題，網路爬蟲能找到我哈哈哈笑死</title></head>
    <body>
        <h1>這是主標題</h1>
        <p>這是一個段落。</p>
        <a href="https://www.example.com">這是一個連結</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string
print(f"網頁標題：{title}")
