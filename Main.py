
import tkinter as tk
import tkinter.messagebox
import os  # 建立新資料夾與其他目錄相關的處理
import sys
from searchReddit import _getArticles
from PIL import Image, ImageTk

pics = []
current = -1
currentWorkingDir = os.getcwd()

def execPathAdaptor():
    global currentWorkingDir
    application_path = ""
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.executable)
        currentWorkingDir = os.path.dirname(sys.argv[0])
        os.chdir(application_path)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(application_path)


def resetList():
    os.chdir(currentWorkingDir)
    global current
    current = -1


def _entKeyword():
    resetList()
    keyWord = entKeyword.get()
    url = "https://www.reddit.com/r/shootingcars/search/?q=" + keyWord
    newDir = "Find Result/" + keyWord

    try:  # 先判斷目錄是否存在，若不存在才建立新目錄
        os.makedirs(str(newDir))
    except FileExistsError:
        print("目錄已經存在!!!")

    os.chdir(newDir + "/")  # 切換到新建的目錄底下
    url = _getArticles(url)  # [_getArticles()]是我們的自訂函式，用來處理網頁資料抓取
    global pics
    pics = [p for p in os.listdir('.')]
    changePic(1)


def changePic(flag):
    '''flag=-1表示上一個，flag=1表示下一個'''
    global current
    new = current + flag
    if new<0:
        tkinter.messagebox.showerror('', '這已經是第一張圖片了')
    elif new>=len(pics):
        tkinter.messagebox.showerror('', '這已經是最後一張圖片了')
    else:
        
        pic = pics[new]
        im = Image.open(pic)
        w, h = im.size
        if w>400:
            h = int(h*400/w)
            w = 400
        if h>600:
            w = int(w*600/h)
            h = 600
        im = im.resize((w,h))
        im1 = ImageTk.PhotoImage(im)
        lbPic['image'] = im1
        lbPic.image = im1
        current = new

def btnPreClick():
    changePic(-1)

def btnNextClick():
    changePic(1)



wiN = tk.Tk()
wiN.title("Find Your Dream Car")
wiN.geometry("600x500+250+100")

lblKeyword = tk.Label(wiN, text="Please enter your dream car's keyword",
                      fg="white", bg="green", font=("Arial", 16), width=50, height=3)
lblKeyword.pack()

entKeyword = tk.Entry(wiN, font=("Arial", 16), bd=5)
entKeyword.pack()

btnSearch = tk.Button(wiN, text="Search Image", fg="green", font=(
    "Arial", 16), width=10, height=2, command= _entKeyword)
btnSearch.pack()


btnPre = tkinter.Button(wiN, text='上一張', command=btnPreClick)
btnPre.place(width=80, height=30)
btnPre.pack()

btnNext = tkinter.Button(wiN, text='下一張', command=btnNextClick)
btnNext.place(width=80, height=30)
btnNext.pack()

lbPic = tkinter.Label(wiN, text='preView', width=400, height=600)
lbPic.place(width=400, height=600)
lbPic.pack()

entKeyword.focus()
execPathAdaptor()
wiN.mainloop()
