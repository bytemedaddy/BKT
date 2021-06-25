import engine
import os


player = engine.player()

def loop():
    while True:
        command=input(">>")
        if command=="q":
            break
        elif command=="l":
            path=input()
            player.load_playlist([path])
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
            pass


loop()