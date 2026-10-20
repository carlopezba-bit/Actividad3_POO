"""Modelos orientados a objetos para el ejercicio 8.3."""
import math


class FiguraGeometrica:
    """Clase padre que guarda el volumen y la superficie calculados."""

    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def set_volumen(self, volumen):
        self._volumen = volumen

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie


class Cilindro(FiguraGeometrica):
    """Cilindro circular recto de radio y altura dados en cm."""

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.altura + self.radio)


class Esfera(FiguraGeometrica):
    """Esfera de radio dado en cm."""

    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    """Pirámide regular de base cuadrada: lado, altura y apotema en cm."""

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.base ** 2 * self.altura / 3

    def calcular_superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


class Cubo(FiguraGeometrica):
    """Cubo de lado dado en cm (ampliación propuesta en el libro)."""

    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * self.lado ** 2


class Prisma(FiguraGeometrica):
    """Prisma rectangular recto de largo, ancho y altura dados en cm."""

    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura

    def calcular_superficie(self):
        return 2 * (self.largo * self.ancho +
                    self.largo * self.altura +
                    self.ancho * self.altura)
