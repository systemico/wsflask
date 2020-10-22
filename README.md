# wsflask
Flask application like reference to develop projects on Systemico.
Aplicación Flask que se debe tomar como referencia para el desarrolló de módulos en Systemico.

# Ejecutar el servicio
python application.py

# Crear nuevo módulo en 5 pasos sencillos.
Los pasos para crear el módulo son:
1. Renombrar la carpeta *module* teniendo en cuenta el nombre del módulo a desarrollar. 
2. Renombré el blueprint en el archivo *main.py* teniendo en cuenta el nombre del modulo a desarrollar.
3. Renombre el módulo en cada uno de los ENDPOINT creados por ejemplo *@module.route('/')*  por *@mi_modulo.route('/')*.
4. Actualice el archivo *application.py* para ajustar el import teniendo en cuenta el nombre del módulo a desarrollar.
5. En la línea 6 *application.register_blueprint(module, url_prefix='/module')* modifique la palabra module teniendo en cuenta el nombre del módulo a desarrollar.

# Requerimientos para instalacion
Establecer todos los requerimientos de instalacion en *requirements.txt*.

## Ejemplo de archivo requirements.txt
Flask==1.1.2  
flask-cors  
pymysql  
requests  
datetime  
