from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento.nombre in [elem.nombre for elem in self.elementos]

    def agregar_elemento(self, elemento: Elemento) -> None:
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elem in otro_conjunto.elementos:
            self.agregar_elemento(elem)

    def __add__(self, otro_conjunto):
        self.unir(otro_conjunto)
        return self

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos = [elem for elem in conjunto1.elementos if elem in conjunto2.elementos]
        return cls(nombre=nombre, elementos=elementos)

    def __str__(self):
        elementos_str = ", ".join([elem.nombre for elem in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"