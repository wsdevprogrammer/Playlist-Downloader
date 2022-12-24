from pytube import Playlist

print("Welcome to the epic Youtube Playlist Downloader\n")
py = Playlist(input("Please Enter your Playlist URL 🔗 here\n"))

print(f'Downloading: {py.title}')

# v_streams = py.streams.filter(progressive=True,file_extension='mp4').get_by_itag(22)

for video in py.videos:
# for video in v_streams.videos:clear

    print("File Path: ",video.streams.get_highest_resolution().download(r'D:\Progamming-Vids'))
    # video.streams.download(r'F:\SEO_Pro\Python\downloaded-videos-folder')
    # UPdated
    # print("File Path: ", video.streams.download(r'D:\Progamming-Vids'))
    
#print("File Path: ", v_streams.download(r'F:\SEO_Pro\Python\downloaded-videos-folder'))
print('Hurray : Sucessfully Downloaded Playlist' )

