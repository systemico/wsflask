from flask import Flask, request
from module.main import module

application = Flask(__name__)
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