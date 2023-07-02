import tkinter as tk

class BotonesAyuda:


    def __init__(self, ventana:tk.Frame):
        self.size = 150  #tamaño en px de los botones
        self.frame = tk.Frame(ventana)
        self.imagen_publico = tk.PhotoImage(file="assets/people.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_publico = tk.Button(self.frame, image=self.imagen_publico, command=self.usar_publico, width=self.size, height=self.size)

        self.imagen_50_50 = tk.PhotoImage(file="assets/50-50.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_50_50 = tk.Button(self.frame, image=self.imagen_50_50, command=self.usar_50_50, width=self.size, height=self.size)

        self.imagen_llamada = tk.PhotoImage(file="assets/call.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_llamada = tk.Button(self.frame, image=self.imagen_llamada, command=self.usar_llamada, width=self.size, height=self.size)

    def render(self):
        self.boton_llamada.pack(side="left", padx=10)
        self.boton_50_50.pack(side="left", padx=10)
        self.boton_publico.pack(side="left", padx=10)
        self.frame.pack()

    def delete(self):
        self.boton_llamada.pack_forget()
        self.boton_50_50.pack_forget()
        self.boton_publico.pack_forget()

    def usar_publico(self):
        # Lógica para usar la ayuda del público
        pass

    def usar_50_50(self):
        # Lógica para usar la ayuda del 50-50
        pass

    def usar_llamada(self):
        # Lógica para usar la ayuda de la llamada
        pass

