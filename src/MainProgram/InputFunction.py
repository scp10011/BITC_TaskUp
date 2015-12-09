#!/usr/bin/python
# -*- coding:utf-8 -*-
import text
import msvcrt,sys
log = text.text()

def inputyn(SN):
    try:
        intext = raw_input(log[SN])
    except:
        print log[12]
        return inputyn(SN)
    if intext == 'y' or intext == 'Y':
        return True
    elif intext == 'n' or intext == 'N':
        return False
    else:
        print log[13]
        return inputyn(SN)


def inputsn(SN,LEN):
    try:
        intext = raw_input(log[SN])
    except:
        print log[12]
        return inputsn(SN,LEN)
    if intext.isdigit():
        intext = int(intext)
        if intext <= LEN:
            return int(intext)-1
        else:
            print log[14]
            return inputsn(SN,LEN) 
    else:
        print log[14]
        return inputsn(SN,LEN)


def inputpw(SN):
    chars = []
    print log[7],
    while True:
        try:
            newChar = msvcrt.getch()
        except:
            print log[12]
            return inputpw(SN)    
        if newChar in '\r\n':
            break
        elif newChar == '\b':
            if chars:
                del chars[-1]
                sys.stdout.write('\b \b')
        else:
            chars.append(newChar)
            sys.stdout.write('#')
    print ''
    return ''.join(chars)


def inputun(SN):
    try:
        intext = raw_input(log[SN])
    except:
        print log[12]
        return inputun(SN)
    if intext.isdigit():
        if len(intext)==11:
            return intext
        else:
            print log[9]
            return inputun(SN)
    else:
        print log[8]
        return inputun(SN)

