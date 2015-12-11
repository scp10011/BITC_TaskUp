#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,text,UserSave
log = text.text()
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
    key=log[51]
    text = open('Land','r')
    if text.read() !='':
        if InputFunction.inputyn(11) :
            text.close()
            username,password = UserSave.UserLoad(key)
            return username,password
        else :
            text.close()
            username,password = ins()
            if InputFunction.inputyn(10):
                flags = UserSave.UserSave(key, username, password)
                if flags:
                    return username,password
            
    else:
        text.close()
        username,password = ins()
        if InputFunction.inputyn(10):
            flags = UserSave.UserSave(key, username, password)
            if flags:
                return username,password
            
