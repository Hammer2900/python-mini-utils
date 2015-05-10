#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
from os.path import expanduser
import easygui as g


class File_manager(object):


    def __init__(self, main_dir):
        self.MAIN_DIR = main_dir
        self.ALL_PR_DIR = self.finde_all()
        self.MNT_DIR = expanduser("~/mnt/{names}")

    def get_fullpath(self, name):
        return "{path}/{name}".format(path=self.MAIN_DIR, name=name)

    def load_config(self, name):
        return json.load(open(self.get_fullpath(name)))

    def save_config(self, name, date):
        json.dump(date,open(self.get_fullpath(name),'w'))

    def finde_all(self):
        return [f for f in os.listdir(self.MAIN_DIR)]

    def mount_dir(self, name):
        if os.path.exists(self.MNT_DIR.format(names=name)):
            pass
        else:
            os.mkdir(self.MNT_DIR.format(names=name))
        return self.MNT_DIR.format(names=name)

class Gui_manager(object):


    def __init__(self):
        self.MENUS = {'Login ssh to pass':'ssh',
                      'Login ssh to key':'ssh-key',
                      'Mount sftp share':'sftp',
                      'Port forward':'port_forwarding',
                      'Add config':'add config',
                      'Edit config':'edit config',
                      'Unmount all conf shares':'unmount all',
                      'Copy key to server':'send ssh-key',
                      'Menu': ['ssh',
                               'ssh-key',
                               'sftp',
                               'port_forwarding',
                               'add config',
                               'edit config',
                               'unmount all',
                               'send ssh-key']}

    def choisebox(self, message, dictfiles):
        return g.choicebox(msg=message, choices=dictfiles)

    def enterebox(self, message, default=''):
        return g.enterbox(msg=message, default=default)

    def buttonbox(self, message, dictfiles):
        return g.buttonbox(msg=message, choices=dictfiles)

    def multenterbox(self, message, dictfiles, values):
        return g.multenterbox(msg=message, fields=dictfiles, values=values)

    def messagebox(self, message):
        return g.msgbox(msg=message)

    def filedialogbox(self, message):
        return g.fileopenbox(msg=message)

    def show_choise(self, dictionary):
        return self.buttonbox(message=u"Действия", dictfiles=dictionary)

    def show_create_dialog(self):
        return self.multenterbox(message=u"Создание", dictfiles=['Name', 'Server', 'Login', 'Password', 'Port'], values=['Name', '', '', '', '22'])

    def show_port_forward_dialog(self):
        return self.multenterbox(message=u"Проброс порта", dictfiles=['LocalPort','RemotePort'], values=['8888','27017'])

    def show_edit_dialog(self, values):
        return self.multenterbox(message=u"Редактирование", dictfiles=['Name', 'Server', 'Login', 'Password', 'Port'], values=values)

    def show_dir_project(self, list_all_proj):
        return self.choisebox(u"Выберите проект", list_all_proj)

    def show_choise_key(self):
        return self.filedialogbox(message="Укажите файл ключа")

class Cmd_manager(object):


    def __init__(self):
        self.EXE = "{terminal} -e 'bash -c \"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {login}@{server} -p {port}; exec bash\"'"
        self.EXE_SFTP = "{terminal} -e 'bash -c \"ssh {login}@{server} -p {port}; exec bash\"'"
        self.PORT_FORWARD = "{terminal} -e 'bash -c \"ssh -N -p 22 {login}@{server} -L {localport}:localhost:{remoteport}; exec bash\"'"
        self.SFTP = "sshfs {login}@{server}:/ -p {port} -o nonempty {dirpath}"
        self.UNMOUNT = "fusermount -u {dir}"
        self.COPYKEY = "{terminal} -e 'bash -c \"scp -P {port} '{key}' {login}@{server}:/; exec bash\"'"
        self.MNTFOLDER = [expanduser("~/mnt/") + x for x in os.listdir(expanduser("~/mnt/"))]

    def cmd(self, command):
        os.system(command)

    def exe_term_ssh(self, terminal, server, login, password, port):
        self.cmd(self.EXE.format(terminal=terminal, password=password, login=login, server=server, port=port))

    def exe_term_ssh_key(self, terminal, server, login, port):
        self.cmd(self.EXE_SFTP.format(terminal=terminal, login=login, server=server, port=port))

    def exe_mount_sftp(self, server, login, password, port, dirpath):
        self.cmd(self.SFTP.format(login=login, server=server, port=port, dirpath=dirpath))

    def exe_port_forward(self, terminal, server, login, localport, remoteport):
        self.cmd(self.PORT_FORWARD.format(terminal=terminal, server=server, login=login, localport=localport, remoteport=remoteport))

    def choise_key(self, terminal, server, login, port, key_file):
        self.cmd(self.COPYKEY.format(terminal=terminal, login=login, server=server, port=port, key=key_file))

    def fuseunmount(self):
        for path in self.MNTFOLDER:
            self.cmd(self.UNMOUNT.format(dir=path))



