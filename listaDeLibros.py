from cargarDatos import cargar_lista_de_libros, cargar_lista_de_personas
from utils import imprimir_libro, imprimir_persona

def mostrar_titulo():
    print("*********************************************")
    print("**             Lista de libros             **")
    print("*********************************************")

def imprimir_lista_de_libros():
    lista_de_libros = cargar_lista_de_libros()
    mostrar_titulo()
    print(*map(imprimir_libro, lista_de_libros))