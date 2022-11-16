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
milesima = {
    1000:'M',2000:'MM',3000:'MMM'
}

unidades={
    'I':1,'II':2,'III':3,
    'IV':4,'V':5,'VI':6,
    'VII':7,'VIII':8,'IX':9
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX'
}

decenas={
    'X':10,'XX':20,'XXX':30,
    'XL':40,'L':50,'LX':60,
    'LXX':70,'LXXX':80,'XC':90
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC'
}

centenas={
    'C':100,'CC':200,'CCC':300,
    'CD':400,'D':500,'DC':600,
    'DCC':700,'DCCC':800,'CM':900  
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM'  
}


#meta cumplir con esta funcion 
def entero_a_romano(num):

@@ -58,10 +51,24 @@ def entero_a_romano(num):
        lista[i] = lista[i]+"0"*((len(lista)-1 )-i)
    print(lista)

    return lista
    numero_romano=""
    for i in range(len(lista)):

        if i == 0:
            if milesima.get(int(lista[i])) != None:
                numero_romano += milesima.get(int(lista[i]) )

        elif i == 1:
            numero_romano += centenas.get( int(lista[i]) ) 
        elif i == 2:
            numero_romano += decenas.get( int(lista[i]) ) 
        elif i == 3:
            numero_romano += unidades.get( int(lista[i]) )    

    return numero_romano




print("funcion en accion",entero_a_romano(336))
print("funcion en accion",entero_a_romano(1998))

