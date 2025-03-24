#Escribe una función que genera un seis dígitos/carácter aleatorio.
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  # Ejemplo de salida: '1ee33d'

def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
    return '\n'.join(ids)
#
print(user_id_gen_by_user())  
# Entrada: 5 5  
# Ejemplo de salida:  
# kcsy2  
# SMFYb  
# bWmeq  
# ZXOYh  
# 2Rgxf  
