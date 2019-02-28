#coding:utf-8



import win32clipboard as w


import win32con


def gettext():

    w.OpenClipboard()

    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()

    return t

#print(gettext())
