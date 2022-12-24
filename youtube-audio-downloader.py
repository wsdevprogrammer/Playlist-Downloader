from pytube import YouTube

#Please Ignore the Commentend lines of codes. 


url=input("Please Enter your Video Url Link... 🔗🔗\n")

print("Wait for a While your Request is Processing\n")
youtube_audio = YouTube(url)

video_fn=youtube_audio.streams.filter(only_audio=True)
vid = list(enumerate(video_fn))
for i in  vid:
    print(i)

print()

strm = int(input("Enter your Audio Stream Number to Download your Audio: "))
video_fn[strm].download()
print('Congratulations: your Audio File Downloaded in your Given Folder')
