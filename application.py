from flask import Flask, request, render_template
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

@application.route('/')
def iniciar():
    '''
    Permite manera la carga de la primera version de la aplciación.
    :return:
    '''
    return render_template('bienvenida.html')


@application.errorhandler(404)
def page_not_found(e):
  '''
  Permite el manejo detallado de errores 404 en toda la aplicación.
  :param e:
  :return:
  '''
  logging.warning(e)
  return render_template('404.html'), 404

@application.errorhandler(500)
def server_error(e):
  '''
  Permite el de los errores que hagan fallar el servidor.
  :param e:
  :return:
  '''
  logging.error(e)
  return render_template('500.html'), 500

# SE EJECUTA CUANDO SE LLAMA ESTE ARCHIVO COMO PRINCIPAL
if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')

