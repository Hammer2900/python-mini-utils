#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from main2 import Cmd_manager
from main2 import Gui_manager

class All_manager(Cmd_manager):


    def __init__(self):
        self.YOUTUBE = "youtube-dl -o \"{folder}%(title)s.%(ext)s\" {url}"

    def exe_youtube_dl(self, url, folder):
        self.cmd(self.YOUTUBE.format(url=url, folder=folder))

class All_runer(object):


    def __init__(self, terminal="sakura", directory='/'):
        self.git_manager = All_manager()
        self.gui_manager  = Gui_manager()
        self.TERM = terminal
        self.DIR = directory
        self.MENU = {'Youtebe_dl':'ydl','Menu': ['ydl']}
        self.run()

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.MENU['Menu'])

        if otvet == self.MENU['Youtebe_dl']:
            url = self.gui_manager.enterebox(message=self.DIR)
            self.git_manager.exe_youtube_dl(url=url, folder=self.DIR)

        elif otvet == self.MENU['']:
            pass

    def run(self):
        self.choise_execute()

if __name__ == '__main__':
    All_runer(directory=sys.argv[1])