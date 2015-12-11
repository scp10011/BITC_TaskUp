#-*-coding:UTF-8-*-
#!C:\python27
import pyDes
import binascii
Mask = '\0\0\0\0\0\0\0\0'

def UserEncryption(key,username,password):
    content=str(username)+'&*&'+password
    k = pyDes.des(key,pyDes.CBC, Mask, pad=None,padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(content)
    return binascii.hexlify(d)

def UserDecrypt(key,cipher):
    d = binascii.unhexlify(cipher)
    k = pyDes.des(key,pyDes.CBC, Mask, pad=None,padmode=pyDes.PAD_PKCS5)
    return k.decrypt(d)

def UserSave(key,username,password):
    try:
        userlog = open('Land','w')
        cipher = UserEncryption(key,username,password)
        userlog.write(cipher)
        userlog.close()
        return True
    except:
        return False

def UserLoad(key):
    try:
        cipher = open('Land','r').read()
        content = UserDecrypt(key,cipher)
        users = content.split("&*&")
        username = users[0]
        password = users[1]
        return username,password
    except:
        return False,False