def evaluar(f, inicial, veces):
    num = inicial
    for i in range(veces):
        num = f(num)
    return num

def iterar(f, veces):
    
    def evaluar(inicial):
        num = inicial
        for i in range(veces):
            num = f(num)
        return num
    
    return evaluar

def cosito(n):
    return (n ** 2 - 1) / 3

def coso(n):
    return (n + 1)/2



