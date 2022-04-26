import os 
from pytube import YouTube, Search


SAVE_PATH = os.getcwd()
link=input("Enter the video link> ")

yt = YouTube(link)

# print("title: ", yt.title)  # print title of video
# print("length: ", yt.length) # print length of vido in second
# print("views: {:,}".format(yt.views))   # print total number ov views of video

# print('all streams\n', [stream for stream in  yt.streams.order_by("resolution")])
a=yt.streams.filter(progressive=True, file_extension='mp4')
# print('\nfiltered stream\n', a)
# print('\nordered resolution:\n', a.order_by('resolution'))

# print('\nordered disc:\n', a.order_by('resolution').desc())
b=a.order_by('resolution').desc().first()
# print("\nb_first:\n", b)
b.download(SAVE_PATH, 'videoFilename', 'mp4')
print('secess')     


# urllib.error.URLError