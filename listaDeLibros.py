from xlrd import open_workbook

def imprimir_lista_de_libros():
    path = "data/libros.xlsx"
    wb = open_workbook(path)
    sh1 = wb.sheet_by_index(0)
    for i in range(sh1.nrows):
        print(sh1.cell_value(i, 0) + "      " + sh1.cell_value(i, 1))