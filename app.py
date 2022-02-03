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

@app.route("/sms", methods=['GET'])
def prueba():
    mensa = "Hola"
    return str(mensa)

"""
Se mapea un dirección URL a una función. Se realiza un routing.
"""
@app.route("/sms", methods=['POST'])
# Se define el comportamiento de la respuesta.
def reply():
    
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "Hola" in incoming_msg:
        reply = "Hola! \n¿Quiere emplear el Kairós-bot?"
        message.body(reply)
        responded = True

    if len(words) == 1 and "Si" in incoming_msg:
        reminder_string = "Provee una fecha en el siguiente formato.\n\n"\
        "*Date @* _type the date_ "
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "No" in incoming_msg:
        reply="Ok. Tenga un buen día!"
        message.body(reply)
        responded = True
    
    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()
        if input_type == "date":
            reply="Provee un mensaje en el siguiente formato.\n\n"\
            "*Reminder @* _type the message_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True
        if input_type == "reminder":
            reply="Your reminder is set!"
            set_reminder_body(input_string)
            message.body(reply)
            responded = True
        
    if not responded:
        message.body('Formato incorrecto. Por favor, ingrese nuevamente la información.')
    
    return str(response)
    
def set_reminder_date(msg):
    p= parse(msg)
    date=p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0
    
def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0
    
# Aplicación
if __name__ == "__main__":
    app.run(port=5000, debug=True)
