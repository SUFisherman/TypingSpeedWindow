#-*- coding: utf-8 -*- #
import pythoncom
import pyHook
import globalVariable
import time
import wx

'''COUNT=0
def globalVariable():
    global COUNT
    return'''

app = wx.App()  # 创建对象
win = wx.Frame(None,title="speed", size=(410,340))  #创建窗口对象
spBut=wx.Button(win, pos = (5,5), size=(10,10)) #创建按钮1对象
win.Show()


def keywatcher(event):
    globalVariable.COUNT+=1
    if (time.time() - globalVariable.LT >= 2):
        out()
        globalVariable.COUNT = 0
        globalVariable.LT = time.time()
    return True

def out():
    spBut.SetLabelText(str(globalVariable.COUNT))#注意，这里的set……是一个消息事件,而添加新按钮则不是消息事件
    print  globalVariable.COUNT
    return  str(globalVariable.COUNT)


if __name__=="__main__":
    hook=pyHook.HookManager()
    hook.KeyDown=keywatcher
    hook.HookKeyboard()
    pythoncom.PumpMessages()
