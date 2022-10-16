import requests
from bs4 import BeautifulSoup
import savePics

def _getArticles(myUrl):  # 傳入的網址存放在[urL]
    global timeS  # 在函式(區域)內，要更改全域變數的值，必須先宣告其為[global]
    rQ = requests.get(myUrl).text  # 模擬送出cookies的驗證值
    souP = BeautifulSoup(rQ, "html5lib")
    for articleDiv in souP.find_all("div", {"data-click-id": "body"}):
        try:
            linkA = articleDiv.find("a", {"data-click-id": "body"})
            # print("https://www.reddit.com"+linkA["href"])
            titleH3 = linkA.find("h3")
            try:
                titleSpan = titleH3.find("span")
                titleSpanText = titleSpan.text
                titleSpan.replace(titleSpanText)
            except:
                print()

            theUrl = "https://www.reddit.com" + \
                 articleDiv.find("a", {"data-click-id": "body"})["href"]
            titlE = titleH3.text.strip()
            savePics._shootingPic(theUrl)
        except:
            continue
    return  # 傳回[上頁]文章的網址
