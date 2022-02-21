# Librerías
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

# from dateutil.parser import parse

"""
Se crea el objeto de la aplicación Flask, que contiene los datos
de la app y métodos que le dicen a la aplicación que hacer. 
"""
app = Flask(__name__)
count = 0

# Mensaje de prueba
@app.route("/sms", methods=['GET'])
def prueba():
    mensa = "Hola"
    return str(mensa)

# Se mapea un dirección URL a una función. Se realiza un routing.
@app.route("/sms", methods=['POST'])
def reply(): # Se define el comportamiento de la respuesta.
    
    incoming_msg = request.form.get('Body').lower()
    incoming_msg2 = request.form.get('Body')
    response = MessagingResponse()
    print(incoming_msg)
    message = response.message()
    responded = False
    split = incoming_msg.split()
    # words = incoming_msg.split('@')

    # Saludo inicial
    if "hola" in incoming_msg:
        reply = "¡Hola! \nBienvenido al Kairós Bot. \nElija una de las siguientes opciones, escribiendo sólo el número. \n"\
        "1.- Postularme.\n2.- Ver mi seguimiento.\n3.- Contactar un reclutador."
        message.body(reply)
        responded = True

    elif split[0] == "T" or split[0] == "C":
        reply = recupera_local(incoming_msg2)
        message.body(reply)
        responded = True 
    
    elif "2" in incoming_msg:
        reply = "Ingrese el número telefónico o correo electrónico que proporcionó en su postulamiento, "\
        "de la siguiente forma únicamente: T 5547836842 o C emhurtadom@outlook.com"
        message.body(reply)
        responded = True
        
    # Mensaje alterno si no se ingresa correctamente la información.
    if not responded:
        # print("why", input_type)
        message.body('No logro entender. Intente de nuevo.')
    
    return str(response)

def recupera_local(nombre):
    val = recuperador(nombre)
    return val

# Aplicación
if __name__ == "__main__":
    app.run(debug=True)
    
