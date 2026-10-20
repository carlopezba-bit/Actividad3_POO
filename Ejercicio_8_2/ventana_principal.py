import math
import tkinter as tk
from tkinter import ttk, messagebox
from notas import Notas


class VentanaPrincipal(tk.Tk):
    """Interfaz gráfica para ingresar cinco notas y ver resultados."""

    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.2 - Notas")
        self.geometry("380x410")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        contenedor = ttk.Frame(self, padding=20)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(
            contenedor, text="Cálculo de notas", font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(0, 12))

        self.entradas = []
        for i in range(5):
            ttk.Label(contenedor, text=f"Nota {i + 1}:").grid(
                row=i + 1, column=0, sticky="w", pady=4
            )
            entrada = ttk.Entry(contenedor, width=20)
            entrada.grid(row=i + 1, column=1, sticky="ew", pady=4)
            self.entradas.append(entrada)

        botones = ttk.Frame(contenedor)
        botones.grid(row=6, column=0, columnspan=2, pady=12)
        ttk.Button(botones, text="Calcular", command=self.calcular).pack(
            side="left", padx=6
        )
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(
            side="left", padx=6
        )

        ttk.Separator(contenedor).grid(
            row=7, column=0, columnspan=2, sticky="ew", pady=(4, 10)
        )

        self.promedio_var = tk.StringVar(value="Promedio: —")
        self.desviacion_var = tk.StringVar(value="Desviación estándar: —")
        self.mayor_var = tk.StringVar(value="Nota mayor: —")
        self.menor_var = tk.StringVar(value="Nota menor: —")

        for fila, variable in enumerate(
            [self.promedio_var, self.desviacion_var,
             self.mayor_var, self.menor_var], start=8
        ):
            ttk.Label(contenedor, textvariable=variable).grid(
                row=fila, column=0, columnspan=2, sticky="w", pady=4
            )

        contenedor.columnconfigure(1, weight=1)
        self.entradas[0].focus_set()

    def calcular(self):
        valores = []
        for i, entrada in enumerate(self.entradas, start=1):
            texto = entrada.get().strip()
            if not texto:
                messagebox.showwarning(
                    "Nota faltante", f"Debes ingresar la nota {i}."
                )
                entrada.focus_set()
                return
            try:
                nota = float(texto.replace(",", "."))
                if not math.isfinite(nota):
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Dato no numérico", f"La nota {i} debe ser un número válido."
                )
                entrada.focus_set()
                return
            valores.append(nota)

        notas = Notas()
        notas.lista_notas = valores
        self.promedio_var.set(f"Promedio: {notas.calcular_promedio():.2f}")
        self.desviacion_var.set(
            f"Desviación estándar: {notas.calcular_desviacion():.2f}"
        )
        self.mayor_var.set(f"Nota mayor: {notas.calcular_mayor():.2f}")
        self.menor_var.set(f"Nota menor: {notas.calcular_menor():.2f}")

    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)
        self.promedio_var.set("Promedio: —")
        self.desviacion_var.set("Desviación estándar: —")
        self.mayor_var.set("Nota mayor: —")
        self.menor_var.set("Nota menor: —")
        self.entradas[0].focus_set()
