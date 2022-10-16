import requests
from bs4 import BeautifulSoup
import os  # 建立新資料夾與其他目錄相關的處理
import urllib  # 存檔用

myHead = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

def _shootingPic(picUrl):  # 傳入圖片文章連結網址與文章標題
    rqPic = requests.get(picUrl, headers=myHead).text  # 模擬送出cookies的驗證值
    soupPics = BeautifulSoup(rqPic, "html5lib")

    print("---------------------------------------------")

    contentDiv = soupPics.find("div", {"data-test-id": "post-content"})
    contenUl = contentDiv.find("ul")
    if contenUl != None:
        for soupPic in contenUl.find_all("li"):
            try:
                fullPath = soupPic.find("a")["href"]
                picName = fullPath.split("/")[-1]
                picName = picName.split("?")[0]

                if os.path.isfile(picName):  # 判斷圖片檔案是否已經存在，若不存在才做存檔的動作
                    print("檔案已經存在!!!")
                else:
                    urllib.request.urlretrieve(
                        fullPath, picName)  # 圖片存檔
            except:
                continue
    else:
        try:
            fullPath = contentDiv.find(
                "a", {"rel": "noopener noreferrer"})["href"]
            picName = fullPath.split("/")[-1]
            picName = picName.split("?")[0]
            #picName = titilE + "-" + str(nN) + ".jpg"
            if os.path.isfile(picName):
                print("檔案已經存在!!!")
            else:
                urllib.request.urlretrieve(fullPath, picName)
        except:
            pass
