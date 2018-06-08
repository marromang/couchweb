# couchweb
***
Aplicación web para la gestión de las copias de seguridad y la monitorización del entorno creado para CouchBase.

Está escrita en python usando el framework liger Bottle.

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
			│	├── error.tpl
			│	└── monitorización
			│		├── jarvis.tpl
			│		├── monit-jarvis.tpl
			│		└── monitorizacion.tpl
			└── bender.png


