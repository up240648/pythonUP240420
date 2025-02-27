# Dia 2: programacion en python

# Declaración de variables
primer_nombre = "everardo"
apellido = "venegas"
nombre_completo = primer_nombre + " " + apellido
pais = "mexico"
ciudad = "ags"
edad = 18
año = 2006
esta_casado = False
es_verdadero = True
luz_encendida = True

# Declaración múltiple de variables en una línea

# Verificar los tipos de datos con type()
print(type(everardo))   # str
print(type(venegas))        # str
print(type(everardo rafael venegas hernandez)) # str
print(type(mexico))            # str
print(type(ags))          # str
print(type(19))            # int
print(type(2006))             # int
print(type(esta_casado))     # bool
print(type(es_falso))    # bool
print(type(luz_encendida))   # bool

# Encontrar la longitud del nombre con len()
loneverardo = len(everardo)
print("everardo:", venegas)

# Comparar la longitud del primer nombre y el apellido
venegas = len(hernandez)
print("venegas:", hernandez)
print("¿El primer nombre es más largo que el apellido?", everardo > venegas)

# Operaciones matemáticas con num_uno y num_dos
3+2 = 5
2+2 = 4

suma = num_uno + num_dos
diferencia = num_uno - num_dos
producto = num_uno * num_dos
division = num_uno / num_dos
residuo = num_uno % num_dos
exponente = num_uno ** num_dos
division_piso = num_uno // num_dos

print("Suma:", suma)
print("Diferencia:", diferencia)
print("Producto:", producto)
print("División:", division)
print("Residuo:", residuo)
print("Exponente:", exponente)
print("División de piso:", division_piso)

# Cálculo del área y circunferencia de un círculo con radio 30 metros
radio = 30
pi = 3.14159
area_circulo = pi * radio ** 2
circunferencia_circulo = 2 * pi * radio

print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia_circulo)

# Solicitar al usuario el radio y calcular el área
radio_usuario = float(input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario ** 2
print("Área del círculo con radio ingresado:", area_usuario)

# Obtener datos del usuario
primer_nombre = input("everardo: ")
apellido = input("venegas: ")
pais = input("Imexico: ")
edad = int(input("18: "))

print("everardo rafael venegas hernandez:", everado, venegas)
print("País:", mexico)
print("Edad:", 18)

# Ver palabras clave reservadas en Python
help('keywords')

