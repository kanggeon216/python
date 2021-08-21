from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("500x500")
win.title("로또")

ent = Entry(win)
ent.pack()

def lotto_p():
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    txt = soup.find("div", attrs = {"class","win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]

    print("당첨번호")
    print(num_list)
    print("보너스번호")
    print(bonus)

btn = Button(win)
btn.config(text = "lotto")
btn.config(command = lotto_p)
btn.pack()

win.mainloop()