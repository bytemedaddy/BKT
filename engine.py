import youtube_dl
from pygame import mixer
from pygame.time import Clock
from time import perf_counter,sleep
import threading
import mutagen
import random


def download_audio(url,path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':path+'%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


class player:

    def __init__(self):
        mixer.init()
        self.runing=True
        self.repeat=False
        self.shuffle=False
        self.playlist=[]
        self.index=None

    def load_playlist(self,playlist):
        if playlist:
            self.playlist=playlist
            self.index=0
        else:
            print("play list empty")

    def load_song(self,index,start_time=0):
        if 0<=index<len(self.playlist):
            if mixer.music.get_busy():
                self.play_pause()
                sleep(0.1)

            self.index=index
            f=mutagen.File(self.playlist[self.index])
            self.duration=round(f.info.length)

            self.current_time=start_time
            self.start_time=start_time
            self.end_time_keeping=False

            t1=threading.Thread(target=self.time_keeper)
            mixer.music.load(self.playlist[self.index])
            mixer.music.play(start=start_time)
            t1.start()
        else:
            print("play list index out of range")

    def play_pause(self):
        if mixer.music.get_busy():
            self.end_time_keeping=True
            mixer.music.pause()
            self.start_time=self.current_time
        else:
            self.end_time_keeping=False
            t1=threading.Thread(target=self.time_keeper)
            mixer.music.unpause()
            t1.start()

    def repeat(self):
        self.repeat=not self.repeat

    def shuffle(self):
        self.shuffle=not self.shuffle
        if self.shuffle:
            self.shuffle_index=0
            self.shuffle_index_list=list([i for i in range(self.playlist) if i != self.index])
            random.shuffle(self.shuffle_index_list)
            self.shuffle_index_list=[self.index]+self.shuffle_index_list
    def set_position(self,sec):
        self.load_song(self.index,sec)

    def set_volume(self,volume):
        if volume-round(volume,1)==0 and 0<=volume<=1:
            mixer.music.set_volume(volume)
        else:
            print("incorrect volume input")

    def song_done(self):
        if self.repeat:
            self.load_song(self.index)
        elif self.shuffle:
            self.shuffle_index+=1
            self.load_song(self.shuffle_index_list[self.shuffle_index])
        else:
            self.load_song((self.index+1)%len(self.playlist))

    def time_keeper(self):
        clock=Clock()
        c1=perf_counter()
        while self.runing:
            if mixer.music.get_busy():
                c2=perf_counter()
                self.current_time=self.start_time+c2-c1
            else:
                if not self.end_time_keeping:
                    self.song_done()
                break
            clock.tick(30)
            




# mixer.init()
# mixer.music.load("./MUSICS/Duman/Duman - Senden Daha Guzel.wav")
# mixer.music.play()
# sleep(5)
# print(mixer.music.get_pos())
# mixer.music.set_pos(10)  
# sleep(5)



# download_audio("https://www.youtube.com/watch?v=3bfkyXtuIXk","./MUSICS/%(channel)s/")
