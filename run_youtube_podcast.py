#!/usr/bin/python
# -*- coding: utf-8 -*-
import pafy
import re
from os.path import expanduser
from main2 import Cmd_manager
from main2 import Gui_manager

class Youtube_manager(Cmd_manager):
    def __init__(self):
        self.FFMPEG = 'ffmpeg -i \"{m4a}\" -ss {start} -to {end} -q:a 1 {outfolder}'

    def ffmpeg_exist(self):
        return self.is_tool('ffmpeg')

    def normalize_name(name):
        return re.sub("\s+", '', name)

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
        self.youtube_manager = Youtube_manager()
        self.gui_manager = Gui_manager()
        self.FOLDER_SAVE = expanduser("~/{name}.mp3")
        self.TEMP_FILE = expanduser("~/{name}.m4a")
        self.run()

    def run(self):
        vars = self.gui_manager.show_url_counts_dialog()
        vars_teme = self.youtube_manager.download_youtube_m4a(vars[0],self.TEMP_FILE.format(name='tempy'))
        pars_time = self.youtube_manager.parse_time(vars_teme[0])
        sec = self.youtube_manager.show_time(pars_time[0],pars_time[1],pars_time[2])
        for key,part in enumerate(self.youtube_manager.split_int(int(sec), int(vars[1]))):
            self.youtube_manager.youtube_download(vars_teme[1],part[0],part[1],self.FOLDER_SAVE.format(name=key))

if __name__ == '__main__':
    Youtube_runer()