#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from main2 import Cmd_manager
from main2 import Gui_manager

class Git_manager(Cmd_manager):


    def __init__(self):
        self.BODY = "{terminal} -e 'bash -c \"{command}; exec bash\"'"
        self.CLONE = "git clone {repo} {folder}"

    def exe_git_clone(self, terminal, repo, folder):
        self.cmd(self.BODY.format(terminal=terminal, command=self.CLONE.format(repo=repo, folder=folder)))

class Git_runer(object):


    def __init__(self, terminal="sakura", directory='/'):
        self.git_manager = Git_manager()
        self.gui_manager  = Gui_manager()
        self.TERM = terminal
        self.DIR = directory
        self.MENU = {'Clone repository':'clone','Menu': ['clone']}
        self.run()

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.MENU['Menu'])

        if otvet == self.MENU['Clone repository']:
            repos = self.gui_manager.enterebox(message=self.DIR)
            self.git_manager.exe_git_clone(self.TERM, repo=repos, folder=self.DIR)

        elif otvet == self.MENU['']:
            pass

    def run(self):
        self.choise_execute()

if __name__ == '__main__':
    Git_runer(directory=sys.argv[1])