class Ssh_conector(object):


    def __init__(self, terminal="sakura"):
        self.SLOVARIK = {}
        self.file_manager = File_manager('data')
        self.gui_manager  = Gui_manager()
        self.cmd_manager  = Cmd_manager()
        self.TERM = terminal
        self.run()

    def set_slovarik(self, parselist):
        self.SLOVARIK['SERVER'] = parselist[0].strip()
        self.SLOVARIK['LOGIN'] = parselist[1].strip()
        self.SLOVARIK['PASS'] = parselist[2].strip()
        self.SLOVARIK['PORT'] = parselist[3].strip()
        return self.SLOVARIK

    def choise_execute(self):

        otvet = self.gui_manager.show_choise(self.gui_manager.MENUS['Menu'])

        if otvet == self.gui_manager.MENUS['Login ssh to pass']:
            edit = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(edit)
            self.cmd_manager.exe_term_ssh(self.TERM, self.SLOVARIK['SERVER'], self.SLOVARIK['LOGIN'], self.SLOVARIK['PASS'], self.SLOVARIK['PORT'])

        elif otvet == self.gui_manager.MENUS['Login ssh to key']:
            edit = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(edit)
            self.cmd_manager.exe_term_ssh_key(self.TERM, self.SLOVARIK['SERVER'], self.SLOVARIK['LOGIN'], self.SLOVARIK['PORT'])

        elif otvet == self.gui_manager.MENUS['Mount sftp share']:
            edit = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(edit)
            self.cmd_manager.exe_mount_sftp(self.SLOVARIK['SERVER'], self.SLOVARIK['LOGIN'],self.SLOVARIK['PASS'], self.SLOVARIK['PORT'],self.file_manager.mount_dir(edit))

        elif otvet == self.gui_manager.MENUS['Port forward']:
            server = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(server)
            port = self.gui_manager.show_port_forward_dialog()
            self.cmd_manager.exe_port_forward(self.TERM, self.SLOVARIK['SERVER'], self.SLOVARIK['LOGIN'], port[0], port[1])

        elif otvet == self.gui_manager.MENUS['Add config']:
            create = self.gui_manager.show_create_dialog()
            self.set_slovarik(create[1:])
            self.file_manager.save_config(create[0], self.SLOVARIK)

        elif otvet == self.gui_manager.MENUS['Edit config']:
            edit = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(edit)
            edit2 = self.gui_manager.show_edit_dialog([edit,self.SLOVARIK['SERVER'],self.SLOVARIK['LOGIN'],self.SLOVARIK['PASS'],self.SLOVARIK['PORT']])
            self.set_slovarik(edit2[1:])
            self.file_manager.save_config(edit2[0],self.SLOVARIK)

        elif otvet == self.gui_manager.MENUS['Unmount all conf shares']:
            self.cmd_manager.fuseunmount()

        elif otvet == self.gui_manager.MENUS['Copy key to server']:
            edit = self.gui_manager.show_dir_project(self.file_manager.finde_all())
            self.SLOVARIK = self.file_manager.load_config(edit)
            filekey = self.gui_manager.show_choise_key()
            self.gui_manager.enterbox(message=u"Пароль", default=self.SLOVARIK['PASS'])
            self.cmd_manager.choise_key(self.TERM, self.SLOVARIK['SERVER'], self.SLOVARIK['LOGIN'], self.SLOVARIK['PORT'], filekey)

    def run(self):
        self.choise_execute()

if __name__ == '__main__':
    Ssh_conector()
    # t = File_manager('data')
    # t.mount_dir('test')
