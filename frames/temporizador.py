import tkinter as tk

class Temporizador:
    
    def __init__(self, ventana:tk.Frame, tiempo:int, function_to_finish:None):
        self.ventana = ventana
        self.tiempo = tiempo
        self.tiempo_inicial = tiempo
        self.function_to_finish = function_to_finish
        self.barra = tk.Canvas(ventana, width=200, height=20, bg='white')
        self.barra.pack()
        self.after_id = None
        self.wasDelete = False
        self.isFinish = False
        
    def renderizar(self):
        if self.wasDelete == False:
            self.actualizar_barra()
        else:
            self.mostrar()

    def iniciar_contador(self):
        if self.wasDelete:
            self.mostrar()
        if self.isFinish:
            self.tiempo = self.tiempo_inicial
        self.actualizar_contador()

    def reiniciar_contador(self):
        self.eliminar()
        self.tiempo = self.tiempo_inicial
        self.renderizar()
        self.iniciar_contador()

    def actualizar_contador(self):
        if self.tiempo > 0:
            self.actualizar_barra()
            self.after_id = self.ventana.after(1000, self.actualizar_contador)
            self.tiempo -= 1
        else:
            self.function_to_finish()
            self.isFinish = True
            self.eliminar()

    def eliminar(self):
        self.barra.pack_forget()
        self.wasDelete = True
        if self.after_id:
            self.ventana.after_cancel(self.after_id)
            self.after_id = None

    def mostrar(self):
        self.barra.pack()

    def actualizar_barra(self):
        self.barra.delete("all")
        width = int((self.tiempo / self.tiempo_inicial) * 200)
        self.barra.create_rectangle(0, 0, width, 20, fill='green')
        self.barra.create_rectangle(width, 0, 200, 20, fill='white')
