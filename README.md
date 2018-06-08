# couchweb
***
Aplicación web para la gestión de las copias de seguridad y la monitorización del entorno creado para CouchBase.

Está escrita en python usando el framework ligero Bottle y usando un entorno virtual

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

- main.py: 
- header.tpl: contiene todo lo común en todas las plantillas como el título de la web y la columna lateral.
- footer.tpl:
- index.tpl:
- backups.tpl:
- nuevo.tpl:
- nuevo2.tpl:
- restaurar.tpl: 
- restaurar2.tpl:
- restaurar3.tpl:
- docs.tpl:
- jarvis.tpl:
- monitorizacion.tpl:
