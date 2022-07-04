try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("error". format(e))


# url = input(str('Url for download: '))
url = 'https://youtu.be/3Tb0NWTVtqE'

video = YouTube(url).streams.first().download()

# stream = video.streams.get_highest_resolution()

# stream.download(output_path='/home/jhonatan/www/estudos')

print("Download concluido com sucesso!")