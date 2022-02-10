# Librerías
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

from dateutil.parser import parse

"""
Se crea el objeto de la aplicación Flask, que contiene los datos
de la app y métodos que le dicen a la aplicación que hacer. 
"""
app = Flask(__name__)
count=0

# Mensaje de prueba
@app.route("/sms", methods=['GET'])
def prueba():
    mensa = "Hola"
    return str(mensa)

# Se mapea un dirección URL a una función. Se realiza un routing.
@app.route("/sms", methods=['POST'])
def reply(): # Se define el comportamiento de la respuesta.
    
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hola" in incoming_msg:
        reply = "¡Hola! \nBienvenido al Kairós Bot. \nAquí podrás ver tu estado de reclutamiento. \nResponda 'Si', si quiere continuar."
        message.body(reply)
        responded = True

    if len(words) == 1 and "si" in incoming_msg:
        reminder_string = "Por favor, entregue la información en el siguiente formato.\n\n"\
        "*Fecha @* _dia/mes/año_ "
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "no" in incoming_msg:
        reply="Ok. ¡Tenga un excelente día!"
        message.body(reply)
        responded = True
    
    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()
        if input_type == "fecha":
            reply="Por favor, entregue la información en el siguiente formato.\n\n"\
            "*Recordatorio @* _mensaje_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True
        if input_type == "recordatorio":
            print("yuhu")
            reply="¡Su recordatorio está listo!"
            set_reminder_body(input_string)
            message.body(reply)
            responded = True
        
    if not responded:
        print("why", input_type)
        message.body('Formato incorrecto. Por favor, ingréselo en el formato correcto.')
    
    return str(response)
    
def set_reminder_date(msg):
    p= parse(msg)
    date=p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0
    
def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0
    
     
    return reminder_message

# Aplicación
if __name__ == "__main__":
    app.run(debug=True)
    
