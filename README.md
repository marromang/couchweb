# couchweb
***
Aplicación web para la gestión de las copias de seguridad y la monitorización del entorno creado para CouchBase.

Está escrita en python usando el framework ligero Bottle y usando un entorno virtual.

Obviando los directorios y ficheros dedicados a estilos propios de la plantilla, la estructura de la aplicación es:

	couchbase
	├── LICENSE
	├── README.md
	├── requirements.txt
	└── web
		├── app.wsgi
		├── footer.tpl
		├── header.tpl
		├── index.tpl
		├── main.py
		└── static
			├── pages
			│	├── backups
			│	│	├── backups.tpl
			│	│	├── nuevo2.tpl
			│	│	├── nuevo.tpl
			│	│	├── restaurar2.tpl
			│	│	├── restaurar3.tpl
			│	│	└── restaurar.tpl
			│	├── docs.tpl
			│	└── monitorización
			│		├── jarvis.tpl
			│		└── monitorizacion.tpl
			└── bender.png

- requirements.txt: contiene las librerias a instalar con pip para el correcto funcionamiento de la aplicación.
	
		pip install -r requirements.txt

- main.py: contiene la aplicación en sí.
- header.tpl: contiene todo lo común en todas las plantillas como el título de la web y la columna lateral en cuanto a encabezado.
- footer.tpl: contiene todo lo común en todas las plantillas en cuanto a pie de página.
- index.tpl: página principal. Contiene un breve resumen de los servidores activos, inactivos y totales.
- backups.tpl: página principal de las copias de seguridad. Nos muestra las últimas 10 copias realizadas y nos da opciones de crear o restaurar.
- nuevo.tpl: contiene el formulario para poder realizar una nueva copia.
- nuevo2.tpl: recibe los datos del fomulario y ejecuta el comando.
- restaurar.tpl: nos pide el host a restaurar, para mostrar en el siguiente formulario las copias disponibles para restaurar.
- restaurar2.tpl: contiene el formulario para poder restaurar una copia.
- restaurar3.tpl: recibe los datos de los formularios para poder ejecutar el comando.
- docs.tpl: muestra los luegares principales que se han usado para instalaciones y documentación en general.
- jarvis.tpl: muestra un breve resumen del estado de los discos y la RAM y nos da la opción de ver su zabbix.
- monitorizacion.tpl: página principal de la parte de monitorización en la que se muestra un resumen de los hosts existentes, dando el estado u un resumen de cada host. Redirige todos los host al zabbix correspondiente y al resumen de jarvis.
