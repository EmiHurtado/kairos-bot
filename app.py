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
    support2 = incoming_msg2.split(" ")
    response = MessagingResponse()
    print(incoming_msg)
    message = response.message()
    responded = False
    # words = incoming_msg.split('@')

    # Saludo inicial
    if "hola" in incoming_msg:
        reply = "¡Hola! \nBienvenido al Kairós Bot. \nElija una de las siguientes opciones, escribiendo sólo el número. \n"\
        "1.- Postularme.\n2.- Ver mi seguimiento.\n3.- Contactar un reclutador."
        message.body(reply)
        responded = True
    
    elif incoming_msg[0] == "h":
        upHora(support2[1])
        reply = "Muchas gracias por su tiempo. Esperamos contactar con usted pronto."
        message.body(reply)
        responded = True 
    
    elif incoming_msg[0] == "f":
        upFecha(support2[1])
        reply = "Ahora la hora de la siguiente manera: H 3:57PM"
        message.body(reply)
        responded = True 
    
    elif incoming_msg[0] == "v":
        upCV(support2[1])
        reply = "Muy bien. Por último, deseamos saber una fecha y hora en la que esté disponible para contactarlo:\n"\
        "Primero, envíe la fecha de la siguiente manera: F 25/02/2022"
        message.body(reply)
        responded = True 
        
    elif incoming_msg[0] == "n":
        argumento = support2[1] + " " + support2[2]
        upNombre(argumento)
        reply = "Gracias. Ahora mande el link de su CV (puede subirlo a Google Drive y compartirnos el link) de la siguiente forma únicamente:\n"\
        "V https://drive.google.com/file/d/1DHl59LeHzLxmG9w_rsBwAJY-y8rG7dfz/view?usp=sharing"
        message.body(reply)
        responded = True 
    
    elif incoming_msg[0] == "t" or incoming_msg[0] == "c":
        reply = recuperador(support2[1])
        message.body(reply)
        responded = True 
    
    elif incoming_msg == "1":
        reply = "Mande por este medio su nombre completo de la siguiente forma únicamente:\n"\
        "N Emiliano Hurtado"
        message.body(reply)
        responded = True
    
    elif incoming_msg == "2":
        reply = "Ingrese el número telefónico o correo electrónico que proporcionó en su postulamiento, "\
        "de la siguiente forma únicamente: T 5547836842 o C emhurtadom@outlook.com"
        message.body(reply)
        responded = True
    
    elif incoming_msg == "3":
        reply = reclutador()
        message.body(reply)
        responded = True
        
    # Mensaje alterno si no se ingresa correctamente la información.
    if not responded:
        # print("why", input_type)
        message.body('No logro entender. Intente de nuevo.')
    
    return str(response)

# Aplicación
if __name__ == "__main__":
    app.run(debug=True)
    
