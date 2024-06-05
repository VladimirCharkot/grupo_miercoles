from random import *
class Persona:

  def __init__(self, nombre):
    self.nombre = nombre
    self.edad = randint(3, 80)
  
  def saludar(self):
    print(f'Hola, soy {self.nombre}')
    print(f'Tengo {self.edad} años')

p1 = Persona("Vladi")
p2 = Persona("Renzo")
p3 = Persona("Naza")
p4 = Persona("Luki")
p5 = Persona("Alma")
p6 = Persona("Lucía")
p7 = Persona("Fer")

p1.saludar()
p2.saludar()
p3.saludar()

# git init - convertir una carpeta en repo

# git status

# git add - agregar archivos al stage
# git commit -m "Mensaje" - commitea los cambios

# git log --oneline
# git checkout ______ - moverse entre ramas

# git merge NOMBRERAMA - mergea NOMBRERAMA en la rama en la que estoy parado

# git diff C1..C2