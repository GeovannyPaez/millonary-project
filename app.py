import tkinter as tk
from tkinter import messagebox
import random
from dataPreguntas import preguntas,formatRespuestas
from ventanaPrincipal import ventana
from frames.helpsButtons import BotonesAyuda
from frames.temporizador import Temporizador

# Variables globales
contador_intentos = 3
acumulador_puntos = 0
preguntas_restantes = []
tema_actual = ''
pregunta_actual = {}
tiempo_agotado = False
temporizador_label = None
temporizador = None

# Funciones auxiliares
def iniciar_juego():
    inicio.pack_forget()  # Oculta la pestaña de inicio
    tema_seleccion.pack()  # Muestra la sección de selección de tema

def game_over(message):
    temporizador.eliminar()
    messagebox.showerror("Game Over", message)
    tema_pregunta.pack_forget()
    inicio.pack()

def seleccionar_tema(tema):
    global tema_actual, preguntas_restantes, contador_intentos, acumulador_puntos
    tema_seleccion.pack_forget()  # Oculta la sección de selección de tema
    tema_actual = tema
    preguntas_restantes = list(preguntas[tema_actual])  # Copia la lista de preguntas del tema elegido
    contador_intentos = 3  # Reinicia el contador de intentos
    acumulador_puntos = 0  # Reinicia el acumulador de puntos
    resetear_intento()
    mostrar_pregunta()
    botonesAyuda.stateButtonsDefault()

    temporizador.iniciar_contador()

def timeOutQuestion():
    game_over("Lo siento, te quedaste sin tiempo...")

def mostrar_pregunta():
    global pregunta_actual, tiempo_agotado, temporizador_label, temporizador, preguntas_restantes
    if preguntas_restantes:
        tema_pregunta.pack()  # Muestra la sección de la pregunta actual

        # Seleccionar una pregunta aleatoria de las preguntas restantes
        pregunta_actual = random.choice(preguntas_restantes)
        pregunta.config(text=pregunta_actual['pregunta'])
        respuestas  = pregunta_actual['respuestas']
        botonesAyuda.setPregunta(pregunta_actual)
        
        # Configurar los botones de respuesta
        for i, respuesta in enumerate(respuestas):
            botones_respuesta[i].config(text=f"{formatRespuestas[i]}. {respuesta}",state="normal")
            

    else:
        messagebox.showinfo("¡Juego terminado!", f"Has respondido todas las preguntas del tema {tema_actual}.\nTotal de puntos: {acumulador_puntos}")
        temporizador.eliminar()
        tema_pregunta.pack_forget()  # Oculta la sección de la pregunta actual
        tema_seleccion.pack()  # Muestra la sección de selección de tema
        preguntas_restantes = []  # Restablece las preguntas restantes

def comprobar_respuesta(index: int):
    global contador_intentos, acumulador_puntos
    if contador_intentos > 1:
        if index == pregunta_actual['correcta']:
            acumulador_puntos += 100
            temporizador.eliminar()
            messagebox.showinfo("¡Respuesta correcta!", f"¡Correcto! Has ganado 100 puntos.\nTotal de puntos: {acumulador_puntos}")
        else:
            temporizador.eliminar()
            contador_intentos -= 1
            intentos_label.config(text=f"Intentos restantes: {contador_intentos}")  # Actualiza el texto del label
            messagebox.showinfo("¡Respuesta incorrecta!", f"¡Incorrecto! Pierdes un intento.\nIntentos restantes: {contador_intentos}")
        preguntas_restantes.remove(pregunta_actual)  # Elimina la pregunta actual de la lista de preguntas restantes
        mostrar_pregunta()
        temporizador.reiniciar_contador()

    else:
        game_over("Te quedaste sin intentos.")

# Resetear contador de intentos.
def resetear_intento():
    intentos_label.config(text=f"Intentos restantes: {contador_intentos}")

# Creación de widgets
# Frame inicial
inicio = tk.Frame(ventana, bg='black')
tk.Label(inicio, text="¿Quieres Ser Millonario?", font=("Arial", 24), fg='cyan', bg='black').pack(pady=50)
tk.Button(inicio, text="Iniciar juego", font=("Arial", 16), fg='cyan', bg='black', command=iniciar_juego).pack()

# Frame para seleccionar tema
tema_seleccion = tk.Frame(ventana, bg='black')
tk.Label(tema_seleccion, text="Selecciona un tema:", font=("Arial", 16), fg='cyan', bg='black').pack(pady=20)
tk.Button(tema_seleccion, text="Programación Básica", font=("Arial", 14), fg='cyan', bg='black',
          command=lambda: seleccionar_tema('programacion basica')).pack(pady=10)
tk.Button(tema_seleccion, text="Informática", font=("Arial", 14), fg='cyan', bg='black',
          command=lambda: seleccionar_tema('informatica')).pack(pady=10)
tk.Button(tema_seleccion, text="Tecnología", font=("Arial", 14), fg='cyan', bg='black',
          command=lambda: seleccionar_tema('tecnologia')).pack(pady=10)

# Frame para las preguntas
tema_pregunta = tk.Frame(ventana, bg='black')
# Traemos los botones de ayuda
botonesAyuda = BotonesAyuda(tema_pregunta)
botonesAyuda.render()
# Creamos la pregunta
pregunta = tk.Label(tema_pregunta, text="", font=("Arial", 16), fg='cyan', bg='black')
pregunta.pack(pady=20)

botones_respuesta = []
for i in range(4):
    boton = tk.Button(tema_pregunta, text="", font=("Arial", 14), fg='cyan', bg='black',
                      command=lambda idx=i: comprobar_respuesta(idx))
    boton.pack(pady=5)
    botones_respuesta.append(boton)
# añadimos los botones a las ayudas para poder modificarlos 
botonesAyuda.setBotonesRespuesta(botones_respuesta)

intentos_label = tk.Label(tema_pregunta, text=f"Intentos restantes: {contador_intentos}", font=("Arial", 14), fg='cyan', bg='black')
intentos_label.pack(pady=10)

# Creamos el temporizador
temporizador = Temporizador(tema_pregunta, 60, timeOutQuestion)

# Mostrar la ventana inicio
inicio.pack()
ventana.mainloop()
