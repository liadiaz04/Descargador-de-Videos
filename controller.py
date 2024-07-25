import re, os
from interface import Interface
from downloader import Downloader

class Controller:

    def __init__(self):
        self.create_downloads_folder()
        self.downloader = Downloader()
        self.interface = Interface()
        self.setup_interface()

    def create_downloads_folder(self):
        # Crear la carpeta "downloads" si no existe
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

    def setup_interface(self):
        self.interface.video_button_alta.config(command=lambda: self.download_with_error_handling(self.downloader.descargar_video_alta))
        self.interface.video_button_media.config(command=lambda: self.download_with_error_handling(self.downloader.descargar_video_media))
        self.interface.video_button_baja.config(command=lambda: self.download_with_error_handling(self.downloader.descargar_video_baja))
        self.interface.video_button_audio.config(command=lambda: self.download_with_error_handling(self.downloader.descargar_audio))

    def download_with_error_handling(self, download_function):
        url = self.interface.get_url()

        if self.validate_url(url):
            self.download_and_validate_format(download_function, url)

    def download_and_validate_format(self, download_function, url):
        try:
            self.clear_message()
            self.interface.show_loading()  # Mostrar círculo de carga
            self.interface.root.update_idletasks()
            download_function(url)
            self.interface.show_check_mark()  # Mostrar check mark al finalizar
            self.interface.show_message('El archivo se ha descargado correctamente')
        except Exception as e:
            print(e)
            self.interface.show_message(str(e), is_error=True)
            self.interface.show_cross_mark()

    def validate_url(self, url):
        if not self.is_valid_youtube_url(url):
            self.interface.show_message("La URL introducida no es un enlace válido de YouTube.", is_error=True)
            return False
        return True

    def is_valid_youtube_url(self, url):
        # Expresión regular para validar enlaces de YouTube
        pattern = re.compile(r"(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+")
        return bool(pattern.match(url))

    def clear_message(self):
        self.interface.clear_error_message()
    
    def start(self):
        self.interface.run_loop()
        