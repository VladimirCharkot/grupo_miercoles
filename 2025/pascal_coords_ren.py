
nums = [1, 1]

def nuevalinea(ns):  
    cant_rep = len(ns) - 1
    nums_nuevos = []
    nums_nuevos += [1]

    # entender/traducir coordenadas    
    # for i in ns:
    #     if i[1] == 0 or i[1] == (len(ns) - 1) :
    #         ind = 0
    #         ns[ind] = 1
    #         ind += 1
    #     print(ns)
    #  crar proxima linea      
  
    for i in range(cant_rep):
        n = ns[i] + ns[i+1]
        nums_nuevos += [n] 
    nums_nuevos += [1]
    return nums_nuevos


fila = int(input("> Ingresar fila: "))
col = int(input("> Ingresar col: "))

for i in range(fila):
    nn = nuevalinea(nums)
    print(nn)
    nums = nn

print(f'El número en la fila {fila}, columna {col} es {nums[col]}')