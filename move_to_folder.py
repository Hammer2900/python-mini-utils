#!/usr/bin/python
# -*- coding: utf-8 -*-
import os , sys
from sys import platform as _platform
import shutil

class FilesMove(object):
    def __init__(self):
        self.argvs = sys.argv[1:]
        self.prefix = ''
        self.set_os_prefix()

        self.NEWNAME = "((--{name}--))"
        self.PATHNEWFOLDER = "{head}{prefix}{newname}{prefix}"

        self.check_argvs()

    def set_os_prefix(self):
        if _platform == "linux" or _platform == "linux2":
            self.prefix = "/"
        elif _platform == "win32":
            self.prefix = "\\"

    def name_new_folder(self, name):
        return self.NEWNAME.format(name=name)

    def move_files(self, names, path):
        for _ in names:
            shutil.move(_,path)

    def check_dir(self, folder):
        if os.path.isdir(folder):
            pass
        else:
            os.mkdir(folder)

    def make_name_ext(self, file_list):
        return os.path.splitext(os.path.basename(file_list[0]))

    def make_head_tail(self, file_list):
        return os.path.split(file_list[0])

    def main(self):
        name, ext = self.make_name_ext(self.argvs)

    def check_argvs(self):
        if len(self.argvs) > 1:
            self.main()
        else:
            print False

# prefix = ""
#
# if _platform == "linux" or _platform == "linux2":
#     prefix = "/"
# elif _platform == "win32":
#     prefix = "\\"
#
# allfiles = sys.argv[1:]
#
# name , ext = os.path.splitext(os.path.basename(allfiles[0]))
# print name, ext
# head , tail = os.path.split(allfiles[0])
# print head, tail
# newname = "((--{name}--))".format(name=name)
# if os.path.isdir(head+prefix+newname+prefix):
#     pass
# else:
#     os.mkdir(head+prefix+newname+prefix)
#     for lines in allfiles:
#         shutil.move(lines,head+prefix+newname+prefix)
if __name__ == '__main__':
    a = FilesMove()