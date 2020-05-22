ClasePIA.py
#Se utiliza para poder usar los datos de fecha.
import datetime
#Se usa para poder acceder a un archivo de tipo CSV.
import csv
#Se importa una clase para extraer elementos de un objeto.
from operator import attrgetter
#Se declara una clase.
#Se utiliza Pascal Casing.
class Contacto :
    # Se usa como constructor para generar objetos que estén parametrizados.
    # Esta clase cuenta con seis propiedades que se pueden observar entre los paréntesis(). 
    # self no se toma como una propiedad porque se le ordena al objeto que tiene que
    # hacerse referencia a si mismo.
    def __init__( self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTO):
        #NICKNAME: Se registra el apodo. Es de tipo de dato (str).
        #NOMBRE: Se registra el nombre. Es de tipo de dato (str).
        #CORREO: Se registra el correo. Es de tipo de dato (str)
        #TELEFONO: Se registra el telefono. Es de tipo de dato (int).
        #FECHANACIMIENTO: Se registra la fecha de nacimiento. Es de tipo de dato (datetime).
        #GASTO: Se registra el gasto. Es de tipo de dato (float).
        self.NICKNAME = NICKNAME
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        self.TELEFONO = TELEFONO
        self.FECHANACIMIENTO = FECHANACIMIENTO
        self.GASTO = GASTO