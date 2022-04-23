import os 



from pytube import YouTube 
SAVE_PATH = os.getcwd()
print(SAVE_PATH)
link=input("Enter the video link> ")


yt = YouTube(link)
print("title: ", yt.title)
print("length: ", yt.length)
print("views: ", yt.views)

# print(yt.streams)
a=yt.streams.filter(progressive=True, file_extension='mp4')
b=a.order_by('resolution').desc().first()
print(b)
# b.download(SAVE_PATH, 'videoFilename', 'mp4')
