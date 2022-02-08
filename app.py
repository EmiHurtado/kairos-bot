
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

from dateutil.parser import parse


app = Flask(__name__)
count=0


@app.route("/sms", methods=['POST'])
def reply():
    
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hola" in incoming_msg:
        reply = "¡Hola! \nBienvenido al Kairós Bot. \nAquí pordrás ver tu estado de reclutamiento. \nResponda 'Si', si quiere continuar."
        message.body(reply)
        responded = True

    if len(words) == 1 and "si" in incoming_msg:
        reminder_string = "Por favor, entregue la información en el siguiente formato.\n\n"\
        "*Date @* _Escriba la fecha_ "
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "no" in incoming_msg:
        reply="Ok. ¡Tenga un excelente día!"
        message.body(reply)
        responded = True
    
    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()
        if input_type == "date":
            reply="Por favor, entregue la información en el siguiente formato.\n\n"\
            "*Reminder @* _type the message_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True
        if input_type == "reminder":
            print("yuhu")
            reply="Your reminder is set!"
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


if __name__ == "__main__":
    app.run(debug=True)
    
