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

def copylandA(username,password,textqueue,Aerrorqueue):
    NetworkFunction.CopyCookie()
    while 1:
        LogFlag,Code = NetworkFunction.Login(username,password)
        if LogFlag and Code==200:
            break
        else :
            Aerrorqueue.put(16)
            while 1:
                if Aerrorqueue.qsize()==2:
                    Aerrorqueue.get(True)
                    password=Aerrorqueue.get(True)
                    break
            continue
    while 1:
        try:
            Uuid = NetworkFunction.UUID()
            #DataProcessingΪ���󵽿γ���Ϣԭʼ����
            userId,name = NetworkFunction.userId()
            DataProcessing = NetworkFunction.UuidData(Uuid)
            #��ⷵ������Ϊ�պ�����
            if DataProcessing == '':
                continue
            DataProcessing.sort()
        except urllib2.URLError:
            Aerrorqueue.put(10060)
            continue
        tasklist = []
        lenlist = []
        DataProcessing_ = []
        di = 0
        
        #������Ϊ���޿ε���������
        for i in DataProcessing:
            if i[5] == '0':
                DataProcessing_.append(i)
                
        #���������ȥ��ҵΪ�յĿγ�
        PrintDataProcessing = DataProcessing_[:]
        for i in range(0, (len(DataProcessing_)-1) + 1):
        #for i in DataProcessing_:
            TaskProcessing = NetworkFunction.task(DataProcessing_[i][0],DataProcessing_[i][1],Uuid)
            if TaskProcessing != []:
                tasklist.append(TaskProcessing)
            else :
                del PrintDataProcessing[i-di]
                di+=1
            lenlist.append(len(TaskProcessing))
        break
    
    #����Ϣ����Ͷ������
    Aerrorqueue.put(0)
    textqueue.put('play')
    textqueue.put('My_is_A')
    #������ȡ����Ͷ�������ֵ�
    while 1:
        if textqueue.qsize() == 0:
            print len(tasklist)
            textqueue.put({'A':[tasklist,lenlist]})
            break
    while 1:
        if textqueue.qsize() == 1:
            TaskUpList = textqueue.get(True)
            print TaskUpList
            break
    while 1:
        TaskLogs = []
        for i in TaskUpList:
            print i
            taskid = tasklist[i[0]][i[1]][2]
            TaskLog = NetworkFunction.TaskLog(Uuid,userId,taskid)
            TaskLog[1]='%s.%s'%(name,TaskLog[3])
            TaskLogs.append(TaskLog)
        break
    while 1:
        textqueue.put(TaskLogs)
            
    
        
def copylandB(username,password,textqueue,Berrorqueue):
    NetworkFunction.CopyCookie()
    while 1:
        LogFlag,Code = NetworkFunction.Login(username,password)
        if LogFlag and Code==200:
            break
        else :
            Berrorqueue.put(16)
            while 1:
                if Berrorqueue.qsize()==2:
                    Berrorqueue.get(True)
                    password=Berrorqueue.get(True)
                    break
            continue
    while 1:
        try:
            Uuid = NetworkFunction.UUID()
            #DataProcessingΪ���󵽿γ���Ϣԭʼ����
            DataProcessing = NetworkFunction.UuidData(Uuid)
            #��ⷵ������Ϊ�պ�����
            if DataProcessing == '':
                continue
            DataProcessing.sort()
        except urllib2.URLError:
            Berrorqueue.put(10060)
            continue
        tasklist = []
        lenlist = []
        DataProcessing_ = []
        di = 0
        
        #������Ϊ���޿ε���������
        for i in DataProcessing:
            if i[5] == '0':
                DataProcessing_.append(i)
                
        #���������ȥ��ҵΪ�յĿγ�
        PrintDataProcessing = DataProcessing_[:]
        for i in range(0, (len(DataProcessing_)-1) + 1):
        #for i in DataProcessing_:
            TaskProcessing = NetworkFunction.task(DataProcessing_[i][0],DataProcessing_[i][1],Uuid)
            if TaskProcessing != []:
                tasklist.append(TaskProcessing)
            else :
                del PrintDataProcessing[i-di]
                di+=1
            lenlist.append(len(TaskProcessing))
        break
    
    #����Ϣ����Ͷ������
    Berrorqueue.put(0)
    textqueue.put('play')
    textqueue.put('My_is_B')
    #������ȡ����Ͷ�������ֵ�
    
    while 1:
        if textqueue.qsize() == 0:
            print len(tasklist)
            textqueue.put({'B':[tasklist,lenlist,PrintDataProcessing]})
            break
    while 1:
        if textqueue.qsize==1:
            break
    while 1:
        if textqueue.qsize==0:
            break
    while 1:
        if textqueue.qsize==1:
            TaskLogs = textqueue.get(True)   
            break
    print TaskLogs
