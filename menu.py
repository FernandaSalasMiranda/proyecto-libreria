from os import system
from listaDePersonas import imprimir_lista_de_personas
from listaDeLibros import imprimir_lista_de_libros

def menu ():
    menu = """
    -Menu del sistema
    -Opcion a: lista de personas 
    -Opcion b: lista de libros 
    -Opcion c: Imprimir registro de lista de persona
    -Opcion d: Ver lista de libros
    -Opcion e: Buscar libro
    -Opcion f: Prestar libro
    -Opcion g: Ver prestamo de libros
    """ 
    while True:
        print (menu)
        operacion = input("Seleccione una opción: ")
        if (operacion == 'a'):
            print ("seleccionó la opcion a", sep='\n')
            imprimir_lista_de_personas()
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')
        if (operacion == 'b'):
            print ("seleccionó la opcion b", sep='\n')
            imprimir_lista_de_libros()
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')      
       
        if (operacion == 'c'):
            system ('cls')
            print ('nos vemos!!')
            break
        else: 
            system ('cls')
            input ("opcion invalida")
            system ('cls')

menu ()