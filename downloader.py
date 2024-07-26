from pytubefix import YouTube
from pytubefix.cli import on_progress

class Downloader:

    def descargar_video_calidad(self, quality, url):
        video = YouTube(url)
        video_stream = video.streams.filter(res=quality).first()

        if video_stream:
            video_stream.download(output_path="downloads")
            return video.title, quality
        raise Exception(f"El formato de calidad '{quality}' no está disponible para este video.")

    def descargar_audio(self, url):
        video = YouTube(url)
        video_stream = video.streams.get_audio_only()
        video_stream.download(output_path="downloads", mp3=True)

        return video.title, "mp3"
    
    def descargar_video_alta(self, url):
        return self.descargar_video_calidad("1080p", url)

    def descargar_video_media(self, url):
        return self.descargar_video_calidad("720p", url)

    def descargar_video_baja(self, url):
        return self.descargar_video_calidad("360p", url)

