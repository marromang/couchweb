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

# conexion a couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://172.22.200.101')
authenticator = PasswordAuthenticator('Administrator', 'marromang')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('beer-sample')

# cnx = connection.MySQLConnection(user='root', password='root',host='localhost',database='backups')
cnx = mysql.connector.connect(user='root',password='root', database='backups')
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
	# se comprueba si los hosts están activos
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
	return template('static/pages/monit-jarvis.tpl', usuario=usuario, diskPerc = diskPerc, ramPerc = ramPerc, diskTotal=diskTotal, diskAvail=diskAvail, ramAvail=ramAvail, ramTotal=ramTotal)	
	
@route('/metrica')
def metrica():
	# se comprueba si los hosts están activos
	stark = checkAlive('172.22.200.101')
	pepper = checkAlive('172.22.200.103')
	jarvis = checkAlive('172.22.200.105')

	# template
	return template('static/pages/monitorizacion.tpl', usuario=usuario, stark=stark, pepper=pepper, jarvis=jarvis)


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

	# comprobación de que la etiqueta no existe
	query = ("SELECT label FROM backups")
	lista = []
	for c in cursor:
		if c == label:
			redirect('/error')

	# inserción de los datos de la nueva copia
	add_backup = ("INSERT INTO backups VALUES (%s, %s, %s, %s, %s, %s)")
	data_backup = (label, host, nodos, bucket, comentario,time.strftime("%d/%m/%Y %H:%M:%S") )
	cursor.execute(add_backup, data_backup)
	back_no = cursor.lastrowid
	cnx.commit()

	# segun el host que se haya indicado, la copia se hará en un servidor o en otro
	if host == 'stark':
		ip = '172.22.200.101'
	else:
		ip = '172.22.200.103'

	# si es sobre un nodo específico...
	if nodos != 'todos':
		if bucket:
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang --single-node -b "+bucket
		# si no se indica ningun nodo...
		else: 
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang --single-node"
	# si se ha indicado un bucket concreto...
	elif bucket:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubunut/backups -u Administrator -p marromang -b "+bucket
	# si es sobre todos los buckets...
	else:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang"
	
	# ejecucion del comando en remoto. La version normal de couchbase no permite ejecucion en remoto con librerias, por lo que el metodo que 
	# se me ocurrio fue a traves de ssh, aunque no sea el mas adecuado.
	os.system("ssh ubuntu@"+ip+" "+cad)
	#os.system("ssh ubuntu@172.22.200.101 "+cad)
	
	# para depuracion
	print lista

	# redireccion al indice de copias de seguridad, donde aparecerá la primera de la lista
	redirect("/backups")

@route('/restaurar')
def restaurar():
	# obtención del host para luego, segun el elegido, mostrar unos directorios a restaurar u otros, que varian segun las copias realizadas.
	host = request.forms.get('host')
	
	# template
	return template("static/pages/backups/restaurar.tpl", usuario=usuario, host=host)

@route('/restaurar2', method='post')
def restaurar2():
	host = request.forms.get('host')

	# si el host es stark, muestra los directorios desde los que se pueden hacer restauraciones
	if host = stark:
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

	# comprobación de que la etiqueta no existe
	query = ("SELECT label FROM restore")
	lista = []
	for c in cursor:
		if c == label:
			redirect('/error')

	# inserción de los datos de la nueva restauracion
	add_restore = ("INSERT INTO restore VALUES (%s, %s, %s, %s, %s, %s)")
    data_restore = (label, host, directorio, origen, destino, comentario)
    cursor.execute(add_restore, data_restore)
    back_no = cursor.lastrowid
	cnx.commit()
    
	# segun el host que se haya indicado, la restauracion se hará en un servidor o en otro
    if host == 'stark':
        ip = '172.22.200.101'
    else:
     	ip = '172.22.200.103'

    # si no se ha indicado un destino, éste será el mismo que el origen
    if not destino:
        cad = "sh /opt/couchbase/bin/cbrestore /home/ubuntu/backups http://"+ip+":8091 -b "+origen
    # si se ha indicado un directorio, ese será el que se utilice
    elif directorio:
        cad="sh /opt/couchbase/bin/cbrestore /hime/ubuntu/backups/"+directorio+" http://Administrator:marromang@"+ip+":8091 --bucket-source="+origen
        # si se ha indicado un destino, se añadirá al comando anterior 
        if destino:
           cad = cad+" --bucket-destination="+destino
	
	# para depuracion
	print cad
	
	# ejecucion del comando 
	os.system("ssh ubuntu@"+ip+" "+cad)
	
	# redirección a la página principal de las copias de seguridad
	redirect('/backups')

@route('/stark')
def stark():
	# redireccion a zabbix
	redirect('http://jarvis.maria.org/zabbix')

@route('/pepper')
def pepper():
	# redireccion a zabbix
	redirect('http://jarvis.maria.org/zabbix')

@route('/docs')
def docs():
	# template
    return template('static/pages/docs.tpl', usuario=usuario)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=8081)

