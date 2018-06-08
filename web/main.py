from bottle import *
import requests
from sys import argv
import os
import commands
import getpass
import psutil
import mysql.connector
import time

# usuario activo en jarvis
usuario = getpass.getuser()
backup_dir = "/home/ubuntu/backups"
user = "Administrator"
passwd = os.environ["CBPASS"]
port = "8091"
mypasswd = os.environ["MYSQLPASS"]

# conexion a couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://172.22.200.101')
authenticator = PasswordAuthenticator('Administrator', 'marromang')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('beer-sample')

cnx = mysql.connector.connect(user='root',password=mypasswd, database='backups')
cursor = cnx.cursor()

# funcion para convertir los valores obtenidos con psutil a un formato mas real
def human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

# funcion que comprueba si el host esta activo o no
def checkAlive (ip):
	res = True
	if os.system("fping -a "+ ip) != 0:
		res = False 
	return res

@route('/')
def inicio():
	# se comprueba si los hosts estan activos
	stark = checkAlive('172.22.200.101')
	pepper = checkAlive('172.22.200.103')
	jarvis = checkAlive('172.22.200.105')

	# se cuentan los activos y los inactivos
	activos = 0
	total = 3
	if stark:
		activos = activos + 1
	if pepper:
		activos = activos + 1
	if jarvis: 	
		activos = activos + 1
	inactivos = total - activos
	
	# template
	return template('index.tpl', usuario=usuario, activos=activos, inactivos=inactivos, total=total)

@route('/backups')
def backups():
	# consulta con las ultimas 10 copias de seguridad
	query = ("SELECT * FROM backups order by fecha desc limit 10")
	cursor.execute(query)
	
	# conversion del cursor que genera la consulta a lista para usarlo en el template
	lista = []
	for c in cursor:
		lista.append(c)

	# template
	return template('static/pages/backups/backups.tpl', usuario=usuario, lista=lista)

@route('/nuevo')
def nuevo():
	# el template contiene el formulario con los datos para realizar la nueva copia de seguridad
	# template
	return template("static/pages/backups/nuevo.tpl", usuario=usuario)

@route('/nuevo2', method='post')
def nuevo2():
	# coger los datos del formulario anterior para generar el comando para la nueva copia
	label = request.forms.get('label')
	host = request.forms.get('host')
	bucket = request.forms.get('bucket')
	nodos = request.forms.get('nodo')
	comentario = request.forms.get('comentario')

	# insercion de los datos de la nueva copia
	hora = time.strftime("%d/%m/%Y %H:%M:%S")
	add_backup = ("INSERT INTO backups VALUES (%s, %s, %s, %s, %s, %s)")
	data_backup = (label+"-"+hora, host, nodos, bucket, comentario,hora )
	cursor.execute(add_backup, data_backup)
	back_no = cursor.lastrowid
	cnx.commit()

	# segun el host que se haya indicado, la copia se hara en un servidor o en otro
	if host == 'stark':
		ip = '172.22.200.101'
	else:
		ip = '172.22.200.103'

	# si es sobre un nodo especifico...
	if nodos != 'todos':
		if bucket:
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":"+port+" "+backup_dir+" -u "+user+" -p "+passwd+" --single-node -b "+bucket
		# si no se indica ningun nodo...
		else: 
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":"+port+" "+backup_dir+" -u "+user+" -p "+passwd+" --single-node"
	# si se ha indicado un bucket concreto...
	elif bucket:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":"+port+" "+backup_dir+" -u "+user+" -p "+passwd+" -b "+bucket
	# si es sobre todos los buckets...
	else:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":"+port+" "+backup_dir+" -u "+user+" -p "+passwd
	
	# ejecucion del comando en remoto. La version normal de couchbase no permite ejecucion en remoto con librerias, por lo que el metodo que 
	# se me ocurrio fue a traves de ssh, aunque no sea el mas adecuado.
	os.system("ssh ubuntu@"+ip+" "+cad)
	#os.system("ssh ubuntu@172.22.200.101 "+cad)
	
	# redireccion al indice de copias de seguridad, donde aparecera la primera de la lista
	redirect("/backups")

@route('/restaurar')
def restaurar():
	# obtencion del host para luego, segun el elegido, mostrar unos directorios a restaurar u otros, que varian segun las copias realizadas.
	host = request.forms.get('host')
	
	# template
	return template("static/pages/backups/restaurar.tpl", usuario=usuario, host=host)

