#-*-coding:UTF-8-*-
#!C:\python27
import urllib2 
def text():
    url = 'http://bitctaskup.li-exp.com:10080/asjkbncjakchiuacbanu.html'
    text = urllib2.urlopen(url)
    text = text.read().strip()
    text = text.split(",")
    log = []
    for line in text:
        log.append(line.strip().decode("utf-8").encode('gbk'))
    return log
log = text()