from os import system
from listaDePersonas import imprimir_lista_de_personas
from listaDeLibros import imprimir_lista_de_libros,buscar_libro, prestar_libro, imprimir_libros_prestados


def menu ():
    menu = """
    -Menu del sistema
    -Opcion a: Lista de personas 
    -Opcion b: Ordenar lista de personas
    -Opcion c: Ver lista de libros
    -Opcion d: Buscar libro
    -Opcion e: Prestar libro
    -Opcion f: Ver prestamo de libros
    -Opcion g: Opcion para salir del programa 
    """ 
    while True:
        system("cls")
        print (menu)
        operacion = input("Seleccione una opción: ")
        if (operacion == 'a'):
            system ('cls')   
            print ("seleccionó la opcion a", sep='\n')
            imprimir_lista_de_personas(ordenar_lista=False)
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')
        if (operacion == 'b'):
            system ('cls')   
            print ("seleccionó la opcion b", sep='\n')
            imprimir_lista_de_personas(ordenar_lista=True)
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')    
        if (operacion == 'c'):
            system ('cls')   
            print ("seleccionó la opcion c", sep='\n')
            imprimir_lista_de_libros()
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')    
        if(operacion== "d"):
            system ('cls')  
            val = input("Ingrese el id, nombre, genero o autor del libro: ") 
            buscar_libro(val)
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')  
        if(operacion== "e"):
            system ('cls')  
            print("prestar libro")
            idLibro = input("Ingrese el id del libro: ") 
            idPersona = input("Ingrese el id de la persona: ") 
            prestar_libro(idLibro, idPersona)
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')   
        if(operacion== "f"):
            system ('cls')  
            print("libros prestados")
            imprimir_libros_prestados()
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls') 
        if (operacion == 's'):
            system ('cls')
            print ('nos vemos!!')
            break
        else: 
            system ('cls')
            input ("opcion invalida")
            system ('cls')

menu ()