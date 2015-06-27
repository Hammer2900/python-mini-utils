#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from urllib2 import urlopen
import json
from main2 import Cmd_manager
from main2 import Gui_manager


class All_manager(Cmd_manager):
    def __init__(self):
        self.YOUTUBE = "youtube-dl -o \"{folder}%(title)s.%(ext)s\" {url}"
        self.PYREVERSE = "pyreverse -my -A -o png -p {name} {file}"
        self.WGET = "wget {url} -P {folder}"
        self.FEH = "feh --bg-scale {pathimg}"

    def exe_youtube_dl(self, url, folder):
        self.cmd(self.YOUTUBE.format(url=url, folder=folder))

    def exe_pyreverse(self, name_png, file):
        self.cmd(self.PYREVERSE.format(name=name_png, file=file))

    def exe_wget(self, url, folder):
        self.cmd(self.WGET.format(url=url, folder=folder))

    def exe_feh(self, path):
        self.cmd(self.FEH.format(pathimg=path))

    def proc_wallpaper(self):
        string = urlopen('https://api.desktoppr.co/1/wallpapers/random').read()
        response = json.loads(string)
        url = response['response']['image']['url']
        name = url.split('/')[-1]
        path = "/home/izot/"
        self.exe_wget(url, path)
        self.exe_feh(path + name)


class All_runer(object):
    def __init__(self, terminal="sakura", directory='/', file=''):
        self.git_manager = All_manager()
        self.gui_manager = Gui_manager()
        self.TERM = terminal
        self.DIR = directory
        self.FILE = file
        self.FILENAME = os.path.basename(self.FILE).split('.')[0] or None
        self.MENU = {'Youtebe_dl': 'ydl', 'Pyreverse': 'pyreverse', 'Wallpaper':'wallpaper', 'Menu': ['ydl', 'pyreverse', 'wallpaper']}
        self.run()

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.MENU['Menu'])

        if otvet == self.MENU['Youtebe_dl']:
            url = self.gui_manager.enterebox(message=self.DIR)
            self.git_manager.exe_youtube_dl(url=url, folder=self.DIR)

        elif otvet == self.MENU['Pyreverse']:
            self.git_manager.exe_pyreverse(self.FILENAME, self.FILE)

        elif otvet == self.MENU['Wallpaper']:
            self.git_manager.proc_wallpaper()

    def run(self):
        self.choise_execute()


if __name__ == '__main__':
    All_runer(directory=sys.argv[1], file=sys.argv[2])
    # a = All_manager()
    # a.proc_wallpaper()
