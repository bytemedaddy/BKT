import youtube_dl
from pygame import mixer
from pygame.time import Clock
from time import perf_counter
import threading
import mutagen

# from time import sleep


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

    def load_song(self,index):
        if 0<=index<len(self.playlist):
            self.index=index
            self.current_time=0
            self.start_time=0

            f=mutagen.File(self.playlist[self.index])
            self.duration=round(f.info.length)

            c1=perf_counter()
            t1=threading.Thread(target=self.time_calculator,args=[c1])
            mixer.music.load(self.playlist[self.index])
            mixer.music.play()
            t1.start()
        else:
            print("play list index out of range")

    def play_pause(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.start_time=self.current_time
        else:
            c1=perf_counter()
            t1=threading.Thread(target=self.time_calculator,args=[c1])
            mixer.music.unpause()
            t1.start()

    def set_volume(self,volume):
        if volume-round(volume,1)==0 and 0<=volume<=1:
            mixer.music.set_volume(volume)
        else:
            print("incorrect volume input")

    def time_calculator(self,c1):
        clock=Clock()
        while mixer.music.get_busy():
            c2=perf_counter()
            self.current_time=self.start_time+c2-c1
            clock.tick(10)
            # print(self.current_time)




# mixer.init()
# mixer.music.load("./MUSICS/Duman/Duman - Senden Daha Guzel.wav")
# mixer.music.play()
# sleep(5)
# print(mixer.music.get_pos())
# mixer.music.set_pos(10)  
# sleep(5)



# download_audio("https://www.youtube.com/watch?v=3bfkyXtuIXk","./MUSICS/%(channel)s/")
