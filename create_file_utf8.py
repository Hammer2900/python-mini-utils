#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import easygui as g
from time import gmtime, strftime
from sys import platform as _platform
reload(sys)
sys.setdefaultencoding('utf-8')

prefix = ""

dir_virt = "virtualenv"
dir_folder = "dir1"
dir_py_project = "Python-Project"

project_file = "main.py"
test_file = "test.py"
requipments_file = "requirements.txt"
help_file = "README.md"
gitignore_file = ".gitignore"

Time = strftime("%Y-%m-%d---%H-%M", gmtime())

GIRIGNORE = """*.pyc
__pycache__"""

MAIN = """# -*- coding: utf-8 -*-
import sys

def main():
    pass

if __name__ == '__main__':
    sys.exit(main())
"""

def createafile(path, name):
    file = open(path + name, "a")

def create_files_to(path, edit=""):
    file = open(path, "a")
    file.write(unicode(edit))
    file.close()

def Create_files_true():
    namesnew = [x+reply for x in names]
    rnames = g.buttonbox(title="Имя ?", choices=namesnew)
    createafile(sys.argv[1],rnames)

def Create_dirs_true():
    if os.path.isdir(sys.argv[1]+dir_folder):
        pass
    else:
        os.mkdir(sys.argv[1]+dir_folder)
        os.mkdir(sys.argv[1]+dir_folder+prefix+"1")
        os.mkdir(sys.argv[1]+dir_folder+prefix+"2")
        os.mkdir(sys.argv[1]+dir_folder+prefix+"3")

def Create_dirs_date_true():
    if os.path.isdir(sys.argv[1]+Time):
        pass
    else:
        os.mkdir(sys.argv[1]+Time)

def Create_project_true():
    enters = g.enterbox("Имя проекта","Создание проекта")
    if enters != "":
        if os.path.isdir(sys.argv[1]+enters):
            pass
        else:
            os.mkdir(sys.argv[1]+enters)
            os.mkdir(sys.argv[1]+enters+prefix+dir_virt)
            create_files_to(sys.argv[1]+enters+prefix+project_file,MAIN)
            create_files_to(sys.argv[1]+enters+prefix+test_file,MAIN)
            create_files_to(sys.argv[1]+enters+prefix+requipments_file)
            enters2 = g.enterbox("Заметка","README.md")
            create_files_to(sys.argv[1]+enters+prefix+help_file,enters2)
            create_files_to(sys.argv[1]+enters+prefix+gitignore_file,GIRIGNORE)
    else:
        if os.path.isdir(sys.argv[1]+dir_py_project):
            pass
        else:
            os.mkdir(sys.argv[1]+dir_py_project)
            os.mkdir(sys.argv[1]+dir_py_project+prefix+dir_virt)
            create_files_to(sys.argv[1]+dir_py_project+prefix+project_file,MAIN)
            create_files_to(sys.argv[1]+dir_py_project+prefix+test_file,MAIN)
            create_files_to(sys.argv[1]+dir_py_project+prefix+requipments_file)
            enters2 = g.enterbox("Заметка","README.md")
            create_files_to(sys.argv[1]+dir_py_project+prefix+help_file,enters2)
            create_files_to(sys.argv[1]+dir_py_project+prefix+gitignore_file,GIRIGNORE)

if _platform == "linux" or _platform == "linux2":
    prefix = "/"
elif _platform == "win32":
    prefix = "\\"

choices = [".txt",".bat",".py",".html","Py-project","Dirs1","DirDate"]
names = ["1","2","3","help","list","notes","requipments",Time]

#todo Check path awaibility
reply = g.buttonbox("{ddirs}".format(ddirs=sys.argv[1]),title="Какой файл создать ?", choices=choices)


if reply == ".txt":
    Create_files_true()
elif reply == ".bat":
    Create_files_true()
elif reply == ".py":
    Create_files_true()
elif reply == ".html":
    Create_files_true()
elif reply == "Py-project":
    Create_project_true()
elif reply == "Dirs1":
    Create_dirs_true()
elif reply == "DirDate":
    Create_dirs_date_true()