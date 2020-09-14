from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Cambiar el single page por el nombre del modulo que se esta creando
module = Blueprint('module', __name__,
                    template_folder='templates',
                    static_folder='static')

@module.route('/')
def iniciar():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)