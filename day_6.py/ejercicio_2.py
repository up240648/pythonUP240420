# Supongamos que ya tenemos la tupla 'family_members' de la respuesta anterior:
familia = ('Ana', 'Laura', 'Maria', 'Carlos', 'Luis', 'Juan', 'Elena')

# 1. Desempaquetar los hermanos y los padres de la tupla 'family_members'
hermanos_y_hermanas, padre, madre = familia[:-2], familia[-2], familia[-1]
print(f"Hermanos y hermanas: {hermanos_y_hermanas}")  # Salida: ('Ana', 'Laura', 'Maria', 'Carlos', 'Luis')
print(f"Padre: {padre}, Madre: {madre}")  # Salida: 'Juan', 'Elena'

# 2. Crear tuplas de frutas, vegetales y productos animales
frutas = ('Manzana', 'Banana', 'Cereza')
vegetales = ('Zanahoria', 'Brócoli', 'Espinaca')
productos_animales = ('Leche', 'Huevo', 'Queso')

# 3. Unir las tres tuplas en una variable llamada 'food_stuff_tp'
food_stuff_tp = frutas + vegetales + productos_animales
print(food_stuff_tp)  # Salida: ('Manzana', 'Banana', 'Cereza', 'Zanahoria', 'Brócoli', 'Espinaca', 'Leche', 'Huevo', 'Queso')

# 4. Cambiar la tupla 'food_stuff_tp' a una lista 'food_stuff_lt'
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)  # Salida: ['Manzana', 'Banana', 'Cereza', 'Zanahoria', 'Brócoli', 'Espinaca', 'Leche', 'Huevo', 'Queso']

# 5. Cortar el elemento o los elementos del medio de la tupla o lista
# Si es una lista con un número impar de elementos
if len(food_stuff_lt) % 2 != 0:
    middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
    print(f"Elemento del medio: {middle_item}")  # Salida: 'Zanahoria'
else:
    middle_items = food_stuff_lt[len(food_stuff_lt) // 2 - 1: len(food_stuff_lt) // 2 + 1]
    print(f"Elementos del medio: {middle_items}")  # Salida: ['Zanahoria', 'Brócoli']

# 6. Cortar los primeros tres y los últimos tres elementos de la lista 'food_stuff_lt'
primeros_tres_ultimos_tres = food_stuff_lt[:3] + food_stuff_lt[-3:]
print(f"Primeros tres y últimos tres elementos: {primeros_tres_ultimos_tres}")  # Salida: ['Manzana', 'Banana', 'Cereza', 'Leche', 'Huevo', 'Queso']

# 7. Eliminar completamente la tupla 'food_stuff_tp'
del food_stuff_tp
# Intentar imprimir 'food_stuff_tp' causará un error, ya que la tupla ha sido eliminada:
# print(food_stuff_tp)  # Esto generaría un error porque food_stuff_tp ya no existe.

# 8. Comprobar si un elemento existe en una tupla
nordic_countries = ('Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland')
print('Estonia' in nordic_countries)  # Salida: False (Estonia no es un país nórdico)
print('Iceland' in nordic_countries)  # Salida: True (Islandia es un país nórdico)
