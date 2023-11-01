import random

medios_transporte = ["Bús", "Tren", "Buseta", "Metro", "Bicicleta", "Patineta Eléctrica"]
marcas = ["Mercedes-Benz", "Volvo", "Suzuki", "Ford", "GW", "Xiaomi"]

class MedioTransporteUrbano:
    def __init__(self):
        self.tipo = random.choice(medios_transporte)  # Seleccionar aleatoriamente un tipo
        self.marca = random.choice(marcas)  # Seleccionar aleatoriamente una marca
        self.modelo = random.randint(2000, 2023)  # Genera años aleatorios 
        


def presentar_informacion(transporte):
    
    print(f"Tipo: {transporte.tipo}")
    print(f"Marca: {transporte.marca}")
    print(f"Modelo: {transporte.modelo}")
    print('')  # Agrega un espacio al final de cada presentación
    
medio1 = MedioTransporteUrbano()
medio2 = MedioTransporteUrbano()
medio3 = MedioTransporteUrbano()
    
presentar_informacion(medio1)
presentar_informacion(medio2)
presentar_informacion(medio3)

