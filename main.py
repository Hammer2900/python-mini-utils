#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import expanduser

import easygui as g


class Runer_ssh(object):
    def __init__(self, terminal="sakura", projectdir="projects/"):
        self.SLOVARIK = {}
        self.EXE = "{terminal} -e 'bash -c \"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {login}@{server} -p {port}; exec bash\"'"
        self.EXE_SFTP = "{terminal} -e 'bash -c \"ssh {login}@{server} -p {port}; exec bash\"'"
        self.SFTP = "sshfs {login}@{server}:/ -p {port} {dirpath}"
        self.UNMOUNT = "fusermount -u {dir}"
        self.COPYKEY = "{terminal} -e 'bash -c \"scp -P {port} '{key}' {login}@{server}:/; exec bash\"'"
        self.TERM = terminal
        self.PDIR = projectdir
        self.findproj = [f for f in os.listdir(self.PDIR)]
        self.mntfolders = [expanduser("~/mnt/") + x for x in os.listdir(expanduser("~/mnt/"))]
        self.menu = ['ssh', 'ssh-key', 'sftp', 'add config', 'edit config', 'unmount all', 'send ssh-key']
        self.ssh_params = ['Name', 'Server', 'Login', 'Password', 'Port']
        self.active_proj = ''
        self.create_mntd = ''
        self.mntdir = expanduser("~/mnt/{names}")
        self.choise_execute()

    def lenlist(self, lists):
        return (lambda x: True if len(x) == 4 else False)(lists)

    def cmd(self, command):
        os.system(command)

    def fuseunmount(self):
        for path in self.mntfolders:
            self.cmd(self.UNMOUNT.format(dir=path))

    def choisebox(self, message, dictfiles):
        return g.choicebox(msg=message, choices=dictfiles)

    def buttonbox(self, message, dictfiles):
        return g.buttonbox(msg=message, choices=dictfiles)

    def multenterbox(self, message, dictfiles, values):
        return g.multenterbox(msg=message, fields=dictfiles, values=values)

    def messagebox(self, message):
        return g.msgbox(msg=message)

    def filedialogbox(self, message):
        return g.fileopenbox(msg=message)

    def enterbox(self, message, default):
        return g.enterbox(msg=message, default=default)

    def get_dir_project(self):
        choisebox = self.choisebox(u"Выберите проект", self.findproj)
        self.active_proj = self.PDIR + choisebox  # todo Упростить класс
        return self.PDIR + choisebox

    def make_dir(self, names):
        self.create_mntd = self.mntdir.format(names=names)
        if os.path.exists(self.mntdir.format(names=names)):
            pass
        else:
            os.mkdir(self.mntdir.format(names=names))

    def choise_key(self):
        choisebox = self.filedialogbox(message="Укажите файл ключа")
        self.cmd(self.COPYKEY.format(terminal=self.TERM, login=self.SLOVARIK['LOGIN'], server=self.SLOVARIK['SERVER'],
                                     port=self.SLOVARIK['PORT'], key=choisebox))

    def set_slovarik(self, parselist):
        self.SLOVARIK['SERVER'] = parselist[0].strip()
        self.SLOVARIK['LOGIN'] = parselist[1].strip()
        self.SLOVARIK['PASS'] = parselist[2].strip()
        self.SLOVARIK['PORT'] = parselist[3].strip()
        return self.SLOVARIK

    def reads_config(self):
        with open(self.get_dir_project(), 'r') as f:
            parse = f.readlines()
            if self.lenlist(parse):
                return self.set_slovarik(parse)
            else:
                return self.messagebox(u"Мало параметров")

    def write_config(self):
        stroka = "{SERVER}\n{LOGIN}\n{PASS}\n{PORT}\n".format(SERVER=self.SLOVARIK['SERVER'],
                                                              LOGIN=self.SLOVARIK['LOGIN'],
                                                              PASS=self.SLOVARIK['PASS'],
                                                              PORT=self.SLOVARIK['PORT']
        )
        with open(self.active_proj, 'w') as f:
            f.write(stroka)

    def show_choise(self):
        return self.buttonbox(message=u"Действия", dictfiles=self.menu)

    def choise_execute(self):
        otvet = self.show_choise()
        if otvet == self.menu[0]:
            self.reads_config()
            self.cmd(self.EXE.format(terminal=self.TERM,
                                     password=self.SLOVARIK['PASS'],
                                     login=self.SLOVARIK['LOGIN'],
                                     server=self.SLOVARIK['SERVER'],
                                     port=self.SLOVARIK['PORT'])
            )

        elif otvet == self.menu[1]:
            self.reads_config()
            self.cmd(self.EXE_SFTP.format(terminal=self.TERM,
                                          login=self.SLOVARIK['LOGIN'],
                                          server=self.SLOVARIK['SERVER'],
                                          port=self.SLOVARIK['PORT'])
            )

        elif otvet == self.menu[2]:
            self.reads_config()
            self.make_dir(self.active_proj.split('/')[1])
            self.cmd(self.SFTP.format(login=self.SLOVARIK['LOGIN'], server=self.SLOVARIK['SERVER'],
                                      port=self.SLOVARIK['PORT'], dirpath=self.create_mntd))

        elif otvet == self.menu[3]:
            otvet = self.multenterbox(message=u"Создание", dictfiles=self.ssh_params, values=['Name', '', '', '', '22'])
            self.set_slovarik(otvet[1:])
            self.active_proj = self.PDIR + otvet[0]
            self.write_config()

        elif otvet == self.menu[4]:
            self.reads_config()
            otvet = self.multenterbox(message=u"Редактирование", dictfiles=self.ssh_params,
                                      values=[self.active_proj,
                                              self.SLOVARIK['SERVER'],
                                              self.SLOVARIK['LOGIN'],
                                              self.SLOVARIK['PASS'],
                                              self.SLOVARIK['PORT']
                                      ]
            )
            self.set_slovarik(otvet[1:])
            self.active_proj = otvet[0]
            self.write_config()
            self.messagebox(message=u"Файл {file} отредактирован".format(file=self.active_proj))

        elif otvet == self.menu[5]:
            self.fuseunmount()

        elif otvet == self.menu[6]:
            self.reads_config()
            self.enterbox(message=u"Пароль", default=self.SLOVARIK['PASS'])
            self.choise_key()


if __name__ == '__main__':
    Runer_ssh()
