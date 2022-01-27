# Librerías
import gspread
from oauth2client.service_account import ServiceAccountCredentials

"""
Se autentifica y permite el acceso a las hojas de datos.
"""
s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name("credentials.json",s)
client=gspread.authorize(creds)

# Se accede a la hoja de datos para guardar información.
sheet = client.open("Reminders").sheet1
row_values=sheet.row_values(1)
col_values=sheet.col_values(1)
row_filled=len(col_values)
col_filled=len(row_values)

"""
Se definen las funciones para guardar datos.
"""
def save_reminder_date(date):

    sheet.update_cell(row_filled+1, 1, date)
    print("Fecha guardada!")
    return 0
    
def save_reminder_body(msg):

    sheet.update_cell(row_filled+1, 2, msg)
    print("Mensaje guardado!")
    return 0

