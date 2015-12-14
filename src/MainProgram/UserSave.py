#-*-coding:UTF-8-*-
#!C:\python27
import wmi
import pyDes
import binascii
import md5
import base64
from text import *
c = wmi.WMI ()
lv = log[51]
def GetKeyID():
    encrypt_str = ""
    for cpu in c.Win32_Processor():
        encrypt_str += cpu.ProcessorId.strip()
    for physical_disk in c.Win32_DiskDrive():
        encrypt_str += physical_disk.SerialNumber.strip()
    for board_id in c.Win32_BaseBoard():
        encrypt_str += board_id.SerialNumber.strip()
    #for bios_id in c.Win32_BIOS():
        #encrypt_str += bios_id.SerialNumber.strip()
    for mac in c.Win32_NetworkAdapter():
        if mac.MACAddress != None:
            encrypt_str += mac.MACAddress
    MD5key = md5.new()
    MD5key.update(encrypt_str)
    return MD5key.hexdigest()

def UserEncryption(username,password):
    key=GetKeyID()[0:24]
    content=str(username)+'&*&'+password
    k = pyDes.triple_des(key,pyDes.CBC, lv, pad=None,padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(content)
    s = binascii.hexlify(d)
    return base64.b64encode(s)

def UserDecrypt(base):
    key=GetKeyID()[0:24]
    cipher = base64.b64decode(base)
    d = binascii.unhexlify(cipher)
    k = pyDes.triple_des(key,pyDes.CBC, lv, pad=None,padmode=pyDes.PAD_PKCS5)
    return k.decrypt(d)

def UserSave(username,password):
    #try:
    userlog = open('Land','w')
    cipher = UserEncryption(username,password)
    userlog.write(cipher)
    userlog.close()
        #return True
    #except:
        #return False

def UserLoad():
    try:
        cipher = open('Land','r').read()
        content = UserDecrypt(cipher)
        users = content.split("&*&")
        username = users[0]
        password = users[1]
        return username,password
    except:
        return False,False
