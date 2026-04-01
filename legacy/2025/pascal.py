# Lista

nums = [1, 1]

# Receta para hacer una línea a partir de 
# la línea anterior: 

# Ponemos unos en las puntas, y en el medio las sumas
# de los números de la lista anterior, de a pares

cant_rep = len(nums) - 1

nums_nuevos = []

nums_nuevos += [1]
for i in range(cant_rep):
  print('Deberia sumar ', nums[i], 'con', nums[i+1])
  n = nums[i] + nums[i+1]
  nums_nuevos += [n] 
nums_nuevos += [1]

print(nums_nuevos)