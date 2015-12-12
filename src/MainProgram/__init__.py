#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,text,LandFunction,NetworkFunction
import random
import getpass
import string
import time
import re
import os
import sys
import urllib
import urllib2 
import cookielib
import win32ui,win32api,win32con
from bs4 import BeautifulSoup
from text import *

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
    qk()
    while 1:
        flag = False
        if open('cookie.txt','r').read() != '':
            if InputFunction.inputyn(37):
                NetworkFunction.cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
                qk()
                flag = True
                break
        username,password = LandFunction.inuserlog(flag)
        if not username and not password :
            print log[40]
        else :
            print log[15]
            LogFlag,Code = NetworkFunction.Login(username,password)
            if not LogFlag and Code==200:
                qk()
                print log[38]
                open('cookie.txt','w').truncate()
                open('cookie.txt','w').close()
                open('Land','w').truncate()
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
    NetworkFunction.cookie.save(ignore_discard=True, ignore_expires=True)
    while 1:
        Uuid = NetworkFunction.UUID()
        Data = NetworkFunction.UuidData(Uuid)
        DataProcessing_ = NetworkFunction.DataProcessing(Data)
        qk()
        print('%-5s%-5s%-45s%-20s' % (log[21],log[20],log[18],log[19]))
        l = 0
        for i in DataProcessing_:
            l+=1
            print('%-5s%-5s%-45s%-20s' % (l,i[2].decode("utf-8").encode('gbk') ,i[3].decode("utf-8").encode('gbk') ,i[4].decode("utf-8").encode('gbk')))
        print('%-5s%-5s' % ('0',log[29]))
        cla = InputFunction.inputsn(22,len(DataProcessing_))
        if cla == -1:
            break
        CourseList = NetworkFunction.course(DataProcessing_[cla][0],DataProcessing_[cla][1])
        task_ = NetworkFunction.task(DataProcessing_[cla][0],DataProcessing_[cla][1],Uuid)
        TaskProcessing_ = NetworkFunction.TaskProcessing(task_)
        qk()
        print('%-5s%-5s%-45s' % (log[21],log[26],log[27]))
        l=0
        for i in TaskProcessing_:
            l+=1
            flag = ''
            if i[4] == '1':
                print('%-5s%-5s%-45s' % (l,log[24] ,i[1].decode("utf-8").encode('gbk')))
            else:
                print('%-5s%-5s%-45s' % (l,log[25] ,i[1].decode("utf-8").encode('gbk')))
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
        NetworkFunction.cookie.save(ignore_discard=True, ignore_expires=True)
    qk()
    
def copy():
    def logA(username,password):
        while 1:
            print log[15]
            LogFlag,Code = NetworkFunction.Login(username,password)
            if not LogFlag and Code==200:
                qk()
                print log[38]
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
        while 1:
            fomart = 'abcdefghijklmnopqrstuvwxyz0123456789^$.*+-?=!:|\/()[]{} '
            Uuid = NetworkFunction.UUID()
            Data = NetworkFunction.UuidData(Uuid)
            DataProcessing_ = NetworkFunction.DataProcessing(Data)
            tasklist = []
            lenlist = []
            TaskProcessing_ = []
            di = 0
            PrintDataProcessing_ = DataProcessing_[:]
            for i in range(0, (len(DataProcessing_)-1) + 1):
                task_ = NetworkFunction.task(DataProcessing_[i][0],DataProcessing_[i][1],Uuid)
                TaskProcessing_ = NetworkFunction.TaskProcessing(task_)
                if TaskProcessing_ != []:
                    tasklist.append(TaskProcessing_)
                else :
                    del PrintDataProcessing_[i-di]
                    di+=1
                lenlist.append(len(TaskProcessing_))
            colsTEXT = len(PrintDataProcessing_)*27
            os.system('mode con cols=%s lines=50'%colsTEXT)
            TaskInList = []
            while 1:
                TaskIdList = []
                qk()
                print log[44]
                for l in PrintDataProcessing_:
                    PrintData = str(l[3].decode("utf-8").encode('gbk'))[0:14].center(16)
                    PrintData = PrintData.lower()
                    qweData = 0
                    for c in PrintData:
                        if c in fomart:
                            qweData+=1
                    if qweData%2 == 0:
                        lens = 14
                    else :
                        lens = 13
                    print('%-5s%-16.16s%-4s' % (log[46].center(5),str(l[3].decode("utf-8").encode('gbk'))[0:lens].center(16),log[47].center(4))),
                print ''
                for li in range(0, (max(lenlist)-1) + 1):
                    for ll in range(0, (len(DataProcessing_)-1) + 1):
                        try:
                            PrintData = str(tasklist[ll][li][1].decode("utf-8").encode('gbk'))[0:14].center(16)
                            PrintData = PrintData.lower()
                            qweData = 0
                            for c in PrintData:
                                if c in fomart:
                                    qweData+=1
                                    if qweData%2 == 0:
                                        lens = 14
                                    else :
                                        lens = 13
                            if tasklist[ll][li][1] != '':
                                TaskIdList.append((ll+1)*100+li+1)
                            print ('%-5s%-16.16s%-4s' % (str(((ll+1)*100+li+1)).center(5),str(tasklist[ll][li][1].decode("utf-8").encode('gbk'))[0:lens].center(16),''.center(4))),
                        except:
                            print ('%-5s%-16.16s%-4s' % (''.center(5),"".center(20),''.center(4))),
                    print ''    
                TaskIn = InputFunction.inputln(45, TaskIdList)
                if TaskIn:
                    TaskInList.append(TaskIn)
                else :
                    print log[52],TaskInList
                    time.sleep(3)
                    TaskUpList = Processing(TaskInList)
                    break
            break
        return TaskUpList
        

    while 1:
        flag = False
        print log[42]
        oneusername,onepassword = LandFunction.inuserlog(flag)
        #oneusername,onepassword = LandFunction.ins()
        #print log[43]
        #twousername,twopassword = LandFunction.ins()
        TaskUpList = logA(oneusername,onepassword)

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
    


    

