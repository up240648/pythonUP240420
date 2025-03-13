# Level 3
# lista de edades

ages = [25, 30, 25, 40, 35, 30, 40, 50]

#1
st = set(ages)
print (len(st))
print(len(ages))

#2 la diferencia es que los topo string, es un tipo de variable que nos sirve para almacenar 
#cararacteres, las lsitas, para almacenar varios caracteres dentro de una sola variable, los 
#tuple, es la misma forma son una manera de almacenar datos, con la diferencia de que estos no nos permiten
#repetir los mismos

#3
sentence = "I am a teacher and ilove to inspire and teach people"
word = set (sentence.split())
print(len(word))


