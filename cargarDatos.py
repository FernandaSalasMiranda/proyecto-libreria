from xlrd import open_workbook

def cargar_lista_de_personas(): 
    path = "data/personas.xlsx"
    wb = open_workbook(path)
    lista_de_personas = []
    sh1 = wb.sheet_by_index(0)
    for i in range(sh1.nrows):
        lista_de_personas.append({"id": sh1.cell_value(i, 0), "nombre": sh1.cell_value(i, 1), "correo": sh1.cell_value(i, 2)})
    return lista_de_personas


def cargar_lista_de_libros():
    path = "data/libros.xlsx"
    wb = open_workbook(path)
    sh1 = wb.sheet_by_index(0)
    lista_de_libros = []
    for i in range(sh1.nrows):
        lista_de_libros.append(
            {"id": str(sh1.cell_value(i, 0)), "titulo": str(sh1.cell_value(i, 1)), "genero": sh1.cell_value(i, 2),
             "autor": sh1.cell_value(i, 3)})
    return lista_de_libros