@route('/restaurar2', method='post')
def restaurar2():
	host = request.forms.get('host')
	print host
	# si el host es stark, muestra los directorios desde los que se pueden hacer restauraciones
	if host == 'stark':
		lista = commands.getstatusoutput("ssh -q ubuntu@172.22.200.101 'ls /home/ubuntu/backups'")
	# muestra los directorios de pepper	
	else: 
		lista = commands.getstatusoutput("ssh -q ubuntu@172.22.200.103 'ls /home/ubuntu/backups'")
	
	# lista es una lista con dos campos, el primero es el resultado logico del comando (0 o 1) y el siguiente todos los directorios separados por "\n"
	# Para obtener los directorios en una lista, he separado las lineas del segundo campo y lo he almacenado en una nueva lista, que tiene una lista de un campo 
	# que a su vez tiene una lista con los directorios.
	# El segundo bucle for es para obtener los campos de la segunda lista, que los almacena en lis
	lista2= []
	for i in xrange(len(lista)):
		if i > 0:
			lista2.append(lista[i].splitlines())
	for x in lista2:
		lis = x

	# template
    	return template("static/pages/backups/restaurar2.tpl", usuario=usuario, dirs=lis, host=host)

@route('/restaurar3', method='post')
def restaurar3():
	# coger los datos del formulario anterior para generar el comando para la nueva restauracion
	label = request.forms.get('label')        
	host = request.forms.get('host')
    	directorio = request.forms.get('dir')
    	origen = request.forms.get('origen')
    	destino = request.forms.get('destino')
	comentario = request.forms.get('comentario')
	
	# comprobacion de que la etiqueta no existe
	query = ("SELECT label FROM restore")
	lista = []
	for c in cursor:
		if c == label:
			redirect('/error')

	print host
	# insercion de los datos de la nueva restauracion
	hora = time.strftime("%d/%m/%Y %H:%M:%S")
	add_restore = ("INSERT INTO restore VALUES (%s, %s, %s, %s, %s, %s)")
    	data_restore = (label+"-"+hora, host, directorio, origen, destino, comentario)
    	cursor.execute(add_restore, data_restore)
    	back_no = cursor.lastrowid
	cnx.commit()
    
	# segun el host que se haya indicado, la restauracion se hara en un servidor o en otro
    	if host == 'pepper':
        	ip = '172.22.200.103'
    	else:
     		ip = '172.22.200.101'

    	# si no se ha indicado un destino, este sera el mismo que el origen
    	if not destino:
        	cad = "sh /opt/couchbase/bin/cbrestore "+backup_dir+" -u "+user+" -p "+passwd+" http://"+ip+":"+port+" -b "+origen
    	# si se ha indicado un directorio, ese sera el que se utilice
    	elif directorio:
        	cad="sh /opt/couchbase/bin/cbrestore "+backup_dir+" "+directorio+" http://"+user+":"+passwd+"@"+ip+":"+port+" --bucket-source="+origen
        # si se ha indicado un destino, se concatenara con el comando anterior 
        if destino:
           cad = cad+" --bucket-destination="+destino
	
	# para depuracion
	print cad
	
	# ejecucion del comando 
	os.system("ssh ubuntu@"+ip+" "+cad)
	
	# redireccion a la pagina principal de las copias de seguridad
	redirect('/backups')

@route('/metrica')
def metrica():
	# se comprueba si los hosts estan activos
	stark = checkAlive('172.22.200.101')
	pepper = checkAlive('172.22.200.103')
	jarvis = checkAlive('172.22.200.105')

	# template
	return template('static/pages/monitorizacion/monitorizacion.tpl', usuario=usuario, stark=stark, pepper=pepper, jarvis=jarvis)

@route('/stark')
def stark():
	# redireccion a zabbix
	redirect('http://jarvis.maria.org/zabbix')

@route('/pepper')
def pepper():
	# redireccion a zabbix
	redirect('http://jarvis.maria.org/zabbix')

@route('/jarvis')
def jarvis():
	# ram total, libre y porcentaje
	ram = psutil.virtual_memory()
	ramTotal = human(ram.total)
	ramAvail = human(ram.available)
	ramPerc = ram.percent

	# disco total, libre y porcentaje
	disk = psutil.disk_usage('/')
	diskTotal = human(disk.total)
	diskAvail = human(disk.used)
	diskPerc = disk.percent

	# template
	return template('static/pages/monitorizacion/jarvis.tpl', usuario=usuario, diskPerc = diskPerc, ramPerc = ramPerc, diskTotal=diskTotal, diskAvail=diskAvail, ramAvail=ramAvail, ramTotal=ramTotal)	
	
@route('/docs')
def docs():
	# template
    	return template('static/pages/docs.tpl', usuario=usuario)

@route('/error')
def error():
	return template('static/pages/error.tpl', usuario=usuario)

#@error(500)
#def custom500(error):
#    return 'my custom message'

#@route("/test")
#def index():
#    abort("Boo!")
	   
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  


run(host='0.0.0.0',port=8081, reloader=True)

