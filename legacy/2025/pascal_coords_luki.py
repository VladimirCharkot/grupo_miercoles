cord_colum = int(input("Ingresa la columna en la que quieres buscar: "))
cord_fila = int(input("Ingresa en qué fila quieres buscar: "))

num1 = 1
num2 = 1 

for i in range(cord_colum):
        num1 = num1 * (cord_fila - i)
        num2 = num2 * (i + 1)

num3 = num1 / num2
print(f"El numero es {num3}")

# Columna 3, fila 5
# 5 . 4 . 3
#-----------
# 1 . 2 . 3


# Columna 4, fila 6
# 6 . 5 . 4 . 3
#--------------
# 1 . 2 . 3 . 4


# Columna 7, fila 15
# 15 . 14 . 13 . 12 . 11 . 10 . 9
#--------------------------------
#    1 . 2 . 3 . 4 . 5 . 6 . 7

