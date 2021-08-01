#Documentacion
#  https://python-telegram-bot.readthedocs.io
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.keyboardbutton.html
#  https://github.com/nicosiebert2 más repositorios


#Librerias
import os #variables de entorno
import logging # Login
from telegram import KeyboardButton, ReplyKeyboardMarkup #Teclado
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext #Token y comandos

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()

    #"""vamos a definir el teclado que va a aparecer en BotonesDinanicos en la variable respuesta_teclado como"""
respuesta_teclado = [['Numeros', 'Colores'],['Paises']]

    #"""ahora definimos el reply_markup en la variable markup y a la vez llamamos la variable que anteriormente definimos respuesta_teclado"""
markup = ReplyKeyboardMarkup(respuesta_teclado, one_time_keyboard = True, resize_keyboard= True)


#Funcion Start || btndimanicos
def start(update, context):
    nombre = update.effective_user['first_name']
    update.message.reply_text(f"Hola {nombre}👋\n Ingrese los siguientes comandos para ver las demostraciones /botonesdinamicos")
    update.message.reply_text("😊")

def BotonesDinamicos(update, context):
    update.message.reply_text(
        'seleccione un boton',
        reply_markup = markup
    )

#Funcion de los BotonesDinamicos
def seleccion(update, context:CallbackContext):
    #Guardamos la seleccion en la variable texto
    text = update.message.text
    context.user_data['choice'] = text
    #vamos usar "if" para definir que van a hacer los botones

    if text == "Numeros":
        Numeros(update)

    if text == "Colores":
        Colores(update, context)

    if text == "Paises":
        update.message.reply_text(f"{update.effective_user['first_name']} Esta funcion aún no está disponible 😔")
        Volver_boton(update)

#definimos la funciones de los botones "Numeros, Colores y Paises"
def Numeros(update):
    reply_numeros = [[1,2,3,4,5,6], [7,8,9,10, 11 ,12,], [ 13, 14, 15, 16, 17, 18], ['Volver']]
    markup_numeros = ReplyKeyboardMarkup(reply_numeros, one_time_keyboard = True, resize_keyboard=True)
    update.message.reply_text(
        "seleccione un numero",
        reply_markup = markup_numeros
    )
def NumerosFuncion(update, context):
    num_seleccionado = update.message.text
    print(f"El usuario {update.effective_user['first_name']} ha seleccionado el numero {num_seleccionado}")
    update.message.reply_text(f'Ha seleccionado el numero {num_seleccionado}')
    Volver_boton(update)
    
def Colores(update,context):
    reply_color = [['Rojo','Verde','Negro'], ['Azul', 'Amarillo', 'Blanco'],['Volver']]
    markup_colors = ReplyKeyboardMarkup(reply_color, one_time_keyboard = True, resize_keyboard=True)
    update.message.reply_text(
        "seleccione un color",
        reply_markup = markup_colors
    )
def ColoresFuncion(update,context):
    color_seleccionado = update.message.text
    print(f"El usuario {update.effective_user['first_name']} ha seleccionado el color", color_seleccionado)
    update.message.reply_text(f'Ha seleccionado el color {color_seleccionado}')
    Volver_boton(update)

def Paises():
    pass

#definimos el Boton para Volver
def Volver_boton(update):
    reply_volver =[["Volver"]]
    markup_volver= ReplyKeyboardMarkup(reply_volver, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("👀👀" ,reply_markup =markup_volver)

# Definimos la funcion del boton volver que nos va a regresar al inicio
def VolverFuncion(update, context):
    BotonesDinamicos(update, context)
def SourceCode(update):
    update.message.reply_text("Mi codigo fuente esta alojado en: ")
    update.message.reply_text("https://github.com/nicosiebert2/bot-btn/main/bot.py")
#para enlazar el token y añadir comandos
#si va a probar el cogigo borren la variable TUTOKEN y vambien TUTOKEN por su token
TUTOKEN = os.getenv("TUTOKEN")#borrar
updater = Updater("TUTOKEN")#añade tu token

#Comandos|Controladores|Handlers
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("botonesdinamicos", BotonesDinamicos))
dp.add_handler(CommandHandler("sourcecode", SourceCode))


#añadimos un MessageHandler para controlar la funcion botones
dp.add_handler(MessageHandler(
    #dentro añadimos los Filter.regex para definirlos filtros de texto entre " '^ $' " y separados por "|" y su respectiva funcion
            Filters.regex('^Numeros|Colores|Paises$'), seleccion
            )
)
#un MessageHandler del boton Volver|Colores|Numeros
dp.add_handler(MessageHandler(Filters.regex('^Volver$'), VolverFuncion))
dp.add_handler(MessageHandler(Filters.regex('^Rojo|Verde|Negro|Azul|Amarillo|Blanco|Volver$'), ColoresFuncion))
dp.add_handler(MessageHandler(Filters.regex('^1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16$'), NumerosFuncion))

#Mantener y poder terminar la sesion
updater.start_polling()
updater.idle()
