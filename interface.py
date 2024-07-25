from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Colores y tamaños
DARK_BG = '#2E2E2E'         # Fondo oscuro
BUTTON_COLOR = '#FF0000'    # Rojo de YouTube
BUTTON_HIGHLIGHT = '#D00000' # Rojo oscuro
TEXT_COLOR = '#FFFFFF'      # Blanco
ERROR_COLOR = '#FF4500'     # Naranja rojizo
SIZE = "500x600"
ICON = 'assets/youtube.ico'
LOADING_PNG = 'assets/loading.png'
DONE_PNG = 'assets/done.png'
CROSS_PNG = 'assets/cross.png'
LOGO_PNG = 'assets/youtube-icon.png'  # Nombre del logo actualizado
FONT = ('Helvetica', 12, 'bold')

class Interface:

    def __init__(self):
        self.root = Tk()
        self.configuration()
        self.create_interface()

    def configuration(self):
        self.root.iconbitmap(ICON)
        self.root.title("Descargador de Videos de YouTube")
        self.root.geometry(SIZE)
        self.root.configure(bg=DARK_BG)

    def create_interface(self):
        style = ttk.Style()
        style.configure('TLabel', background=DARK_BG, font=FONT, foreground=TEXT_COLOR)
        style.configure('TButton', background=BUTTON_COLOR, foreground=TEXT_COLOR, font=FONT, borderwidth=0)
        style.map('TButton', background=[('active', BUTTON_HIGHLIGHT)])
        style.configure('TEntry', font=FONT)

        # Logo de YouTube
        self.logo_image = ImageTk.PhotoImage(Image.open(LOGO_PNG))
        self.logo_label = Label(self.root, image=self.logo_image, bg=DARK_BG)
        self.logo_label.pack(pady=(20, 10))

        self.url_label = ttk.Label(self.root, text="Ingresa la URL del video de YouTube:")
        self.url_label.pack(pady=(10, 5))

        self.url_entry = ttk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        self.error_label = ttk.Label(self.root, text="", foreground=ERROR_COLOR)
        self.error_label.pack(pady=(5, 15))

        button_frame = Frame(self.root, bg=DARK_BG)
        button_frame.pack(pady=10)

        self.video_button_alta = ttk.Button(button_frame, text="Alta Calidad (1080p)")
        self.video_button_alta.pack(side=TOP, pady=5)

        self.video_button_media = ttk.Button(button_frame, text="Calidad Media (720p)")
        self.video_button_media.pack(side=TOP, pady=5)

        self.video_button_baja = ttk.Button(button_frame, text="Baja Calidad (360p)")
        self.video_button_baja.pack(side=TOP, pady=5)

        self.video_button_audio = ttk.Button(button_frame, text="Solo Audio (Mp3)")
        self.video_button_audio.pack(side=TOP, pady=5)

        self.loading_image = ImageTk.PhotoImage(Image.open(LOADING_PNG))
        self.check_mark_image = ImageTk.PhotoImage(Image.open(DONE_PNG))
        self.cross_mark = ImageTk.PhotoImage(Image.open(CROSS_PNG))

        self.status_label = ttk.Label(self.root, background=DARK_BG)
        self.status_label.pack(pady=20)

    def show_loading(self):
        self.status_label.config(image=self.loading_image)
        self.status_label.image = self.loading_image

    def show_check_mark(self):
        self.status_label.config(image=self.check_mark_image)
        self.status_label.image = self.check_mark_image

    def show_cross_mark(self):
        self.status_label.config(image=self.cross_mark)
        self.status_label.image = self.cross_mark

    def clear_error_message(self):
        self.error_label.config(text=" ")
        self.root.update_idletasks()

    def show_message(self, message, is_error=False):
        if is_error:
            color = 'red'
        else:
            color = 'green'
        
        self.error_label.config(text=message, foreground=color)

    def get_url(self):
        return self.url_entry.get()

    def run_loop(self):
        self.root.mainloop()

if __name__ == '__main__':
    interface = Interface()
    interface.run_loop()
