#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,NetworkFunction
import time,os
import cookielib
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

def copylandA(username,password,textqueue):
    NetworkFunction.CopyCookie()
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
        Uuid = NetworkFunction.UUID()
        DataProcessing_ = NetworkFunction.UuidData(Uuid)
        if DataProcessing_ == '':
            continue
        tasklist = []
        lenlist = []
        TaskProcessing_ = []
        DataProcessing = []
        di = 0
        for i in DataProcessing_:
            print 
            if i[5] == '0':
                DataProcessing.append(i)
        PrintDataProcessing_ = DataProcessing[:]
        for i in range(0, (len(DataProcessing)-1) + 1):
            TaskProcessing_ = NetworkFunction.task(DataProcessing_[i][0],DataProcessing[i][1],Uuid)
            if TaskProcessing_ != []:
                tasklist.append(TaskProcessing_)
            else :
                del PrintDataProcessing_[i-di]
                di+=1
            lenlist.append(len(TaskProcessing_))
        break
    textqueue.put('play')
    textqueue.put('My_is_A')
    while 1:
        if textqueue.qsize() == 0:
            print len(tasklist)
            textqueue.put({'A':[tasklist,lenlist]})
    
    
        
def copylandB(username,password,textqueue):
    NetworkFunction.CopyCookie()
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
        Uuid = NetworkFunction.UUID()
        DataProcessing_ = NetworkFunction.UuidData(Uuid)
        if DataProcessing_ == '':
            continue
        tasklist = []
        lenlist = []
        TaskProcessing_ = []
        DataProcessing = []
        di = 0
        for i in DataProcessing_:
            if i[5] == '0':
                DataProcessing.append(i)
        PrintDataProcessing_ = DataProcessing[:]
        for i in range(0, (len(DataProcessing)-1) + 1):
            TaskProcessing_ = NetworkFunction.task(DataProcessing_[i][0],DataProcessing[i][1],Uuid)
            if TaskProcessing_ != []:
                tasklist.append(TaskProcessing_)
            else :
                del PrintDataProcessing_[i-di]
                di+=1
            lenlist.append(len(TaskProcessing_))
        break
    textqueue.put('play')
    textqueue.put('My_is_B')
    while 1:
        if textqueue.qsize() == 0:
            print len(tasklist)
            textqueue.put({'B':[tasklist,lenlist,PrintDataProcessing_,DataProcessing]})
    
def CopyProcessing(textqueue):
    print 'ok'
    while 1:
        if textqueue.qsize() == 4:
            textqueue.get(True)
            textqueue.get(True)
            textqueue.get(True)
            textqueue.get(True)
            break
    while 1:
        if textqueue.qsize() == 2:
            temp1 = textqueue.get(True)
            temp2 = textqueue.get(True)
            break
        else :
            continue
    if temp1.get('A') != None :
        listA = temp1.get('A')
        listB = temp2.get('B')
    else :
        listA = temp2.get('A')
        listB = temp1.get('B')
    tasklistA = listA[0]
    tasklistB = listB[0]
    #tasklistA.sort()
    #tasklistB.sort
    lenlistA = listA[1]
    lenlistB = listB[1]
    PrintDataProcessing_ = listB[2]
    DataProcessing_ = listB[3]
    '''
    temptasklistA = tasklistA[:]
    temptasklistB = tasklistB[:]
    for i in range(0, len(temptasklistA)-1 +1):
        del temptasklistA[i][4]
        del temptasklistB[i][4]
    if temptasklistA != temptasklistB.sort():
        print 'ok'
    '''
    TaskFlagA =[]
    TaskFlagB =[]
    for i in range(0, len(tasklistA)-1 +1):
        TaskFlagA.append(tasklistA[i][4])
        TaskFlagB.append(tasklistB[i][4])
    TaskFlag = {'A':TaskFlagA,'B':TaskFlagB}
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789^$.*+-?=!:|\/()[]{} '
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
        for li in range(0, (max(lenlistB)-1) + 1):
            for ll in range(0, (len(DataProcessing_)-1) + 1):
                try:
                    PrintData = str(tasklistB[ll][li][1].decode("utf-8").encode('gbk'))[0:14].center(16)
                    PrintData = PrintData.lower()
                    qweData = 0
                    for c in PrintData:
                        if c in fomart:
                            qweData+=1
                            if qweData%2 == 0:
                                lens = 14
                            else :
                                lens = 13
                    if tasklistB[ll][li][1] != '':
                        TaskIdList.append((ll+1)*100+li+1)
                    print ('%-5s%-16.16s%-4s' % (str(((ll+1)*100+li+1)).center(5),str(tasklistB[ll][li][1].decode("utf-8").encode('gbk'))[0:lens].center(16),''.center(4))),
                except:
                    print ('%-5s%-16.16s%-4s' % (''.center(5),"".center(20),''.center(4))),
            print ''    
        TaskIn = InputFunction.inputln(45, TaskIdList)
        if TaskIn:
            TaskInList.append(TaskIn)
            continue
        else :
            print log[52],TaskInList
            time.sleep(3)
            break
        break