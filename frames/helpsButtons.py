import tkinter as tk
from tkinter import messagebox
from dataPreguntas import formatRespuestas

import random
from typing import Any

class BotonesAyuda:
    def __init__(self, ventana: tk.Frame):
        self.size = 150  # Tamaño en píxeles de los botones
        self.frame = tk.Frame(ventana)
        self.imagen_publico = tk.PhotoImage(file="assets/people.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_publico = tk.Button(self.frame, image=self.imagen_publico, command=lambda: self.usar_publico(), width=self.size, height=self.size)

        self.imagen_50_50 = tk.PhotoImage(file="assets/50-50.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_50_50 = tk.Button(self.frame, image=self.imagen_50_50, command=lambda: self.usar_50_50(), width=self.size, height=self.size)
        self.pregunta = None
        
        self.botonesRespuestas = [] 
        self.imagen_llamada = tk.PhotoImage(file="assets/call.png").subsample(2)  # Redimensionar la imagen a la mitad
        self.boton_llamada = tk.Button(self.frame, image=self.imagen_llamada, command=lambda: self.usar_llamada(), width=self.size, height=self.size)

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
        indexCorrecta = self.pregunta["correcta"]
        respuestaCorrecta  = formatRespuestas[indexCorrecta]
        messagebox.showinfo("Ayuda del público", f"El público elige la opción {respuestaCorrecta}.")
        self.boton_publico.config(state="disabled")
    def usar_50_50(self):
        indexCorrecta = self.pregunta["correcta"]
        respuestas = self.pregunta["respuestas"]

        opciones_eliminar = [i for i in range(len(respuestas)) if i != indexCorrecta]
        opciones_eliminar = random.sample(opciones_eliminar, 2)

        for i in opciones_eliminar:
            self.botonesRespuestas[i].config(state="disabled")

        messagebox.showinfo("50-50", "Se eliminan las opciones incorrectas.")
        self.boton_50_50.config(state="disabled")
        
    
        
    def usar_llamada(self):
        indexCorrecta = self.pregunta["correcta"]
        respuestas = self.pregunta["respuestas"]

        opciones_eliminar = [i for i in range(len(respuestas)) if i != indexCorrecta]
        opciones_eliminar = random.sample(opciones_eliminar, 2)
        
        respuestasSugeridas= [opciones_eliminar[0],indexCorrecta]
        respuestaSugerida = random.choice(respuestasSugeridas)
        respuestaSugerida = formatRespuestas[respuestaSugerida]
        messagebox.showinfo("Ayuda de la llamada", f"La llamada sugiere la opción: {respuestaSugerida}.")

        self.boton_llamada.config(state="disabled")
        # Obtener una respuesta incorrecta aleatoria
        
        
    def stateButtonsDefault(self):
        self.boton_50_50.config(state="normal")
        self.boton_llamada.config(state="normal")
        self.boton_publico.config(state="normal")
        
    def setPregunta(self,pregunta):
        self.pregunta = pregunta

    def setBotonesRespuesta(self,botonesRespuesta):
        self.botonesRespuestas = botonesRespuesta
# Resto del código...
