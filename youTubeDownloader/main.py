try:
    from pytube import YouTube
except Exception as e:
    print("error". format(e))


url = input(str('Url for download: '))


video = YouTube(url).streams.first().download()

print("Download concluido com sucesso!")