#Documentacion
#  https://python-telegram-bot.readthedocs.io
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.keyboardbutton.html
#  https://github.com/nicosiebert2 siganme para mas guias


#Librerias
import logging # Login
from telegram import KeyboardButton, ReplyKeyboardMarkup #Teclado
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext #Token y comandos

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()

    #"""vamos a definir el teclado start en la variable respuesta_teclado"""
respuesta_teclado = [['Numeros', 'Colores'],['Paises']]

    #"""ahora definimos el reply_markup en la variable markup"""
markup = ReplyKeyboardMarkup(respuesta_teclado, one_time_keyboard = True, resize_keyboard= True)


#Funcion Start
def start(update, context):
    update.message.reply_text(
        'seleccione un boton',
        reply_markup = markup
    )

#Funcion de los botones start
def seleccion(update, context:CallbackContext):
    #Guardamos la seleccion en la variable texto
    text = update.message.text
    context.user_data['choice'] = text
    #vamos usar "if" para definir que van a hacer los botones

    if text == "Numeros":
        Numeros(update)
        Volver_boton(update)

    if text == "Colores":
        Colores(update)
        Volver_boton(update)

    if text == "Paises":
        update.message.reply_text("Esté boton no tiene ninguna funcion")
        Volver_boton(update)

#definimos la funciones de los botones "Numeros, Colores y Paises"
def Numeros(update):
    update.message.reply_text("La funcion de este boton no esta definida")
    
def Colores(update):
    update.message.reply_text("La funcion de este boton no esta definida")
    
def Paises():
    pass

#definimos el BotonVolver
def Volver_boton(update):
    reply_volver =[["Volver"]]
    markup_volver= ReplyKeyboardMarkup(reply_volver, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("👀👀" ,reply_markup =markup_volver)

# Definimos la funcion del boton volver que nos va a regresar al inicio
def VolverFuncion(update, context):
    start(update, context)

#para enlazar el token y añadir comandos
updater = Updater("1947126220:AAGCjUQp9iYNP40mnmaFBndHLLCRBQ4YyQw")

#Comandos|Controladores|Handlers
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

#añadimos un MessageHandler para controlar la funcion botones
dp.add_handler(MessageHandler(
    #dentro añadimos los Filter.regex para definirlos filtros de texto entre " '^ $' " y separados por "|" y su respectiva funcion
            Filters.regex('^Numeros|Colores|Paises$'), seleccion
            )
)
#un MessageHandler del boton Volver
dp.add_handler(MessageHandler(Filters.regex('^Volver$'), VolverFuncion))

#Mantener y poder terminar la sesion
updater.start_polling()
updater.idle()