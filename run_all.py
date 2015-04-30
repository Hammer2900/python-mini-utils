#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from main2 import Cmd_manager
from main2 import Gui_manager

class All_manager(Cmd_manager):


    def __init__(self):
        self.YOUTUBE = "youtube-dl -o \"{folder}%(title)s.%(ext)s\" {url}"
        self.PYREVERSE = "pyreverse -my -A -o png -p {name} {file}"

    def exe_youtube_dl(self, url, folder):
        self.cmd(self.YOUTUBE.format(url=url, folder=folder))

    def exe_pyreverse(self, name_png, file):
        self.cmd(self.PYREVERSE.format(name=name_png, file=file))

class All_runer(object):


    def __init__(self, terminal="sakura", directory='/', file=''):
        self.git_manager = All_manager()
        self.gui_manager  = Gui_manager()
        self.TERM = terminal
        self.DIR = directory
        self.FILE = file
        self.FILENAME = os.path.basename(self.FILE).split('.')[0] or None
        self.MENU = {'Youtebe_dl':'ydl', 'Pyreverse':'pyreverse','Menu': ['ydl', 'pyreverse']}
        self.run()

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.MENU['Menu'])

        if otvet == self.MENU['Youtebe_dl']:
            url = self.gui_manager.enterebox(message=self.DIR)
            self.git_manager.exe_youtube_dl(url=url, folder=self.DIR)

        elif otvet == self.MENU['Pyreverse']:
            self.git_manager.exe_pyreverse(self.FILENAME, self.FILE)

    def run(self):
        self.choise_execute()

if __name__ == '__main__':
    All_runer(directory=sys.argv[1], file=sys.argv[2])