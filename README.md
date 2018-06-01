# Módulo 3: Integración Telegram.
### **infoecoVLC**
### **Asistente virtual para información económica municipal**

Modulo responsable de gestionar todos los mensajes que se reciben de Telegram. Se comunica con el módulo 2 (agente inteligente) para obtener la respuesta para el usuario. Si quieres más información entra al proyecto **[infoecoVLC: Asistente virtual para información económica municipal](https://github.com/areahackerscivics/infoecoVLC)**

## Descripción

![Diseño de comunicacion](https://github.com/ricardocancar/chatbot_v1/blob/master/imagen/Diagrama_M3-ChatBot.png)


## Guía de uso

### Lenguaje de programación
Python 3.6.3

### Librerías empleadas
Las librerías actualizadas siempre estarán actualizadas en el documento [**requirements.txt**](./requirements.txt) consultar en caso de errores.

    pymongo = 3.6.0
    python-telegram-bot = 9.0.0
    requests = 2.18.4

## Herramientas usadas para tener en funcionamiento el Bot
- Api de Telegram.
- MongoDB.
- Instancia EC2 AWS.
- Python.

## Justificación

Se usó la plataforma de Telegram, debido al gran número de usuario con lo que cuenta esta aplicación ademas de la facilidad con la que permite desarrollar bots a los usuarios de su plataforma con su API. 

MongoDB, permite almacenar datos en forma de documentos de manera no estructurada de manera consistente.

Se usó el lenguaje Python  de programación la cuál cuenta con una serie de librerías que facilitan el desarrollo de este proyecto.

- python-telegram-bot esta librería provee una interfaz de Python a la API de bot telegram, esta librería también cuenta con característica que facilitan el desarrollo de bots.

- pymongo librería de Python que permite realizar gran parte de las operaciones que se pueden hacer directamente desde la interfaz de mongodb.

- requests, permite hacer solicitudes GET and POST a paginas web.

- bs4, estandar en Python para realizar Scrapping en paginas web.

El InfoecoVLC bot está corriendo en una instancia EC2, el cual es un servicio muy practico de AWS que ofrece poder de computo como servicio ademas teda la posibilidad de aumentar la capacidad de computo de la instancia dependiendo del la demanda que tenga tu aplicación.

### Instalación

**Pasos**
1. Descargar desde github el proyecto.

        sudo git clone https://github.com/areahackerscivics/Chatbot_M3_Infoeco

2. Entramos en la carpeta descargada que contiene el proyecto.

        cd Chatbot_M3_Infoeco

3. Instalamos virtaulenv.
        
        sudo apt-get install python-virtualenv virtualenv
   o
        sudo pip install virtualenv

4. Creamos un entorno virtual con python3. 
 
        virtualenv env --python=python3

Este comando crea el directorio env con la siguiente estructura.

        env/
           bin/
           include/
           lib/
              site-packages/

En el directorio **bin/** se encuentran los ejecutables necesarios para interactuar con el entorno virtual. 
En el directorio **include/** se encuentran algunos archivos de cabecera de C (cuya extensión es *.h) necesarios para compilar algunas librerías de Python.

Finalmente, en el directorio **lib/** se encuentra una copia de la instalación de Python así como un directorio llamado **site-packages/** en donde se almacenan los paquetes Python instalados en el entorno virtual.

5. Instalamos las librerías de Python necesarias.
    
        pip install -r requirements.txt

6. Activamos el ambiente virtual.
 
        source env/bin/activate
        "si lo queremos desactivar"
        (env)$ deactivate

7. Cambiamos el  nombre de variables_ejemplo.py por **variables.py**.

        sudo mv variables_ejemplo.py variables.py

8. Sustituir las “XXX” de dentro de **variables.py** por las variables personales.

        sudo nano variables.py

9. Descargar desde github el proyecto.
   
        sudo git clone https://github.com/areahackerscivics/Chatbot_M1_Extraccion_y_Almacenamiento

10. Seguir los pasos mostrados en la [guía](https://github.com/areahackerscivics/Chatbot_M1_Extraccion_y_Almacenamiento.) para la creación de una base de datos en Mongodb (importante tener Mongodb en el sistema operativo).
  
11. Del [modulo 2 Api.ia](https://github.com/areahackerscivics/Apiai_M2_infoecoVLC)
        
        cd git clone https://github.com/areahackerscivics/Apiai_M2_infoecoVLC

12. Revisamos La [guía](https://github.com/areahackerscivics/Apiai_M2_infoecoVLC) de este modulo.

13. Ejecutamos un screen para mantener la aplicación en ejecución.
       
        screen 

14. Ejecutamos el script de Python dentro del screen.
        
        python3 chat_bot.py


## Colaboración
Se puede colaborar:
- Difundiendo.
- Ampliando o modificando el proyecto.

## Términos de uso

El contenido de este repositorio está sujeto a la licencia [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

![](https://www.gnu.org/graphics/gplv3-127x51.png)

