import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from os import path
import time
import subprocess
def Subtitles(titles): #[['6 years in a man made hell part 2', 0, 1, 2], ["I used to work at McDonald's and I just remembered this", 0, 1]]
    for i in range(len(titles)):
        CurrentVideo = titles[i]
        for j in range(1, len(CurrentVideo)):
            clip = mp.VideoFileClip("Story_"+str(i)+"_Part_"+str(CurrentVideo[j])+".mp4")
            clip.audio.write_audiofile("theaudio.mp3")
            convertToWav()
            
            
            
            filename = "theaudio.wav"
            r = sr.Recognizer()
            # open the file
            with sr.AudioFile(filename) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)
                print(text)

def convertToWav():
    subprocess.call(['ffmpeg', '-i', 'theaudio.mp3',
                'converted_to_wav_file.wav'])
titles = [['6 years in a man made hell part 2', 0, 1, 2], ["I used to work at McDonald's and I just remembered this", 0, 1]]
Subtitles(titles)