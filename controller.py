import re, os
from interface import Interface
from downloader import Downloader

LAST_DOWNLOADS = 3

class Controller:

    def __init__(self):
        self.create_downloads_folder()
        self.downloader = Downloader()
        self.interface = Interface()
        self.setup_interface()
        self.last_downloads = []

    def create_downloads_folder(self):
        # Crear la carpeta "downloads" si no existe
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

    def setup_interface(self):
        self.interface.video_button_alta.config(command=lambda: self.download_video(self.downloader.descargar_video_alta))
        self.interface.video_button_media.config(command=lambda: self.download_video(self.downloader.descargar_video_media))
        self.interface.video_button_baja.config(command=lambda: self.download_video(self.downloader.descargar_video_baja))
        self.interface.video_button_audio.config(command=lambda: self.download_video(self.downloader.descargar_audio))

    def download_video(self, download_function):
        url = self.interface.get_url()

        if self.validate_url(url):
            self.download_and_validate_format(download_function, url)

    def download_and_validate_format(self, download_function, url):
        try:
            self.download_handler(download_function, url)
        except Exception as error:
            self.download_error_handler(error)

    def update_last_downloads(self, title, quality):
        record = f"{title} - {quality}"

        if record not in self.last_downloads:
            self.last_downloads.append(record) 

        if len(self.last_downloads) > LAST_DOWNLOADS:
            self.last_downloads.pop(0)
        
        for i in range(len(self.last_downloads)):
            self.interface.update_lasts_downloads(i+1, self.last_downloads[i])
            self.interface.root.update_idletasks()

        self.refresh_last_downloads_display()

    def refresh_last_downloads_display(self):
        # Limpiar la lista mostrada en la interfaz
        for i in range(LAST_DOWNLOADS):
            if i < len(self.last_downloads):
                self.interface.update_lasts_downloads(i + 1, self.last_downloads[i])
            else:
                self.interface.update_lasts_downloads(i + 1, "")  # Limpiar si no hay más registros

    def download_handler(self, download_function, url):
            self.clear_message()
            self.interface.show_loading()  # Mostrar círculo de carga
            self.interface.root.update_idletasks()

            video_title, quality = download_function(url)

            self.update_last_downloads(video_title, quality)
            self.interface.show_check_mark()  # Mostrar check mark al finalizar
            self.interface.show_message('El archivo se ha descargado correctamente')

    def download_error_handler(self, error):
        self.interface.show_message(str(error), is_error=True)
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
        