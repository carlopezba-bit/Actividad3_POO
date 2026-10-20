"""Ventana principal para seleccionar una figura geométrica."""
import tkinter as tk
from tkinter import ttk
from ventana_figura import VentanaFigura


class VentanaPrincipal(tk.Tk):
    """Menú principal con los cinco tipos de figuras del ejercicio 8.3."""

    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.3 - Figuras geométricas")
        self.geometry("445x360")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        contenedor = ttk.Frame(self, padding=24)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text="Figuras geométricas",
                  font=("Arial", 17, "bold")).pack(pady=(2, 5))
        ttk.Label(contenedor, text="Selecciona una figura para calcular",
                  foreground="#4f5968").pack(pady=(0, 18))

        botones = ttk.Frame(contenedor)
        botones.pack(fill="x")
        figuras = ["Cilindro", "Esfera", "Pirámide", "Cubo", "Prisma"]
        for indice, figura in enumerate(figuras):
            boton = ttk.Button(
                botones, text=figura,
                command=lambda nombre=figura: self.abrir_figura(nombre))
            boton.grid(row=indice // 2, column=indice % 2,
                       sticky="ew", padx=8, pady=7, ipady=8)
        botones.columnconfigure(0, weight=1)
        botones.columnconfigure(1, weight=1)

        ttk.Separator(contenedor).pack(fill="x", pady=(14, 10))
        ttk.Label(contenedor, text="POO · Ejercicio 8.3 · Python + Tkinter",
                  foreground="#657181").pack()

    def abrir_figura(self, nombre_figura):
        VentanaFigura(self, nombre_figura)