def CopyProcessing(textqueue):
    print log[15]
    #ȡ������
    while 1:
        if textqueue.qsize() == 4:
            print log[17]
            textqueue.get(True)
            textqueue.get(True)
            textqueue.get(True)
            textqueue.get(True)
            break
    #���������ֵ�
    while 1:
        if textqueue.qsize() == 2:
            temp1 = textqueue.get(True)
            temp2 = textqueue.get(True)
            break
        else :
            continue
    #�ѽ���ABֵ����
    if temp1.get('A') != None :
        listA = temp1.get('A')
        listB = temp2.get('B')
    else :
        listA = temp2.get('A')
        listB = temp1.get('B')
    tasklistA = listA[0]
    tasklistB = listB[0]
    lenlistA = listA[1]
    lenlistB = listB[1]
    PrintDataProcessing = listB[2]
    
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789^$.*+-?=!:|\/()[]{} '
    #����CMD���ڿ��
    colsTEXT = len(PrintDataProcessing)*28
    os.system('mode con cols=%s lines=50'%colsTEXT)
    
    TaskInList = []
    TaskFlag = {'11':log[60],'10':log[60],'00':log[61],'01':log[62]}
    
    while 1:
        TaskIdList = []
        qk()
        print log[44]
        for l in PrintDataProcessing:
            #��ȡ�γ������ü�
            PrintData = str(l[3].decode("utf-8").encode('gbk'))[0:14].center(14).lower()
            qweData = 0
            #���ռ��λ��˫λ�ַ����������ӡ?
            for c in PrintData:
                if c in fomart:
                    qweData+=1
            if qweData%2 == 0:
                lens = 14
            else :
                lens = 13
            #��ӡ�γ���
            print('%-5s%-16.16s%-5s' % (log[46].center(5),str(l[3].decode("utf-8").encode('gbk'))[0:lens].center(16),log[47].center(5))),
        print ''
        #һ��ѭ������Ϊ�����ҵ��
        for li in range(0, (max(lenlistB)-1) + 1):
            #����ѭ������Ϊ�γ�����
            for ll in range(0, (len(PrintDataProcessing)-1) + 1):
                try:
                    #��ȡ��ҵ�����ü�
                    PrintTaskData = str(tasklistB[ll][li][1].decode("utf-8").encode('gbk'))[0:14].center(14).lower()
                    qweData = 0
                    #���ռ��λ��˫λ�ַ����������ӡ?
                    for c in PrintTaskData:
                        if c in fomart:
                            qweData+=1
                    if qweData%2 == 0:
                        lens = 14
                    else :
                        lens = 13
                    #�������ݵĿγ�ID��������
                    if tasklistB[ll][li][1] != '':
                        TaskIdList.append((ll+1)*100+li+1)
                    #��ӡ��ҵ����ID
                    print ('%-5s%-16.16s%-2s%-1s%-2s' % (str(((ll+1)*100+li+1)).center(5),str(tasklistB[ll][li][1].decode("utf-8").encode('gbk'))[0:lens].center(16),TaskFlag.get(tasklistA[ll][li][4]+tasklistA[ll][li][5]).center(2),'/',TaskFlag.get(tasklistB[ll][li][4]+tasklistB[ll][li][5]).center(2))),
                except IndexError:
                    print ('%-5s%-16.16s%-5s' % (''.center(5),"".center(20),''.center(5))),
            print ''
            
        TaskIn = InputFunction.inputln(45, TaskIdList)
        if TaskIn:
            TaskInList.append(TaskIn)
            continue
        else :
            print log[52],TaskInList
            time.sleep(3)
            break
    while 1:
        TaskUpList=[]
        for i in TaskInList:
            TaskUpList.append([int(str(i)[0:1])-1,int(str(i)[1:3])-1])
        textqueue.put(TaskUpList)
            
    
