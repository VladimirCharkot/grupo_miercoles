# ==============================================================================
# PARTE 1 — La intuición: funciones que reciben y devuelven funciones
# ==============================================================================
# Antes de ver decoradores, hay que entender que en Python las funciones
# son objetos como cualquier otro. Se pueden pasar como argumentos.

def saludar():
    print("Hola!")

def ejecutar(funcion):
    print("Antes de ejecutar...")
    funcion()
    print("Después de ejecutar.")

ejecutar(saludar)
# → Antes de ejecutar...
# → Hola!
# → Después de ejecutar.


# ==============================================================================
# PARTE 2 — El patrón: una función que *envuelve* a otra (wrapper)
# ==============================================================================

def agregar_log(funcion):
    def wrapper():
        print(f"[LOG] Llamando a '{funcion.__name__}'")
        funcion()
        print(f"[LOG] '{funcion.__name__}' terminó")
    return wrapper

def decir_hola():
    print("Hola mundo!")

decir_hola_con_log = agregar_log(decir_hola)
decir_hola_con_log()
# → [LOG] Llamando a 'decir_hola'
# → Hola mundo!
# → [LOG] 'decir_hola' terminó


# ==============================================================================
# PARTE 3 — La sintaxis @: el decorador propiamente dicho
# ==============================================================================
# @agregar_log es exactamente lo mismo que: decir_chau = agregar_log(decir_chau)
# Solo es azúcar sintáctica (syntactic sugar).

@agregar_log
def decir_chau():
    print("Chau!")

decir_chau()
# → [LOG] Llamando a 'decir_chau'
# → Chau!
# → [LOG] 'decir_chau' terminó


# ==============================================================================
# PARTE 4 — Decoradores con funciones que tienen argumentos
# ==============================================================================
# El wrapper tiene que aceptar y pasar los argumentos de la función original.
# *args y **kwargs capturan cualquier combinación posible.

def agregar_log_v2(funcion):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando a '{funcion.__name__}' con args={args}, kwargs={kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"[LOG] Resultado: {resultado}")
        return resultado
    return wrapper

@agregar_log_v2
def sumar(a, b):
    return a + b

sumar(3, 5)
# → [LOG] Llamando a 'sumar' con args=(3, 5), kwargs={}
# → [LOG] Resultado: 8


# ==============================================================================
# PARTE 5 — Preservar la identidad de la función decorada con @wraps
# ==============================================================================
# Sin @wraps, la función decorada "pierde su nombre" y su docstring.

from functools import wraps

def temporizador(funcion):
    import time
    @wraps(funcion)  # preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"'{funcion.__name__}' tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

@temporizador
def operacion_lenta():
    """Simula una operación que tarda."""
    import time
    time.sleep(0.1)
    return "listo"

operacion_lenta()
print(operacion_lenta.__name__)   # → operacion_lenta  (no 'wrapper')
print(operacion_lenta.__doc__)    # → Simula una operación que tarda.


# ==============================================================================
# PARTE 6 — Decoradores con parámetros propios
# ==============================================================================
# Para pasarle argumentos al decorador, necesitamos una capa más: una función
# que devuelve el decorador.

def repetir(n):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def aplaudir():
    print("👏")

aplaudir()
# → 👏
# → 👏
# → 👏


# ==============================================================================
# PARTE 7 — Apilar decoradores
# ==============================================================================
# Se aplican de abajo hacia arriba: primero @temporizador, luego @repetir(2).

@repetir(2)
@temporizador
def saludar_lento(nombre):
    import time
    time.sleep(0.05)
    print(f"Hola, {nombre}!")

saludar_lento("Ana")
# → 'saludar_lento' tardó 0.05s  (x2)
# → Hola, Ana!  (x2)


# ==============================================================================
# PARTE 8 — Caso real: control de acceso (autenticación)
# ==============================================================================

def requiere_admin(funcion):
    @wraps(funcion)
    def wrapper(usuario, *args, **kwargs):
        if usuario.get("rol") != "admin":
            print("Acceso denegado.")
            return None
        return funcion(usuario, *args, **kwargs)
    return wrapper

@requiere_admin
def borrar_base_de_datos(usuario):
    print(f"{usuario['nombre']} borró la base de datos.")

admin  = {"nombre": "Vlad",  "rol": "admin"}
alumno = {"nombre": "Sofía", "rol": "alumno"}

borrar_base_de_datos(admin)    # → Vlad borró la base de datos.
borrar_base_de_datos(alumno)   # → Acceso denegado.


# ==============================================================================
# PARTE 9 — Caso real: caché simple (memoización)
# ==============================================================================

def cachear(funcion):
    cache = {}
    @wraps(funcion)
    def wrapper(*args):
        if args not in cache:
            print(f"  [calculando {args}...]")
            cache[args] = funcion(*args)
        else:
            print(f"  [desde caché {args}]")
        return cache[args]
    return wrapper

@cachear
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
# Solo calcula los valores nuevos; el resto viene del caché.


# ==============================================================================
# PARTE 10 — Python ya trae decoradores built-in
# ==============================================================================

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property                   # getter: accede como atributo, no como método
    def area(self):
        import math
        return math.pi * self.radio ** 2

    @staticmethod               # no necesita self ni cls
    def descripcion():
        return "Figura geométrica plana"

    @classmethod                # recibe la clase, no la instancia
    def desde_diametro(cls, diametro):
        return cls(diametro / 2)

c = Circulo(5)
print(c.area)                   # → 78.53...  (sin paréntesis)
print(Circulo.descripcion())    # → Figura geométrica plana
c2 = Circulo.desde_diametro(10)
print(c2.radio)                 # → 5.0