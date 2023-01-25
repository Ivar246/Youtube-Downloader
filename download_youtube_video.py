import os 
from pytube import YouTube


SAVE_PATH = os.getcwd()


# def downloadVideo(link):
    
#     yt = YouTube(link)
#     downloadObj = yt.streams.filter(progressive=True)
   
#     try:
#         downloadObj.download(SAVE_PATH)
#     except: 
#         print('Error has occured.')
    
#     print("Download Successfully")


url=input("Enter the video link > ")
yt = YouTube(url)
downloadObj = yt.streams.filter(progressive=True)
