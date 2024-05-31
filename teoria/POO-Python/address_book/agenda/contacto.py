# Consideraciones de la sintaxis:
# __str__ -> Metodo que se ejecuta cuando se imprime el objeto
# @property -> Decorador que permite acceder a los atributos privados de la clase
# @atributo.setter -> Decorador que permite modificar los atributos privados de la clase
# -> Indica el tipo de retorno de la funcion
# : -> Indica el tipo de dato de un parametro

class Contacto:
    def __init__(self, nombre: str, telefono: str, direccion: str, relacion: str):
        self._nombre = nombre
        self._telefono = telefono
        self._direccion = direccion
        self._relacion = relacion


    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return (f"\nNombre:\t\t{self._nombre}\nTelefono:\t{self._telefono}\n"
                f"Direccion:\t{self._direccion}\nRelacion:\t{self._relacion}\n")

    @staticmethod
    def parsear_de_json(dic):
        return Contacto(dic["nombre"], dic["telefono"], dic["direccion"], dic["relacion"])

    def parsear_a_json(self):
      return {
        "nombre": self.nombre,
        "telefono": self.telefono,
        "direccion": self.direccion,
        "relacion": self.relacion
      }

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, value: str) -> None:
        self._telefono = value

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, value: str) -> None:
        self._direccion = value

    @property
    def relacion(self) -> str:
        return self._relacion

    @relacion.setter
    def relacion(self, value: str) -> None:
        self._relacion = value


