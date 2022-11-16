
d1={

    "nombre":"Carlos",
    "edad":"45",
    "dni":"4732421S"

}

d2=dict([
    ('nombre',' Dulce'),
    ('edad', '25'),
    ('dni', '48521367R')

])
print(d2)


#Funciones 
print("funcion get "d2.get('nombre'))


#Funcion Clear elimina todo el diccionario
d2.clear()
print("funcion clear", d2)

#Funcion Keys devuelve una lista con las keysy valores del diccionario
valores = d1.items()
print("Funcion items ",valores )

for key,val in valores:
    print(str(key) +"-"+str(val))

#Funcion Keys devuelve una lista con todas las keys del diccionario

llaves = d1.keys()
print("funcion key ", llaves)

#funcion values devuelve una lista con todos los valores del diccionario

valores = d1.values()
print("Funcion values", valores)

#funcion para agregar pop(key)
d1.pop(10)
print("funcion pop(10)" , d1)

#funcion update
d3={'a':10,'b':50,'c':60}
d1.update({'a':100,'b':50,'c':60})
print("funcion update", d1)

#popitem() elimina de manera aleatorai ua elemento del diccionario

d1.popitem()
print("Funcion popitem", d1)
