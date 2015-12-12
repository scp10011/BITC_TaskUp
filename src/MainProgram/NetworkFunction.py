#-*-coding:UTF-8-*-
#!C:\python27
import urllib
import urllib2 
import time
import re
import cookielib
from bs4 import BeautifulSoup
import random
import os

Cookiename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(Cookiename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)


def Login(username,password):
    LogUrl = 'http://ids2.bitc.edu.cn/amserver/UI/Login'
    LogData = {'IDToken' : '0',
               'IDToken1': '%s'%username,
               'IDToken2' : '%s'%password,
               'IDButton' : '登陆',
               'goto' : 'aHR0cDovL2VsZWFybmluZy5iaXRjLmVkdS5jbi96ZWNCZWl4aW4vU1NPU2VydmxldA==',
               'encoded' : 'true'
              }
    
    LogData = urllib.urlencode(LogData)
    UidRequest = urllib2.Request(LogUrl, LogData)  
    UidResponse = urllib2.urlopen(UidRequest)
    LogText = UidResponse.read()
    LogSoup = BeautifulSoup(LogText, "html.parser")
    LogZT = LogSoup.title.string
    if LogZT == "My JSP 'index.jsp' starting page":
        return True,UidResponse.code
    else:
        return False,UidResponse.code

    
def UUID():
    UidUrl = 'http://elearning.bitc.edu.cn/zecBeixin/student/myCourse/myCourse.html'            
    Uid = urllib2.urlopen(UidUrl)
    UidText = Uid.read()
    UidSoup = BeautifulSoup(UidText, "html.parser")
    Uid = UidSoup.findAll('script')
    Uuid = str(Uid[len(Uid)-2]).split("'")
    return Uuid[1]

def UuidData(Uuid):
    UrlTime = time.strftime("%Y%m%d")
    DataUrl = "http://elearning.bitc.edu.cn/zecBeixin/student/myCourse/zui_servlet?sid=proc__searchStudentCourseClassRel&UUID="+Uuid
    DataData = {'pageIndex' : '1',
                'pageSize' : '10',
                'courseClassRelation' : '{"planId":"125"}'
               }
    DataData = urllib.urlencode(DataData)
    DataRequest = urllib2.Request(DataUrl, DataData)
    DataResponse = urllib2.urlopen(DataRequest)
    DataText = DataResponse.read()
    return DataText

def DataProcessing(Data):
    DP = Data.split('{"checkType"')
    list = [[] for l in range(len(DP)-1)]
    for i in range(1, (len(DP)-1) + 1):
        Processing = DP[i]
        list[(i-1)].append(re.search('(courseId":)(\S*)(,"courseIds)',Processing).group(2))
        list[(i-1)].append(re.search('(classId":)(\S*)(,"classIds)',Processing).group(2))
        list[(i-1)].append(re.search('(credit":)(\S*)(,"hasUpdate)',Processing).group(2))
        list[(i-1)].append(re.search('(courseName":")(\S*)(","courseNum)',Processing).group(2))
        list[(i-1)].append(re.search('(userName":")(\S*)(","userNameOrNumber)',Processing).group(2))
    return list

def course(courseId,classId):
    CourseUrl = "http://elearning.bitc.edu.cn/zecBeixin/student/home/index.html?courseId="+courseId+"&taskObjId="+classId+"&planId=125"
    Course = urllib2.urlopen(CourseUrl)
    CourseText = Course.read()
    CourseSoup = BeautifulSoup(CourseText, "html.parser")
    CourseText = CourseSoup.findAll('td')
    CourseList = []
    CourseList.append(re.search('(<span class="span_num">)(.*?)(</span>)',str(CourseText[0])).group(2))
    CourseList.append(re.search('(<span class="span_num">)(.*?)(</span>)',str(CourseText[1])).group(2))
    CourseList.append(re.search('(<span class="span_num">)(.*?)(</span>)',str(CourseText[2])).group(2))
    return CourseList
    
