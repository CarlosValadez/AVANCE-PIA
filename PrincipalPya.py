PrinciplaPIA.py
import csv
import datetime
# Se usa para poder usar expresiones regulares.
import re
# Libreria  necesaria para usar el sistema operativo.
import os
# Se importan las clases de clasePIA.
from clasePIA import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter
# Función que sirve para mostrar los elementos de la lista de ejemplos.
def NumdeElementos():
    txt = "Los elementos de la coleccion son {}"
    print(txt.format(len(Contactos)))

def BscTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BscContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.TELEFONO==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

Contactos = []
# Se declara una lista que va a almacenar objetos, en un inicio esta vacia.
NumdeElementos()

# Se agregaran objetos que estaran en esta lista.
Contactos.append(Contacto("01CV","Carlos Valadez","carlosvz@unal.edu.mx",8126432187,datetime.date(year=2000,month=4,day=10),1700))
Contactos.append(Contacto("02FE","Franco Escalon","fcoescalon@unal.edu.mx",8113459378,datetime.date(year=2001,month=7,day=12),1900))
NumdeElementos()


# Se define una función utilizando la expresión lambda, para facilitar el procedimiento.
LimPantalla = lambda: os.system('cls')

# Valida expresiones regulares.
# _txt es el texto que se va a validar.
# _regex es el patrón de expresión regular a validar.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimPantalla()
        print("LISTA DE CONTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(Contactos[indice_obtenido].TELEFONO)
                    print(Contactos[indice_obtenido].NOMBRE)
                    print(Contactos[indice_obtenido].CORREO)

            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Modo en que se ordena.
                Contactos.sort(key=attrgetter("TELEFONO"),reverse=False)
                # Barrido en secuencia.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(contacto.NICKNAME)
                    print(contacto.NOMBRE)
                    print(contacto.CORREO)
                    print(contacto.TELEFONO)
                    print(contacto.FECHANACIMIENTO)
                    print(contacto.GASTO)
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()
