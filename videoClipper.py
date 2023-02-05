
from mutagen.mp3 import MP3
import math
from moviepy.editor import *
import os
import random

def videoClipper(NumberOfPosts):
    for i in range(NumberOfPosts):

        audio = MP3("Story_"+str(i)+".mp3")
        
        

        clip = VideoFileClip("Subway Surfers (2023) - Gameplay (PC UHD) [4K60FPS].mp4")
        startVideo = random.randint(0,10) * 100
        endVideo = startVideo + math.ceil(audio.info.length)

        # getting subclip as video is large
        clip = clip.subclip(startVideo, endVideo)
        audioclip = AudioFileClip("Story_"+str(i)+".mp3")
        
        clip = clip.set_audio(audioclip)
        clip.write_videofile("Story_"+str(i)+".mp4")
        if os.path.exists("Story_"+str(i)+".mp3"):
            os.remove("Story_"+str(i)+".mp3")
        else:
            print("The file does not exist")
    if os.path.exists("Stories"):
        os.remove("Stories")
    else:
        print("The file does not exist")

    
