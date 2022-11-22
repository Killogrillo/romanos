class Heroe:
    #nombre,poder, apodo son varibles de la clase Heroe
    #nombre,poder, apodo son atributos de la clase Heroe
    nombre=""
    poder=""
    apodo=""

#funcion que inicializa la clase Heroe
#Self es un valor incialque indica para atributos y funciones que pertenecen a la misma clase.
#Se llama constructor de la clase Heroe

    def __init__(self):

        self.nombre=nombre
        self.poder=poder
        self.apodo=apodo
        
    def saludar(self):
        print("hola como vamos, "+self.nombre)

    def datos_heroe(self):
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"
    #metodo magico devolver una cadena string definida sin tener que llamar a una funcion
    #def __str__(self) -> str:
    #    return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"

    def __repr__(self) -> str:
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"

#spiderman es objeto de la clase Heroe
#spiderman es una instancia de la clase Heroe
                    
spiderman = Heroe("Peter Parker","super fuerza","Spiderman") 
spiderman.nombre="Peter Parker"
spiderman.poder="Mucha fuerza"
spiderman.apodo="Spiderman"

ironman = Heroe("Tony Stark","Millonario","Hombre de acero")
ironman.nombre="Tony Stark"
ironman.poder="Millonario"
ironman.apodo="Ironman"

print(spiderman.nombre)
print(ironman.nombre)