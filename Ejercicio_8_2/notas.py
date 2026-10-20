import math


class Notas:
    """Almacena cinco notas y calcula sus estadísticas."""

    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        suma = 0
        for nota in self.lista_notas:
            suma += nota
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0
        for nota in self.lista_notas:
            suma += (nota - promedio) ** 2
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota > mayor:
                mayor = nota
        return mayor

    def calcular_menor(self):
        menor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota < menor:
                menor = nota
        return menor
