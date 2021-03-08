from cargarDatos import cargar_lista_de_libros, cargar_lista_de_personas
from utils import imprimir_libro, imprimir_persona, imprimir_prestamo

def mostrar_titulo():
    print("*********************************************")
    print("**             Lista de libros             **")
    print("*********************************************")

def imprimir_lista_de_libros():
    lista_de_libros = cargar_lista_de_libros()
    mostrar_titulo()
    print(*map(imprimir_libro, lista_de_libros))


def buscar_libro(val):
    lista_de_libros = cargar_lista_de_libros()
    resultado = filter(lambda libro: val in libro['id'].lower() or val in libro["titulo"].lower() or val in libro["genero"].lower() or val in libro["autor"].lower(), lista_de_libros)
    print(*map(imprimir_libro, resultado))

libros_prestados = []

def prestar_libro(idLibro, idPersona):
    lista_de_libros = cargar_lista_de_libros()
    lista_de_personas = cargar_lista_de_personas()

    persona = list(map(imprimir_persona,  filter(lambda persona: persona["id"]  == idPersona, lista_de_personas)))[0]

    libro = list(map(imprimir_libro, filter(lambda libro: libro["id"] == idLibro, lista_de_libros)))[0]


    # Chequear si libro o persona no tienen elementos
    if(len(persona) > 0 and len(libro) > 0):
        print("Se presto el libro: " + libro + " a " + persona)
        libros_prestados.append({"libro": libro, "persona": persona})
    else:
        print("No se encontraron regitros para los ids ingresados")



def imprimir_libros_prestados():
    print(*map(imprimir_prestamo, libros_prestados))