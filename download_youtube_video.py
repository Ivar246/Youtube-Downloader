import os 
from pytube import YouTube 


SAVE_PATH = os.getcwd()
link=input("Enter the video link> ")


yt = YouTube(link)
print("title: ", yt.title)  # print title of video
print("length: ", yt.length) # print length of vido in second
print("views: {:,}".format(yt.views))   # print total number ov views of video

# print(yt.streams)
a=yt.streams.filter(progressive=True, file_extension='mp4')
b=a.order_by('resolution').desc().first()

b.download(SAVE_PATH, 'videoFilename', 'mp4')
