#-*-coding:UTF-8-*-
#!C:\python27
import InputFunction,text
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
    users = open('Land','r').read()
    if users !='':
        if InputFunction.inputyn(11) :
            users = users.split("$*$")
            username = users[0]
            password = users[1]
            return username,password
        else :
            username,password = ins()
            if InputFunction.inputyn(10):
                userlog = open('Land','w')
                userlog.write(str(username))
                userlog.write('$*$')
                userlog.write(str(password))
                userlog.close()
            return username,password
    else:
        username,password = ins()
        if InputFunction.inputyn(10):
            userlog = open('land','w')
            userlog.write(str(username))
            userlog.write('$*$')
            userlog.write(str(password))
            userlog.close()
        return username,password
            
