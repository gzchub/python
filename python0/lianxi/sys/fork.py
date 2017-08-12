#!/usr/bin/python
#coding=utf-8

import os
from time import sleep


pid = os.fork()

if pid < 0:
    print "啦啦啦啦啦啦啦"

elif pid == 0:
    print pid
    print "哈哈哈哈哈哈哈哈哈哈哈哈",os.getpid()

else:
    sleep(0.1)
    print pid
    print "嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎",os.getpid()

print"+++++++++++++++++++++++++++++++++++++++++++++"
