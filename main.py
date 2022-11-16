'''
1.-Crear una funciuon que pase de entero >0 y < 4000 a romano

2.-Cualquier otra enytrada debe de dar error

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000-> RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberErro("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
'''

class RomanNumberError( Exception ):
    pass

diccionario = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
}

unidades={
    'I':1,'II':2,'III':3,
    'IV':4,'V':5,'VI':6,
    'VII':7,'VIII':8,'IX':9,
}

decenas={
    'X':10,'XX':20,'XXX':30,
    'XL':40,'L':50,'LX':60,
    'LXX':70,'LXXX':80,'XC':90
    
}

centenas={
    'C':100,'CC':200,'CCC':300,
    'CD':400,'D':500,'DC':600,
    'DCC':700,'DCCC':800,'CM':900

}


  #M C D U
  #0 1 2 3
 #[0 9 6 9]
#[0000,900,60,9]

#guardar el numero string en una lista
valor="000300306"
numeros=list(valor)
print(numeros)

#añadir ceros
valorBuscado= "{:0>4d}".format(1)
print(valorBuscado)


#meta cumplir con esta funcion 
def entero_a_romano(num):
    '''
    num = str(num)
    longitud = len(num)-num[]
    if longitud < 4:
        "{:0>4d}".format()
    lista_numeros = list(num) 
    return lista_numeros
    '''
    lista = []
    num = str(num)

    if len(num)<4:
       num = "{:0>4s}".format(num)
    # for digito in num:
    #        lista.append(digito)
    lista = list(num) 
    for i in range(len(lista)):
        lista[i] = lista[i]+"0"*((len(lista)-1 )-i)
    print(lista)

    return lista

#Nuevo objetivo devolver 336 a CCCXXXVI

.\entorno_virtual\Scripts\activate




print("funcion en accion",entero_a_romano(336))


