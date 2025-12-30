from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # necesitas instalar pillow

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Control de Mano Robótica")
        self.geometry("1000x600")
        self.configure(bg="#0c1a2b")

        self.sliders = {}
        self.create_ui()

    def create_ui(self):

        # -------- Título superior --------
        title = Label(self, text="Control de Mano Robótica",
                      font=("Segoe UI Semibold", 20),
                      bg="#0c1a2b", fg="white")
        title.pack(pady=10)

        # -------- Imagen de mano robótica --------
        try:
            image = Image.open("mano.png")  # poné acá tu imagen
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)

            img_label = Label(self, image=photo, bg="#0c1a2b")
            img_label.image = photo
            img_label.pack(pady=(0, 20))
        except:
            Label(self, text="[ IMAGEN NO ENCONTRADA ]",
                  bg="#0c1a2b", fg="white").pack()

        # -------- Frame de sliders --------
        container = Frame(self, bg="#0c1a2b")
        container.pack(fill="both", expand=True, padx=30)

        dedos = ["Pulgar", "Índice", "Medio", "Anular", "Meñique"]

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("TScale", background="#1a2d40")

        for dedo in dedos:
            frame = Frame(container, bg="#1a2d40")
            frame.pack(fill="x", pady=8)

            lbl = Label(frame, text=f"{dedo}: 0°", font=("Segoe UI", 11),
                        bg="#1a2d40", fg="white")
            lbl.pack(anchor="w", padx=10)

            slider = ttk.Scale(
                frame,
                from_=0, to=180,
                orient="horizontal",
                command=lambda val, d=dedo, l=lbl: self.update_value(l, val)
            )
            slider.pack(fill="x", padx=15, pady=5)

            self.sliders[dedo] = slider

        # -------- Botones inferiores --------
        btn_frame = Frame(self, bg="#0c1a2b")
        btn_frame.pack(pady=20)

        def bot(txt, cmd):
            return Button(
                btn_frame,
                text=txt,
                font=("Segoe UI", 10),
                bg="#1f6feb",
                fg="white",
                relief="flat",
                activebackground="#185ec9",
                cursor="hand2",
                width=15,
                command=cmd
            )

        bot("Guardar Movimiento", lambda: print("Guardar")).grid(row=0, column=0, padx=10)
        bot("Repetir Movimiento", lambda: print("Repetir")).grid(row=0, column=1, padx=10)
        bot("Resetear", self.reset).grid(row=0, column=2, padx=10)
        bot("Detener Movimiento", lambda: print("Detener")).grid(row=0, column=3, padx=10)

    def update_value(self, label, val):
        label.config(text=f"{label.cget('text').split(':')[0]}: {int(float(val))}°")

    def reset(self):
        for name, slider in self.sliders.items():
            slider.set(0)
