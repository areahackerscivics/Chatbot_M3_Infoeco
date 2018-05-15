#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
dicVal = {
# telegram.py //////////////////////////////////////////////////////////////////
    "botInactivo": "Huy, ara mateix estic en manteniment! Torna a parlar-me més tard per favor.",
    "comandoStart": "Hola, és la primera vegada que entres. En quin idioma vols que em comunique amb tu?",
    "comandoIdioma": "En quin idioma vols que em comunique amb tu a partir d'ara?",
    "usuarioNoGuardado": "Hola sembla que hi ha hagut un error i no tinc emmagatzemat que idioma vols que em comunique amb tu. M'ho podries recordar?",
    "errorNoTexto": "Perdona però no entenc aquest tipus de missatges.",
    "errorNoResult":"no hem trobat el nom a la base de dades, revisa que estigui ben escrit",
    "errorManyResult":"Hi ha més d'un alt càrrec amb aquest nom, si pots col·loca el nom complet per respondre't.",
    "error.Connection":"Disculpes tenim problemes per trobar les respostes.",
# busquedaRespuesta.py /////////////////////////////////////////////////////////
    "resErrorRespApiai": 'El servei està caigut ara mateix, torna a intentar-ho més tard.',
    "resErrorRespWH": "Ops! Les dades no estan disponibles en aquests moments. Torna a manar la teua pregunta en uns pocs minuts, per favor.",
    "resErrorano": "no tenim els {} de l'{} any. de moment només comptem amb els impost de l'any 2016",
    "errorImpRes":"disculpa no Podem donar-te una resposta",
    "resComplemento.Saludo": "Bon dia!",
    "resinput.unknown": "Huy! Aquesta pregunta no la tenia contemplada.",
    "res.Salario": ["{} guanya {}€ de retribució anual bruta (sense antiguitat) pel seu càrrec de {}.",
                   "un {} guanya {}€ de retribució anual bruta (sense antiguitat)"],
    "res.Impuesto":"al barri {} va pagar en total {} l'any {}.",
    "error.Salario": "¿Revisaste que aquest ben escrit el nom?",
                    
# botonesTeclados.py ///////////////////////////////////////////////////////////
    "pulsarBotonIdioma": "Guardat en memòria.",
    "respuestaCambioIdioma": "A partir d'ara les comunicacions seran en valencià.",
    "respuestaCambioIdiomaError": "No s'ha pogut desar el canvi ara mateix, torna a intentar-ho més tard si us plau."
}

dicCast = {
# telegram.py //////////////////////////////////////////////////////////////////
    "botInactivo": "¡Huy, ahora mismo estoy en mantenimiento! Vuelve a hablarme más tarde por favor.",
    "comandoStart": 'Hola, es la primera vez que entras. ¿En qué idioma quieres que me comunique contigo?',
    "comandoIdioma": "¿En qué idioma quieres que me comunique contigo a partir de ahora?",
    "usuarioNoGuardado": 'Hola parece que ha habido un error y no tengo almacenado en que idioma quieres que me comunique contigo. ¿Me lo podrías recordar?',
    "errorNoTexto": "Perdona pero no entiendo este tipo de mensajes.",
    "errorNoResult":"no se encontró el nombre en la base de datos, revisa que este bien escrito",
    "errorManyResult":"Hay más de un alto cargo con ese nombre, si puedes coloca el nombre completo para respoderte!",
    "error.Connection":"Disculpas tenemos problemas para encontrar las respuestas.",
# busquedaRespuesta.py /////////////////////////////////////////////////////////
    "resErrorRespApiai": 'El servicio esta caído ahora mismo, vuelve a intentarlo más tarde.',
    "resErrorRespWH": "¡Ops! Los datos no están disponibles en estos momentos. Vuelve a mandar tu pregunta en unos pocos minutos, por favor.",
    "resErrorano": "no tenemos los impuesto del {} año. de momento solo contamos con los impuesto del año 2016",
    "errorImpRes":"disculpa no podemos darte una respuesta",
    "resComplemento.Saludo": "¡Buenos días!",
    "resinput.unknown": "¡Huy! Esa pregunta no la tenía contemplada.",
    "res.Salario": ["{} gana {}€ de retribución anual bruta (sin antigüedad) por su cargo de {}.",
                    "un {} gana {}€ de retribución anual bruta (sin antigüedad)"],
    "res.Impuesto":"el barrio {} pago en total {} en {} el año {}",
# botonesTeclados.py ///////////////////////////////////////////////////////////
    "pulsarBotonIdioma": 'Guardado en memoria.',
    "respuestaCambioIdioma": 'A partir de ahora las comunicaciones serán en castellano.',
    "respuestaCambioIdiomaError": 'No se pudo guardar el cambio en estos momentos, vuelve a intentarlo más tarde por favor.'
    
}

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Función
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def respuesta_bot(key,idioma):
    if idioma == 'Val':
        text = dicVal[key]

    else:
        text = dicCast[key]

    return text
