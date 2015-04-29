#!/usr/bin/python
# -*- coding: utf-8 -*-
from main2 import Cmd_manager
from main2 import Gui_manager

class Apt_manager(Cmd_manager):

    def __init__(self):
        self.APT_UPDATE = "{terminal} -e 'bash -c \"sudo apt-get update; exec bash\"'"
        self.APT_UPGRADE = "{terminal} -e 'bash -c \"sudo apt-get upgrade; exec bash\"'"
        self.APT_CLEAN = "{terminal} -e 'bash -c \"sudo apt-get clean; exec bash\"'"
        self.APT_AUTOREMOVE = "{terminal} -e 'bash -c \"sudo apt-get autoremove -y; exec bash\"'"
        self.APT_FINSTALL = "{terminal} -e 'bash -c \"sudo apt-get -f install -y; exec bash\"'"
        self.APT_INSTALL = "{terminal} -e 'bash -c \"sudo apt-get install {prog} -y; exec bash\"'"
        self.APT_UNINSTALL = "{terminal} -e 'bash -c \"sudo apt-get purge {prog} -y; exec bash\"'"
        self.APT_REPOSITORY = "{terminal} -e 'bash -c \"sudo apt-add-repository {repo} -y; exec bash\"'"

    def exe_apt_update(self, terminal):
        self.cmd(self.APT_UPDATE.format(terminal=terminal))

    def exe_apt_upgrade(self, terminal):
        self.cmd(self.APT_UPGRADE.format(terminal=terminal))

    def exe_apt_clean(self, terminal):
        self.cmd(self.APT_CLEAN.format(terminal=terminal))

    def exe_apt_autoremove(self, terminal):
        self.cmd(self.APT_AUTOREMOVE.format(terminal=terminal))

    def exe_apt_finstall(self, terminal):
        self.cmd(self.APT_FINSTALL.format(terminal=terminal))

    def exe_apt_install(self, terminal, prog):
        self.cmd(self.APT_INSTALL.format(terminal=terminal, prog=prog))

    def exe_apt_uninstall(self, terminal, prog):
        self.cmd(self.APT_UNINSTALL.format(terminal=terminal, prog=prog))

    def exe_apt_add_repository(self, terminal, repo):
        self.cmd(self.APT_REPOSITORY.format(terminal=terminal, repo=repo))

class Apt_runer(object):


    def __init__(self, terminal="sakura"):
        self.apt_manager = Apt_manager()
        self.gui_manager  = Gui_manager()
        self.TERM = terminal
        self.MENU ={ 'Update repository': 'Update' ,
                     'Upgrade distribution': 'Upgrade' ,
                     'Clear cash': 'Clean Cash' ,
                     'Autoremove package': 'Autoremove' ,
                     'Repair install -f': '-f install' ,
                     'Install package': 'Install' ,
                     'Purge package': 'Uninstall' ,
                     'Add repository':'AddRepo',
                     'Menu': ['Update',
                              'Upgrade',
                              'Clean Cash',
                              'Autoremove',
                              '-f install',
                              'Install',
                              'Uninstall',
                              'AddRepo'] }
        self.run()

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.MENU['Menu'])

        if otvet == self.MENU['Update repository']:
            self.apt_manager.exe_apt_update(self.TERM)

        elif otvet == self.MENU['Upgrade distribution']:
            self.apt_manager.exe_apt_upgrade(self.TERM)

        elif otvet == self.MENU['Clear cash']:
            self.apt_manager.exe_apt_clean(self.TERM)

        elif otvet == self.MENU['Autoremove package']:
            self.apt_manager.exe_apt_autoremove(self.TERM)

        elif otvet == self.MENU['Repair install -f']:
            self.apt_manager.exe_apt_finstall(self.TERM)

        elif otvet == self.MENU['Install package']:
            self.apt_manager.exe_apt_install(terminal=self.TERM, prog=self.gui_manager.enterebox(message='Имя пакета для установки'))

        elif otvet == self.MENU['Purge package']:
            self.apt_manager.exe_apt_uninstall(terminal=self.TERM, prog=self.gui_manager.enterebox(message='Имя пакета для удаления'))

        elif otvet == self.MENU['Add repository']:
            self.apt_manager.exe_apt_add_repository(terminal=self.TERM, repo=self.gui_manager.enterebox(message='Имя репозитория'))

    def run(self):
        self.choise_execute()

if __name__ == '__main__':
    Apt_runer()
    # xxx = Apt_manager()
    # xxx.exe_apt_update("sakura")
    # xxx.exe_apt_upgrade("sakura")
    # xxx.exe_apt_clean("sakura")
    # xxx.exe_apt_autoremove("sakura")
    # xxx.exe_apt_finstall("sakura")
    # xxx.exe_apt_install("sakura", "mc")
    # xxx.exe_apt_uninstall("sakura", "mc")