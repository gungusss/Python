from pytube import YouTube
link = input("Give Link")# Get Link :o
video = YouTube(link) # Use Link
stream = video.streams.get_highest_resolution() #Get video
stream. download( ) #Download >:)