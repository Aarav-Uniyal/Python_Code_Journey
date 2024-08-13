from pygame import mixer


mixer.init()
mixer.music.load("Eminem.mp3")
mixer.music.play()


def play():
    while True:
        ar = input("Enter 'stop' to stop the music.\n")
        ar = ar.lower()
        if ar == "stop":
            mixer.music.stop()
            exit()

        else:
            play()

if __name__ == '__main__':
    play()
