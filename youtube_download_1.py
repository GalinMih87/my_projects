import pytube

url = input("Enter video url: ")
path = "C:"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
