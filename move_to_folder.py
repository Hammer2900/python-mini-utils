#!/usr/bin/python
# -*- coding: utf-8 -*-
import os , sys
from sys import platform as _platform
import shutil

class FilesMove(object):
    def __index__(self, argvs):
        self.argvs = argvs
        self.prefix = ''
        self.set_os_prefix()

        self.NEWNAME = "((--{name}--))"

    def set_os_prefix(self):
        if _platform == "linux" or _platform == "linux2":
            self.prefix = "/"
        elif _platform == "win32":
            self.prefix = "\\"

    def move_files(self):
        pass

    def check_dir(self):
        pass

    def check_argvs(self):
        pass

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