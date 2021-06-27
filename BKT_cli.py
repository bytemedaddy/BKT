import engine
import threading


player = engine.player()

def loop():
    while True:
        command=input(">>")
        if command=="q":
            player.runing=False
            break
        elif command=="l":
            # path=input()
            # player.load_playlist([path])
            player.load_playlist(["./MUSICS/Duman/Duman - Senden Daha Guzel.wav","./MUSICS/Calvin Harris/Calvin Harris & Disciples - How Deep Is Your Love.wav"])
            player.load_song(0)
        elif command=="ps":
            player.play_pause()
        elif command=="v":
            volume=float(round(float(input()),1))
            if 0<=volume<=1:
                player.set_volume(volume)
        elif command=="r":  
            player.rewind()
        elif command=="gs":
            print(player.current_time)
        elif command=="ms":
            sec=int(input())
            player.set_position(sec)


loop()