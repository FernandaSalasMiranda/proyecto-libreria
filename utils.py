def imprimir_nombre(val):
    return val["id"] + " - " + val["nombre"] + "\n"

def imprimir_persona(val):
    return val["id"] + " - " + val["nombre"] + " " + val["correo"] +"\n"

def imprimir_libro(val):
    return val["id"] + " - " + val["titulo"] + " " + val["genero"] + " " + val["autor"] + "\n"

def imprimir_prestamo(val):
    libro = val["libro"]
    persona = val["persona"]
    return "Se presto el libro: " + libro + " a " + persona
