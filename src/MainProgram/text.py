#-*-coding:UTF-8-*-
#!C:\python27
import sys
import urllib2 
def text():
    url = 'http://nas.li-exp.com:13945'
    text = urllib2.urlopen(url)
    text = text.read().strip()
    text = text.split(",")
    log = []
    for line in text:
        log.append(line.strip().decode("utf-8").encode('utf-8'))
    return log
print sys.getdefaultencoding()
log = text()
print log[1]