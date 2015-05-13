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

    def move_files(self, path):
        for _ in self.argvs:
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
        head, tail = self.make_head_tail(self.argvs)
        new_path = self.PATHNEWFOLDER.format(head=head, prefix=self.prefix, newname=self.name_new_folder(name))
        self.check_dir(new_path)
        self.move_files(new_path)

    def check_argvs(self):
        if len(self.argvs) > 0:
            self.main()
        else:
            print False

if __name__ == '__main__':
    a = FilesMove()