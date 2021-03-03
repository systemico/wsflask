import os
import os.path
from dotenv import load_dotenv
import json
import logging

'''Clase que permite cargar la configuracion inical de Wabot'''
class Startup:
    '''Listado de Metodos'''
    def iniciar(self):
        dir = os.path.dirname(__file__)
        # Cargamos las variables del entorno.
        if os.path.isfile(dir+'/.env'):
          env_path = dir+'/.env'
          load_dotenv(dotenv_path=env_path)
        # Creamos el archivo de variables de entorno para diligenciarlo.
        else:
          # Open Json Variables
          with open(dir+'/conf.json') as json_file:
            data = json.load(json_file)
            variables = data['variables']
            lvariables = variables.split(",")
            fenv = open(dir+"/.env", "w")
            # Almacenando las variables en el archivo .env
            for variable in lvariables:
              variable_env=str(os.getenv(variable))
              if variable_env=='None':
                fenv.write(str(variable)+"=\n")
              else:
                fenv.write(str(variable) + "=" + variable_env+"\n")
            fenv.close()

ostartup = Startup()
ostartup.iniciar()
