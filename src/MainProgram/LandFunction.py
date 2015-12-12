#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,UserSave
from text import *
def inuserlog(flag):
    if flag:
        return False,False
    else :
        username,password = load()
        return username,password

def ins():
    username = InputFunction.inputun(6)
    password = InputFunction.inputpw(7)
    return username,password

def load():
    text = open('Land','r')
    if text.read() !='':
        if InputFunction.inputyn(11) :
            text.close()
            username,password = UserSave.UserLoad()
            return username,password
        else :
            text.close()
            username,password = ins()
            if InputFunction.inputyn(10):
                flags = UserSave.UserSave(username, password)
                return username,password  
            else :
                return username,password     
    else:
        text.close()
        username,password = ins()
        if InputFunction.inputyn(10):
            flags = UserSave.UserSave(username, password)
            if flags:
                return username,password
        return username,password    
