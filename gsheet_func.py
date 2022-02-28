# Librerías
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

# Se autentifica y permite el acceso a las hojas de datos.
s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name('credentials.json',s)
client=gspread.authorize(creds)

# Se accede a la hoja de datos para guardar información.
sheet = client.open("Data_Base").sheet1
sheet2 = client.open("Data_Base").worksheet("Hoja 2")
sheet3 = client.open("Data_Base").worksheet("Hoja 3")

# Define las casillas ya ocupadas
row_values = sheet3.row_values(1)
col_values = sheet3.col_values(1)
row_filled = len(col_values)
col_filled = len(row_values)

# Se definen las funciones para recuperar datos.
def recuperador(nombre):
    
    # Encuentra la celda requerida
    print(nombre)
    cell = sheet.find(nombre)

    # Imprime la información deseada
    if cell != None:
        if cell.col == 1:
            val1 = sheet.cell(cell.row, cell.col + 3).value
            val2 = sheet.cell(cell.row, cell.col + 4).value
        elif cell.col == 2:
            val1 = sheet.cell(cell.row, cell.col + 2).value
            val2 = sheet.cell(cell.row, cell.col + 3).value
        print("Usted está", val1, val2)
        return "Usted está " + val1 + "\nFeedback: " + val2

    else:
        return "No se pudo encontrar. Contáctese con RH."
    
# Se definen las funciones para recuperar datos.
def reclutador():
    
    # Genera un número aleatorio.
    n = random.randint(2,17)

    # Encuentra al reclutador y devuelve su información.
    nombre = sheet2.cell(n, 3).value
    numero = sheet2.cell(n, 10).value
    
    return nombre + " se contactará con usted. Este es su número telefónico: " + numero

# Funciones para guardar los datos
def upNombre(nombre):

    sheet3.update_cell(row_filled+1, 1, nombre)
    print("Nombre listo")
    return 0
    
def upCV(CV):

    sheet3.update_cell(row_filled+1, 2, CV)
    print("CV listo")
    return 0

def upFecha(fecha):

    sheet3.update_cell(row_filled+1, 3, fecha)
    print("Fecha lista")
    return 0

def upHora(hora):

    sheet3.update_cell(row_filled+1, 4, hora)
    print("Hora lista")
    return 0
