from cargarDatos import cargar_lista_de_personas
from utils import imprimir_nombre

def mostrar_titulo():
    print("*********************************************")
    print("**             Lista de personas           **")
    print("*********************************************")

def imprimir_lista_de_personas(ordenar_lista):
    lista_de_personas = cargar_lista_de_personas()
    mostrar_titulo()
    if(ordenar_lista):
        lista_ordenada = sorted(lista_de_personas, key=lambda persona: persona['nombre'])
        print(*map(imprimir_nombre, lista_ordenada))
    else:
        print(*map(imprimir_nombre, lista_de_personas))
