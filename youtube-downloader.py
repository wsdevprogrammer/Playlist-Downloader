from asyncio import streams
from turtle import title
from pytube import YouTube


#Please Ignore the Commentend lines of codes. 

url=input("Please Enter your Youtube Video URL 🔗🔗🔗🔗🙏\n")
youtube_file= YouTube(url)

print(f'Downloading: {youtube_file.title}' )
# print(youtube_file.thumbnail_url)

# video_fn=youtube_file.streams.all() 
# video_fn=youtube_file.streams.get_by_resolution("720p") 

# vid = list(enumerate(video_fn))


# for i in  vide:
# for i in  video_fn:
#     print(i)

# print()

# strm = int(input("Enter your Video Resoulution Number: \n"))
# print("Please wait for a While your File is Being Downloading\n")

# Downloading with providing Resoultion Numbers

# video_fn[video_fn].download(r'F:\SEO_Pro\Python\downloaded-videos-folder') 

# Auto High Resoultioin Dowlded filter set. 
# video_fn.download(r'F:\SEO_Pro\Python\downloaded-videos-folder')
print("File Path: ",youtube_file.streams.get_highest_resolution().download(r'D:\Progamming-Vids'))

print('Sucessfully downloaded your file in your given forder')