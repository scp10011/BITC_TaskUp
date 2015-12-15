#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,text,LandFunction,NetworkFunction,CopyProcessing
import random
import getpass
import string
import time
import re
import os
import sys
import msvcrt
import urllib
import urllib2
import cookielib
import multiprocessing
import win32ui,win32api,win32con
from bs4 import BeautifulSoup
from text import *
from time import sleep

def qk():
    os.system('cls')
    logtext()
def logtext():
    print log[0]
    print log[1]
    print log[2]
    print log[3]
    print log[4]
    print log[5]

def uptk():
    cookie = NetworkFunction.Cookie()
    qk()
    while 1:
        flag = False
        if open('cookie.txt','r').read() != '':
            if InputFunction.inputyn(37):
                cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
                qk()
                flag = True
                print log[58]
                break
        username,password = LandFunction.inuserlog(flag)
        
        if not username and not password :
            print log[53]
            open('Land','w').close()
            continue
        else :
            print log[15]
            LogFlag,Code = NetworkFunction.Login(username,password)
            if not LogFlag and Code==200:
                qk()
                print log[38]
                open('cookie.txt','w').close()
                open('Land','w').close()
                time.sleep(2)
                continue
            elif LogFlag and Code==200:
                qk()
                print log[17]
                break
            else :
                qk()
                print log[39]
                time.sleep(2)
                continue
    cookie.save(ignore_discard=True, ignore_expires=True)
    while 1:
        Uuid = NetworkFunction.UUID()
        DataProcessing_ = NetworkFunction.UuidData(Uuid)
        
        qk()
        print('%-5s%-5s%-5s%-45s%-20s' % (log[21],log[26],log[20],log[18],log[19]))
        l = 0
        chooseCourse = {'1':log[24],'0':log[25]}
        for i in DataProcessing_:
            l+=1
            print('%-5s%-5s%-5s%-45s%-20s' % (str(l).center(5),chooseCourse.get(i[5]) ,str(i[2]).decode("utf-8").encode('gbk').center(5) ,i[3].decode("utf-8").encode('gbk') ,i[4].decode("utf-8").encode('gbk')))
        print('%-5s%-20s' % (str(l+1).center(5),log[56].center(20)))
        print('%-5s%-20s' % ('0'.center(5),log[29].center(20)))
        cla = InputFunction.inputsn(22,len(DataProcessing_)+1)
        if cla == -1:
            break
        elif cla == l:
            qk()
            print log[58]
            Already = 0
            NotTask = 0
            for CourseNumber in range(0, (len(DataProcessing_)-1) + 1):
                CourseList = NetworkFunction.course(DataProcessing_[CourseNumber][0],DataProcessing_[CourseNumber][1])
                Already += int(CourseList[0])
                NotTask += int(CourseList[1])
            print log[54],Already,log[55],NotTask
            print log[57]
            msvcrt.getch()
            qk()
            continue
        TaskProcessing_ = NetworkFunction.task(DataProcessing_[cla][0],DataProcessing_[cla][1],Uuid)
        qk()
        print('%-5s%-5s%-45s' % (log[21],log[47],log[27]))
        l=0
        for i in TaskProcessing_:
            l+=1
            flag = ''
            if i[4] == '1':
                print('%-5s%-5s%-45s' % (l,log[48] ,i[1].decode("utf-8").encode('gbk')))
            elif i[4] == '0' and i[5] == '1':
                print('%-5s%-5s%-45s' % (l,log[50] ,i[1].decode("utf-8").encode('gbk')))
            elif i[4] == '0' and i[5] == '0':
                print('%-5s%-5s%-45s' % (l,log[49] ,i[1].decode("utf-8").encode('gbk')))
        print('%-5s%-5s' % ('0',log[28]))
        Task = InputFunction.inputsn(23,len(TaskProcessing_))
        if Task == -1:
            continue
        dlg = win32ui.CreateFileDialog(1)
        dlg.SetOFNInitialDir('C:\Users')
        dlg.DoModal()
        filename = dlg.GetPathName()
        if filename=='':
            print log[30]
            FileName = ''
        else:
            FileName = NetworkFunction.Upfile(filename)
        text = ''
        text = raw_input(log[31])
        x = NetworkFunction.UpTask(Uuid,TaskProcessing_[Task][2],TaskProcessing_[Task][3],text,FileName)
        if x[0][1] == 'SUCCESS' and x[2][1] == 'true' and x[3][1] == 'SUCCESS':
            qk()
            print log[41]
            time.sleep(2)
        else :
            qk()
            print x[3][1].decode("utf-8").encode('gbk')
            time.sleep(2)
        cookie.save(ignore_discard=True, ignore_expires=True)
    qk()
    
def copy():
    while 1:
        flag = False
        print log[42]
        oneusername,onepassword = LandFunction.inuserlog(flag)
        print log[43]
        twousername,twopassword = LandFunction.inuserlog(flag)
        textqueue = multiprocessing.Queue()
        copylandAPlay = multiprocessing.Process(target=CopyProcessing.copylandA, args=(oneusername,onepassword,textqueue,))
        copylandBPlay = multiprocessing.Process(target=CopyProcessing.copylandB, args=(twousername,twopassword,textqueue,))
        #copyProcessing = multiprocessing.Process(target=CopyProcessing.CopyProcessing, args=(textqueue,))
        copylandAPlay.start()
        copylandBPlay.start()
        CopyProcessing.CopyProcessing(textqueue)
        
        copylandAPlay.join()
        msvcrt.getch()
        

def down():
    print 'down'
def Endr():
    sys.exit()

def Processing(TaskInList):
    TaskUpList = []
    for i in TaskInList:
        clas = str(i-100)[0:1]
        task = str(i-1)[1:3]
        TaskUp  = clas,task
        TaskUpList.append(TaskUp)
    return TaskUpList
if __name__ == '__main__':
    
    while 1:
        qk()
        print('%-5s%-5s' % (log[21],log[36]))
        for i in range(1, 3 + 1):
            print('%-5s%-5s' % (i,log[99+i]))
        print('%-5s%-5s' % (0,log[29]))
        Options = {0:uptk,1:copy,2:down,-1:Endr}
        Option = InputFunction.inputsn(32,3)
        Options.get(Option)()
    


    

