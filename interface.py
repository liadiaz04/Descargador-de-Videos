from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

PINK = '#FFC0CB'
SIZE = "480x500"
ICON = 'assets/youtube.ico'
LOADING_PNG = 'assets/loading.png'
DONE_PNG = 'assets/done.png'
CROSS_PNG = 'assets/cross.png'

class Interface:

    def __init__(self):
        self.root = Tk()
        self.configuration()
        self.create_interface()

    def configuration(self):
        self.root.iconbitmap(ICON)
        self.root.title("Descargador de Videos de YouTube")
        self.root.geometry(SIZE)  # Tamaño de la ventana

    def create_interface(self):
        self.root.configure(bg=PINK) #Background

        self.url_label = Label(self.root, text="Ingresa la URL del video de YouTube:", bg=PINK)
        self.url_label.pack()

        self.url_entry = Entry(self.root, width=50)
        self.url_entry.pack()

        button_style = {'bg': PINK, 'fg': 'black', 'borderwidth': 2, 'relief': 'solid'}

        self.error_label = Label(self.root, text="", bg=PINK)  # Etiqueta para mostrar mensajes de error
        self.error_label.pack()  # Agregar la etiqueta a la interfaz

        self.video_button_alta = Button(self.root, text="Descargar Video en Alta Calidad (1080p)", **button_style)
        self.video_button_alta.pack()

        self.video_button_alta.pack(pady=15)
        
        self.video_button_media = Button(self.root, text="Descargar Video en Calidad Media (720p)", **button_style)
        self.video_button_media.pack()

        self.video_button_media.pack(pady=10)
        
        self.video_button_baja = Button(self.root, text="Descargar Video en Baja Calidad (360p)", **button_style)
        self.video_button_baja.pack()

        self.video_button_baja.pack(pady=10)

        self.video_button_audio = Button(self.root, text="Descargar Solo el audio (Mp3)", **button_style)
        self.video_button_audio.pack()

        self.video_button_audio.pack(pady=10)

        # Cargar imágenes
        self.loading_image = ImageTk.PhotoImage(Image.open(LOADING_PNG))  # Cargar la imagen de carga
        self.check_mark_image = ImageTk.PhotoImage(Image.open(DONE_PNG))  # Cargar la imagen de check mark
        self.cross_mark = ImageTk.PhotoImage(Image.open(CROSS_PNG))

        # Label para mostrar el estado de carga
        self.status_label = Label(self.root, bg=PINK)
        self.status_label.pack(pady=10)

    def show_loading(self):
        self.status_label.config(image=self.loading_image)
        self.status_label.image = self.loading_image  # Mantener una referencia

    def show_check_mark(self):
        self.status_label.config(image=self.check_mark_image)
        self.status_label.image = self.check_mark_image  # Mantener una referencia

    def show_cross_mark(self):
        self.status_label.config(image=self.cross_mark)
        self.status_label.image = self.cross_mark  # Mantener una referencia 

    def clear_error_message(self):
        self.error_label.config(text="                                                                                           ")
        self.root.update_idletasks()

    
    def set_high_definition_button(self, download_function) -> None:
        url = self.get_url()
        self.video_button_alta.config(command=download_function(url))
    
    def set_medium_definition_button(self, download_function) -> None:
        self.get_url()
        self.video_button_media.config(command=download_function)

    def set_low_definition_button(self, download_function) -> None:
        self.get_url()
        self.video_button_baja.config(command=download_function)

    def set_mp3_button(self, download_function) -> None:
        self.get_url()
        self.video_button_audio.config(command=download_function)

    def show_message(self, message, is_error=False):
        if is_error:
            color = 'red'
        else:
            color = 'green'
        
        self.error_label.config(text=message, fg=color)

    def get_url(self):
        return self.url_entry.get()

    def run_loop(self):
        self.root.mainloop()