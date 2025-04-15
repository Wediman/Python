from pytube import YouTube
from sys import argv

link = input("Enter Link: ")
yt = YouTube(link)

print("title", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('C:/Users/wdi/Videos/ytdownload')