def task(courseId,classId,Uuid):
    TaskUrl = "http://elearning.bitc.edu.cn/zecBeixin/student/courseHomework/zui_servlet?sid=task__getTaskListStudent&UUID="+Uuid
    TaskData = {'task' : '{"planId":"125","taskObjId":"'+classId+'","courseId":"'+courseId+'","taskName":"","taskForward":1}',
                'pageIndex' : '1',
                'pageSize' : '20'
               }
    TaskData = urllib.urlencode(TaskData)
    TaskRequest = urllib2.Request(TaskUrl, TaskData)
    TaskResponse = urllib2.urlopen(TaskRequest)
    TaskText = TaskResponse.read()
    return TaskText

def TaskProcessing(task):
    TP = task.split('{"baseTaskId"')
    list = [[] for l in range(len(TP)-1)]
    for i in range(1, (len(TP)-1) + 1):
        Processing = TP[i]
        list[(i-1)].append(re.search('(num":)(\d*)(,"opFlag)',Processing).group(2))
        list[(i-1)].append(re.search('(taskLesson":0,"taskName":")(.*?)(","taskNum":")',Processing).group(2))
        list[(i-1)].append(re.search('(taskId":)(\d*)(,"taskIds)',Processing).group(2))
        list[(i-1)].append(re.search('(userTaskId":)(\d*)(}},"isStart)',Processing).group(2))
        list[(i-1)].append(re.search('({"flag":)(\d*)(,"count)',Processing).group(2))
    return list

def Upfile(FilesName):
    FileName = []
    files = open(FilesName, "rb")
    length = os.path.getsize(FilesName)
    rd = ("%.16f" % random.random())
    UpTaskurl = 'http://elearning.bitc.edu.cn/zecBeixin/uploadImage!uploadImg.action?uploadtype=1&rd='+rd 
    BOUNDARY = '----------%s' % ''.join(random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 30))
    data=[]
    data.append('--%s' %BOUNDARY)
    data.append('Content-Disposition: form-data; name="filename"\r\n')
    data.append('%s' %FilesName)
    data.append('--%s' %BOUNDARY)
    data.append('Content-Disposition: form-data; name="fileupload"; filename="%s"'%FilesName)
    data.append('Content-Type: application/oct-stream\r\n')
    data.append(files.read())
    data.append('--%s' %BOUNDARY)
    data.append('Content-Disposition: form-data; name="Upload"\r\n')
    data.append('Submit Query')
    data.append('--%s--' %BOUNDARY)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    body = '\r\n'.join(data)
    req=urllib2.Request(UpTaskurl, body)
    req.add_header('accept', 'text/*')
    req.add_header('Content-Type', content_type)
    req.add_header('Connection','Keep-Alive')
    req.add_header('User-Agent','Shockwave Flash')
    req.add_header('Cache-Control','no-cache')
    resp = urllib2.urlopen(req, timeout=5).read()
    FileName.append(re.search('(filePath":")(\S*)(","original)',resp).group(2))
    FileName.append(re.search('(original":")(\S*)(","fileName)',resp).group(2))
    FileName.append(length)
    FileExtendName = str(FileName[1]).split('.')
    FileName.append(FileExtendName[len(FileExtendName)-1])
    return FileName

def UpTask(Uuid,taskId,userTaskId,text,FileName):
    url = 'http://elearning.bitc.edu.cn/zecBeixin/student/courseHomework/zui_servlet?sid=task__addUserTask&UUID='+Uuid
    data ={'userTask' : '{"taskId":"%s","userTaskId":"%s","userTaskContent":"<p>%s<br/></p>"}'%(taskId,userTaskId,text)}
    if FileName!='':
        data['fileRels'] = '[{"_status":1,"uid":"","fileRelId":"","operateType":1,"fileName":"%s","fileSize":%s,"objType":2,"filePath":"%s","fileExtendName":"%s"}]'%(FileName[1],FileName[2],FileName[0],FileName[3])
    data = urllib.urlencode(data)
    Request = urllib2.Request(url, data)
    Response = urllib2.urlopen(Request)
    UpTaskData = Response.read()
    TaskFlag = UpTaskData.strip('{').strip('}').replace('"','').split(',')
    x = []
    for i in TaskFlag:
        x.append(i.split(':'))
    return x
    
