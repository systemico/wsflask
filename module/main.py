from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import logging

# Cambiar el single page por el nombre del modulo que se esta creando
module = Blueprint('module', __name__,
                    template_folder='templates',
                    static_folder='static')


@module.route('/')
def iniciar():
    '''
    Método inicial del módulo.
    :return:
    '''
    try:
        return render_template('index.html')
    except Exception as exp:
      # GUARDAMOS LA EXCEPCION EN EL LOG ASOCIADO A LA APLIACIÓN Y CONFIGURADO EN STARTUP.
      logging.error(exp)
      return render_template('404.html')
      abort(404)
