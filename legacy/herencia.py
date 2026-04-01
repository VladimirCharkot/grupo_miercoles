class Jugador:
    
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

    def patear(self):
        print(f"{self.nombre} patea la pelota")
        
    def gritar(self):
        print("Vaaaamoooo!")
        
class Arquero(Jugador):
    
    def atajar(self):
        print(f"{self.nombre} ataja la pelota")
        
    def gritar(self):
        print("¡Atajada!")
        super().gritar()

jug1 = Jugador("Messi", "Argentina")
jug2 = Arquero("Dibu", "Argentina")

jug1.patear()
jug1.gritar()

print()

jug2.atajar()
jug2.gritar()
jug2.patear()