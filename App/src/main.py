import tkinter as tk
#from tkinter import ttk
from tkinter import simpledialog
import pygame # type: ignore
from PIL import Image, ImageTk # type: ignore
from mesa import Mesa
from tkinter import PhotoImage
from tkinter import messagebox
from recursos import recurso


class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHOSTPOOL")
        self.geometry("980x650")
        self.resizable(False, False)
        self.configure(bg="#181817")
        self.extras_mesa1 = []
        self.mesas = []
        self.contador_mesas = 0


        # --- Frame principal ---
        self.mi_frame = tk.Frame(self, bg="#000000", padx=20, pady=20)
        #self.mi_frame.pack(fill="x")
        self.mi_frame.pack(fill="both", expand=True)

        #crear fondo
        

        #titulo

        self.label_titulo = tk.Label(self.mi_frame,text="GhostPool",font=("Arial", 15, "bold"),fg="white",
            bg="#000000")
        
        self.label_titulo.grid(row=0, column=0, sticky="w")


        self.boton_nueva = tk.Button(self.mi_frame, text="Nueva Mesa", command=self.agregar_mesa)
        self.boton_nueva.grid(row=1, column=0, sticky="w", pady=5)

        #creacion del canvas y scrollbar

        self.canvas_mesas = tk.Canvas(self.mi_frame, bg="#000000",highlightthickness=0)
        self.scrollbar_mesas = tk.Scrollbar(self.mi_frame, orient="vertical", command=self.canvas_mesas.yview)

        self.canvas_mesas.configure(yscrollcommand=self.scrollbar_mesas.set)

        self.canvas_mesas.grid(row=2, column=0, sticky="nsew")
        self.scrollbar_mesas.grid(row=2, column=1, sticky="ns")
        

        def ajustar_fondo(event):
            nueva_imagen = self.imagen_original.resize(
            (event.width, event.height),
            Image.LANCZOS
            )
            self.imagen_fondo = ImageTk.PhotoImage(nueva_imagen)
            self.canvas_mesas.itemconfig(self.fondo_canvas_id, image=self.imagen_fondo)

        self.canvas_mesas.bind("<Configure>", ajustar_fondo)

        def scroll_mouse(event):
            self.canvas_mesas.yview_scroll(-1 * (event.delta // 120), "units")

        def activar_scroll(event):
            self.canvas_mesas.bind_all("<MouseWheel>", scroll_mouse)

        def desactivar_scroll(event):
            self.canvas_mesas.unbind_all("<MouseWheel>")

        self.canvas_mesas.bind("<Enter>", activar_scroll)
        self.canvas_mesas.bind("<Leave>", desactivar_scroll)

        #fondo de canvas
        self.imagen_original = Image.open(recurso("GhostPoolOficial.png"))
        self.imagen_original = self.imagen_original.resize((980, 650))
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_original)

        self.fondo_canvas_id = self.canvas_mesas.create_image(
        0, 0, anchor="nw", image=self.imagen_fondo
        )

        #frame que contiene los frames de las mesas para scroll

        self.frame_mesas = tk.Frame(self.canvas_mesas,bg="#000000")
        self.frame_mesas.grid(row=2, column=0, sticky="nsew")

        self.mi_frame.grid_rowconfigure(2, weight=1)
        self.mi_frame.grid_columnconfigure(0, weight=1)

        self.canvas_mesas.create_window(
        (0, 0), 
        window=self.frame_mesas, 
        anchor="nw"
        )

        self.frame_mesas.bind(
        "<Configure>", 
        lambda event: self.canvas_mesas.configure(scrollregion=self.canvas_mesas.bbox("all"))
        
        )
        
    def agregar_mesa(self):
        self.contador_mesas = simpledialog.askstring("Nueva Mesa", "Ingrese el nombre o número de la mesa:")
        if self.contador_mesas == None:
            return

        if not self.contador_mesas.strip():
            messagebox.showwarning(
            "Nombre inválido",
            "Debe ingresar un nombre para la mesa"
            )
            return

        nueva = Mesa(self.frame_mesas, self.contador_mesas)
        fila_actual = len(self.mesas) + 2
        nueva.frame.grid(row=fila_actual, column=0, sticky="ew", padx=3, pady=3)
        self.mesas.append(nueva)
    
    

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()