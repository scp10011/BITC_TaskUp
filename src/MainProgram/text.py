#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
def text():
    files = open('%s\q'%os.getcwd(),'r')
    lines = files.readlines()
    log = []
    for line in lines:
        log.append(line.strip())
    files.close()
    return log

