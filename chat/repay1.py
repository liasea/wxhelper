# -*-encoding:utf-8-*-

import itchat
from tkinter import *
from multiprocessing import Process

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

def openLogin(arg):
    mainWindow = Tk()
    mainWindow.title("微信机器人")
    photo = PhotoImage(file='C:\\login.png')
    label = Label(mainWindow, image=photo)
    label.pack()
    mainWindow.mainloop()

def run_proc(name):
    mainWindow = Tk()
    mainWindow.title("微信机器人")
    photo = PhotoImage(file='C:\\login.png')
    label = Label(mainWindow, image=photo)
    label.pack()
    mainWindow.mainloop()

if __name__=='__main__':
    p = Process(target=openLogin, args=('test',))
    p.start()
    itchat.auto_login(picDir="C:\\login.png", hotReload=True)
    # itchat.auto_login(qrCallback=qrHandler)
    # p = Process(target=run_proc, args=('test',))

    itchat.run()