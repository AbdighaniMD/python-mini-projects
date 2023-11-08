# Install: "pip install pytube"
from pytube import YouTube

#Youtube video = https://www.youtube.com/shorts/TKIyim7qhnk

def startDownload():
    try:
        url = str(input("Enter the url for the Youtube video: \n" ))
        getVideo = YouTube(url).streams.get_highest_resolution()
        getVideo.download()
    except:
        print("Youtube Link is invalid")
    
    print("Complete")


startDownload()