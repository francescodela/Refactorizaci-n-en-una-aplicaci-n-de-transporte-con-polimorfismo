class Vehiculo:
    def calcular_tiempo_de_viaje(self, distancia):
        raise NotImplementedError("Las subclases deben implementar este método")

class Coche(Vehiculo):
    def calcular_tiempo_de_viaje(self, distancia):
        velocidad = 60
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en coche: {tiempo:.2f} horas"

class Bici(Vehiculo):
    def calcular_tiempo_de_viaje(self, distancia):
        velocidad = 15
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en bicicleta: {tiempo:.2f} horas"

class Autobus(Vehiculo):
    def calcular_tiempo_de_viaje(self, distancia):
        velocidad = 40
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en autobús: {tiempo:.2f} horas"

vehiculos = [
    Coche(),
    Bici(),
    Autobus()
]

distancia = 100
for vehiculo in vehiculos:
    print(vehiculo.calcular_tiempo_de_viaje(distancia))
