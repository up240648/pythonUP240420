# 1. Crear una tupla vacía
tupla_vacia = ()

# 2. Crear una tupla con los nombres de tus hermanas y hermanos (hermanos y hermanas imaginarios están bien)
hermanas = ('Ana', 'Laura', 'Maria')  # Ejemplo de hermanas
hermanos = ('Carlos', 'Luis')  # Ejemplo de hermanos

# 3. Unir las tuplas de hermanos y hermanas y asignarla a la tupla 'siblings'
hermanos_y_hermanas = hermanas + hermanos
print(hermanos_y_hermanas)  # Salida: ('Ana', 'Laura', 'Maria', 'Carlos', 'Luis')

# 4. ¿Cuántos hermanos y hermanas tienes?
cantidad_siblings = len(hermanos_y_hermanas)
print(f"Tengo {cantidad_siblings} hermanos y hermanas.")  # Salida: Tengo 5 hermanos y hermanas.

# 5. Modificar la tupla 'siblings' para agregar el nombre de tu padre y madre, y asignarla a 'family_members'
padre = 'Juan'
madre = 'Elena'
familia = hermanos_y_hermanas + (padre, madre)
print(familia)  # Salida: ('Ana', 'Laura', 'Maria', 'Carlos', 'Luis', 'Juan', 'Elena')