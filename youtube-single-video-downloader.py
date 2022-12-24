# from pytube import YouTube
from pytube import *

print("Welcome to the epic Youtube Downloader\n")
URL=input("Hey you Want to Download Video ? Okay Please Enter your Video 🔗 URL\n ")

video = YouTube(URL)
# to see videos treams 
# print(video.streams)

# Pritnig Video File title
print(f'Downloading your File: {video.title}')
# print(f'Downloading: {video_download.title}' )


# Video Stream Declaraiton from itag.

v_streams = video.streams.filter(progressive=True,file_extension='mp4').get_by_itag(22)

# Video Stream Declaraiton from generic Resoultion.

# v_streams = video.streams.get_by_resolution("780")

# file_location= print(input(" Where you want to save your Video\n"))

# video_resoultion.download(file_location)

# if file_location == 'file_location':
#     video_resoultion.download(file_location)
# else:
#     video_resoultion.download(r'\Downloads')
# print("File Path: ", v_streams.download(r'D:\Progamming-Vids'));
print("File Path: ", video.streams.get_highest_resolution().download(r'Downloads'));

print('Hurray : Sucessfully Downloaded' )