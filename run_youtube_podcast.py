#!/usr/bin/python
# -*- coding: utf-8 -*-
import pafy
import os
import time
from os.path import expanduser
from main2 import Cmd_manager
from main2 import Gui_manager

class Youtube_manager(Cmd_manager):
    def __init__(self):
        self.FFMPEG = 'ffmpeg -i \"{m4a}\" -ss {start} -to {end} -q:a 1 {outfolder}'
        self.FOLDER_SAVE = expanduser("~/{name}.mp3")

    def ffmpeg_exist(self):
        return self.is_tool('ffmpeg')

    def parse_time(self, time):
        return map(int, time.split(':'))

    def split_int(self, sec, parts):
        r = range(0, sec, sec/parts)[:-1] + [sec]
        return zip(r[:-1], r[1:])

    def show_time(self, houer=0, minets=0, second=0):
        return sum([a * b for a, b in zip([3600, 60, 1], map(int, [houer, minets, second]))])

    def download_youtube_m4a(self, url, path, quiet=True):
        video = pafy.new(url)
        audiostreams = video.getbestaudio()
        return (video.duration, audiostreams.download(filepath=path, quiet=quiet))

    def youtube_download(self, m4a, start, end, outfolder):
        self.cmd(self.FFMPEG.format(m4a=m4a,start=start,end=end,outfolder=outfolder))

class Youtube_runer():
    def __init__(self):
        self.git_manager = Youtube_manager()
        self.gui_manager  = Gui_manager()
        self.run()

    def run(self):
        print Youtube_manager().ffmpeg_exist()

if __name__ == '__main__':
    Youtube_runer()