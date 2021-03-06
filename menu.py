from os import system
from xlrd import open_workbook

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
            path = "data/personas.xlsx"

            wb = open_workbook(path)
            sh1 = wb.sheet_by_index(0)
            for i in range(sh1.nrows):
                print(sh1.cell_value(i, 0) + "      " + sh1.cell_value(i, 1) + "        " + sh1.cell_value(i, 2))
            input ("Presione cualquier letra para regresar al menu ")
            system ('cls')
        if (operacion == 'b'):
            print ("seleccionó la opcion b", sep='\n')
            path = "data/libros.xlsx"

            wb = open_workbook(path)
            sh1 = wb.sheet_by_index(0)
            for i in range(sh1.nrows):
                print(sh1.cell_value(i, 0) + "      " + sh1.cell_value(i, 1))
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