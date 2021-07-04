# flask-mvc-crud

> Un ejemplo de mvc en flask

Primero instala las depencias

```bash
pip install -r requirements.txt
```
## Creación 🔰
Se creo una variable de entorno usando
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
### Base de datos 🖥

```bash
# Creamos la carpeta migrations con una sub carpeta
flask db init
# detectamos cambios del modelo
flask db migrate
# aplicará los cambios de modelo que ha implementado.
flask db upgrade
```

🛑 Si algo saliera mal, puedes aplicar el siguiente comando para quitar los cambios del modelo

```bash
flask db downgrade
```

## MVC
### Models 📦
En la carpeta models, se ponen los modelos para poder manejar en nuestra base de datos.
### Controller 🎮
En la carpeta Controllers, es la logica de nuestro codigo que pide los datos del modelo y lo pone en las vistas que son los templates.
### Views 🖥
Son los templates donde se muestra todos los datos que recibe

## Carpetas adicionales 📂
### Routes
Las carpeta de routes son las rutas de nuestra aplicación, se usa blueprints para poder manejar mas sencilla la distribución de datos
### migrations
Se encuentra los cambios de la base de datos.

