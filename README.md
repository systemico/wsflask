# wsflask
Flask application like reference to develop projects on Systemico.
Aplicación Flask que se debe tomar como referencia para el desarrolló de módulos en Systemico.

# Instalar requisitos de entorno
pip install -r requirements.txt

# Generando el archivo de configuración
Todos las variables de configuración están definidas en el archivo *config/.env* y se debe
modificar con los datos requeridos.

# Ejecutar el servicio
python application.py

# Crear nuevo módulo en 5 pasos sencillos.
Los pasos para crear el módulo son:
1. Renombrar la carpeta *module* teniendo en cuenta el nombre del módulo a desarrollar.
2. Renombré el blueprint en el archivo *main.py* teniendo en cuenta el nombre del modulo a desarrollar.
3. Renombre el módulo en cada uno de los ENDPOINT creados por ejemplo *@module.route('/')*  por *@mi_modulo.route('/')*.
4. Actualice el archivo *application.py* para ajustar el import teniendo en cuenta el nombre del módulo a desarrollar.
5. En la línea 6 *application.register_blueprint(module, url_prefix='/module')* modifique la palabra module teniendo en cuenta el nombre del módulo a desarrollar.

# Requerimientos para instalación
Establecer todos los requerimientos de instalacion en *requirements.txt*.

## Ejemplo de archivo requirements.txt
    Flask==1.1.2
    flask-cors
    pymysql
    requests
    datetime

## Configuración de variables de entorno
Todas las variables de entorno se van a manejar en
**config/conf.env** y se utilizará el modelo de variables ENV
para registrar todas las variables, no debe existir ninguna
variable de entorno creda en ningún otro lado.

### Ejemplo de variables de entorno establecidas en la variable .env
    USUARIO_BD=wsflask
    CLAVE_BD=wsflask
    URL_BD=bd.wsflask.com
    NOMBRE_BD=wsflask
    # Usuarios Testing
    DEFAULT_ID=1

## Ejecutando la base de datos Mysql
cd db/mariadb
docker-compose build && docker-compose up -d

## Ejecutando la base de datos PostgreSQL
cd db/postgres
docker-compose build && docker-compose up -d
