#!/usr/bin/python
# -*- coding: utf-8 -*-
import os , sys
from sys import platform as _platform
import shutil

prefix = ""

if _platform == "linux" or _platform == "linux2":
    prefix = "/"
elif _platform == "win32":
    prefix = "\\"

allfiles = sys.argv[1:]

name , ext = os.path.splitext(os.path.basename(allfiles[0]))
head , tail = os.path.split(allfiles[0])
newname = "((--{name}--))".format(name=name)
if os.path.isdir(head+prefix+newname+prefix):
    pass
else:
    os.mkdir(head+prefix+newname+prefix)
    for lines in allfiles:
        shutil.move(lines,head+prefix+newname+prefix)