import os 
from pytube import YouTube


SAVE_PATH = os.getcwd()


def downloadVideo(link):
    yt = YouTube(link)
    destination = ''
   
    try:
        
       downloadObj = yt.streams.filter(progressive=True)
       res=[r.resolution for r in downloadObj]
       
       print("Select the video resolution: ")
       for item in enumerate(res, 1):
           print(f'{item[0]}. {item[1]}')
       
       userChoice = int(input('Enter your choice: '))
       chosenStream = [stream for stream in downloadObj if stream.resolution == res[userChoice-1]][0]
       print("Downloading...")
       destination = chosenStream.download()  
       print("Download Successfully")
                     
    except: 
        print("Error has occured.")
        return;

    
if __name__ == '__main__':
    url = input("Enter video URL: ");
    downloadVideo(url)