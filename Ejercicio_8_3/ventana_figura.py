"""Ventana reutilizable que gestiona los eventos de cada figura geométrica."""
import math
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

from figuras_geometricas import Cilindro, Esfera, Piramide, Cubo, Prisma


# Para cada figura se especifican su clase, dimensiones e ilustración.
FIGURAS = {
    "Cilindro": {
        "clase": Cilindro,
        "campos": [("radio", "Radio (cm)"), ("altura", "Altura (cm)")],
        "imagen": "cilindro.png",
    },
    "Esfera": {
        "clase": Esfera,
        "campos": [("radio", "Radio (cm)")],
        "imagen": "esfera.png",
    },
    "Pirámide": {
        "clase": Piramide,
        "campos": [("base", "Lado de la base (cm)"),
                   ("altura", "Altura (cm)"),
                   ("apotema", "Apotema (cm)")],
        "imagen": "piramide.png",
    },
    "Cubo": {
        "clase": Cubo,
        "campos": [("lado", "Lado (cm)")],
        "imagen": "cubo.png",
    },
    "Prisma": {
        "clase": Prisma,
        "campos": [("largo", "Largo (cm)"),
                   ("ancho", "Ancho (cm)"),
                   ("altura", "Altura (cm)")],
        "imagen": "prisma.png",
    },
}


class VentanaFigura(tk.Toplevel):
    """Crea los campos, muestra la figura y procesa Calcular/Limpiar."""

    def __init__(self, ventana_padre, nombre_figura):
        super().__init__(ventana_padre)
        self.nombre_figura = nombre_figura
        self.configuracion = FIGURAS[nombre_figura]
        self.entradas = {}
        self.imagen = None

        self.title(f"Ejercicio 8.3 - {nombre_figura}")
        self.geometry("460x570")
        self.resizable(False, False)
        self.inicio()
        self.transient(ventana_padre)
        self.focus_force()
        self.entradas[next(iter(self.entradas))].focus_set()

    def inicio(self):
        contenedor = ttk.Frame(self, padding=18)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text=self.nombre_figura,
                  font=("Arial", 16, "bold")).pack(pady=(0, 4))
        ttk.Label(contenedor, text="Cálculo de volumen y superficie",
                  foreground="#4f5968").pack(pady=(0, 8))

        ruta_imagen = (Path(__file__).resolve().parent / "imagenes" /
                       self.configuracion["imagen"])
        self.imagen = tk.PhotoImage(file=str(ruta_imagen))
        ttk.Label(contenedor, image=self.imagen).pack(pady=(0, 8))

        campos = ttk.Frame(contenedor)
        campos.pack(fill="x", padx=26)
        for numero_fila, (clave, etiqueta) in enumerate(
                self.configuracion["campos"]):
            ttk.Label(campos, text=etiqueta + ":").grid(
                row=numero_fila, column=0, sticky="w", pady=5)
            entrada = ttk.Entry(campos, width=17)
            entrada.grid(row=numero_fila, column=1, sticky="ew", pady=5)
            entrada.bind("<Return>", lambda _evento: self.calcular())
            self.entradas[clave] = entrada
        campos.columnconfigure(1, weight=1)

        botones = ttk.Frame(contenedor)
        botones.pack(pady=13)
        ttk.Button(botones, text="Calcular", command=self.calcular).pack(
            side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(
            side="left", padx=5)
        ttk.Button(botones, text="Cerrar", command=self.destroy).pack(
            side="left", padx=5)

        ttk.Separator(contenedor).pack(fill="x", pady=(1, 10))
        self.volumen_var = tk.StringVar(value="Volumen: —")
        self.superficie_var = tk.StringVar(value="Superficie: —")
        ttk.Label(contenedor, textvariable=self.volumen_var,
                  font=("Arial", 11)).pack(anchor="w", padx=20, pady=5)
        ttk.Label(contenedor, textvariable=self.superficie_var,
                  font=("Arial", 11)).pack(anchor="w", padx=20, pady=5)

    def calcular(self):
        """Lee dimensiones, valida los datos y crea el objeto de la figura."""
        valores = {}
        for clave, etiqueta in self.configuracion["campos"]:
            texto = self.entradas[clave].get().strip()
            if not texto:
                messagebox.showwarning(
                    "Dato faltante", f"Debes ingresar: {etiqueta}.",
                    parent=self)
                self.entradas[clave].focus_set()
                return
            try:
                numero = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Dato no numérico", f"Escribe un número válido en: {etiqueta}.",
                    parent=self)
                self.entradas[clave].focus_set()
                return
            if not math.isfinite(numero) or numero <= 0:
                messagebox.showerror(
                    "Valor no válido", f"{etiqueta} debe ser un número positivo y finito.",
                    parent=self)
                self.entradas[clave].focus_set()
                return
            valores[clave] = numero

        figura = self.configuracion["clase"](**valores)
        self.volumen_var.set(f"Volumen: {figura.get_volumen():.2f} cm³")
        self.superficie_var.set(
            f"Superficie: {figura.get_superficie():.2f} cm²")

    def limpiar(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.volumen_var.set("Volumen: —")
        self.superficie_var.set("Superficie: —")
        self.entradas[next(iter(self.entradas))].focus_set()
