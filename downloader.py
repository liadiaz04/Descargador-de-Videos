from pytubefix import YouTube
from pytubefix.cli import on_progress

class Downloader:

    def descargar_video_calidad(self, quality, url):
        yt = YouTube(url)
        ys = yt.streams.filter(res=quality).first()

        if ys:
            ys.download(output_path="downloads")
        else:
            raise Exception(f"El formato de calidad '{quality}' no está disponible para este video.")

    def descargar_audio(self, url):
        yt = YouTube(url)
        ys = yt.streams.get_audio_only()
        ys.download(output_path="downloads", mp3=True)
    
    def descargar_video_alta(self, url):
        self.descargar_video_calidad("1080p", url)

    def descargar_video_media(self, url):
        self.descargar_video_calidad("720p", url)

    def descargar_video_baja(self, url):
        self.descargar_video_calidad("360p", url)

