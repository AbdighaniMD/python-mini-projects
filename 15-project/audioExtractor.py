# install: "pip install moviepy"
import moviepy.editor as mp

videoFilePath = input("Enter the path for the video file: \n ")

videoClip = mp.VideoFileClip(videoFilePath)
audioClip = videoClip.audio
audioClip.write_audiofile("audio.mp3")

#C:\Users\ghani\OneDrive\Desktop\Projects\Mini_Python_Projects\Your First 2 Years of Trading The Key to Early Success.mp4