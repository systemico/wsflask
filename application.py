from flask import Flask, request
from module.main import module
from flask_sslify import SSLify
from flask_cors import CORS
from config.startup import Startup
import logging
# Rut apara la carga de archivos.
UPLOAD_FOLDER = '/var/tmp/'
# Extensiones permitidas para subir
ALLOWED_EXTENSIONS = {'csv'}
# Establecemos la configuracion del Log
logging.basicConfig(filename='/var/tmp/wsflask.log', level=logging.DEBUG)

# Cargamos la aplicación Flask.
application = Flask(__name__)
sslify = SSLify(application)
cors = CORS(application, resources={r"/*": {"origins": "*"}})
# Registramos el module.
application.register_blueprint(module, url_prefix='/module')

'''
ENDPOINT de inicio de la application.
'''
@application.route('/')
def iniciar():
    # Crear las variables de sesion que requiera el proyecto.
    return 'Bienvenidos al proyecto!'

if __name__ == '__main__':
    application.run()
    application.debug = True
