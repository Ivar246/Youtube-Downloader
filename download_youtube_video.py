import os 
from pytube import YouTube


SAVE_PATH = os.getcwd()


def downloadVideo(link="https://youtu.be/tPEE9ZwTmy0"):
    yt = YouTube('https://youtu.be/tPEE9ZwTmy0')
    downloadObj = yt.streams.filter(progressive=True)
    destination = ''
   
    try:
        
       downloadObj = yt.streams.filter(progressive=True)
       res=[r.resolution for r in downloadObj]
       
       print("Select the video resolution: ")
       for item in res.enumerate(res, 1):
           print(f'{item[0]}. {item[1]}')
       
       userChoice = int(input('Enter your choice: '))
       chosenStream = [stream for stream in downloadObj if stream.resolutiion == res[userChoice-1]][0]
       destination = chosenStream.download(SAVE_PATH)  
                     
    except: 
        print('Error has occured.')
    
    print("Download Successfully")
    print(f"File has been saved in {destination}")

if '__name__' == '__main__':
    downloadVideo()