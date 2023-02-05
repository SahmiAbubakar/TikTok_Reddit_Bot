from moviepy.editor import *
import math
import os
def videoSplitter(numberofPosts, titles):
    
    for i in range(numberofPosts):
        SubClipParts=[]
        SubClipParts.append(titles[i])
        clip = VideoFileClip("Story_"+str(i)+".mp4")
        startVideo = 0
        OGStoryLength = clip.duration
        NumberOfSubClips = math.ceil(OGStoryLength/60)
        for j in range(NumberOfSubClips):
            if(OGStoryLength - startVideo >60):
                TempClip = clip.subclip(startVideo, startVideo+60)
                TempClip.write_videofile("Story_"+str(i)+"_Part_"+str(j)+".mp4")
            else:
                TempClip = clip.subclip(startVideo, clip.duration)
                TempClip.write_videofile("Story_"+str(i)+"_Part_"+str(j)+".mp4")
            startVideo+= 60
            SubClipParts.append(j)
        titles[i] = SubClipParts
        if os.path.exists("Story_"+str(i)+".mp4"):
            os.remove("Story_"+str(i)+".mp4")
        else:
            print("The file does not exist")
    return titles
    
