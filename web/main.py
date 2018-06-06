from bottle import *
#from lxml import etree
#import sesion
import requests
from sys import argv
import os
import commands
import getpass
import psutil
import mysql.connector
import time

#usuario activo en jarvis
usuario = getpass.getuser()

#conexion a couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://172.22.200.101')
authenticator = PasswordAuthenticator('Administrator', 'marromang')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('beer-sample')

#cnx = connection.MySQLConnection(user='root', password='root',host='localhost',database='backups')
cnx = mysql.connector.connect(user='root',password='root', database='backups')
cursor = cnx.cursor()

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

def checkAlive (ip):
	res = True
	if os.system("fping -a "+ ip) != 0:
		res = False 
	return res


@route('/')
def inicio():
	stark = checkAlive('172.22.200.101')
	pepper = checkAlive('172.22.200.103')
	jarvis = checkAlive('172.22.200.105')

	activos = 0
	total = 3
	if stark:
		activos = activos + 1
	if pepper:
		activos = activos + 1
	if jarvis: 	
		activos = activos + 1
	inactivos = total - activos
	
	return template('index.tpl', usuario=usuario, activos=activos, inactivos=inactivos, total=total)


@route('/jarvis')
def inicio():
	ram = psutil.virtual_memory()
	ramTotal = human(ram.total)
	ramAvail = human(ram.available)
	ramPerc = ram.percent
	disk = psutil.disk_usage('/')
	diskTotal = human(disk.total)
	diskAvail = human(disk.used)
	diskPerc = disk.percent
	cpu = psutil.cpu_percent(interval=None)
	return template('static/pages/monit-jarvis.tpl', usuario=usuario, diskPerc = diskPerc, ramPerc = ramPerc, diskTotal=diskTotal, diskAvail=diskAvail, ramAvail=ramAvail, ramTotal=ramTotal, cpu=cpu)	
	
@route('/metrica')
def inicio():
	stark = checkAlive('172.22.200.101')
	pepper = checkAlive('172.22.200.103')
	jarvis = checkAlive('172.22.200.105')

	return template('static/pages/monitorizacion.tpl', usuario=usuario, stark=stark, pepper=pepper, jarvis=jarvis)


@route('/backups')
def inicio():
	query = ("SELECT * FROM backups order by fecha desc limit 10")
	cursor.execute(query)
	lista = []

	for c in cursor:
		lista.append(c)
	return template('static/pages/backups/backups.tpl', usuario=usuario, lista=lista)

@route('/nuevo')
def inicio():
	return template("static/pages/backups/nuevo.tpl", usuario=usuario)

@route('/nuevo2', method='post')
def inicio():
	label = request.forms.get('label')
	host = request.forms.get('host')
	bucket = request.forms.get('bucket')
	nodos = request.forms.get('nodo')
	comentario = request.forms.get('comentario')

	add_backup = ("INSERT INTO backups VALUES (%s, %s, %s, %s, %s, %s)")

	data_backup = (label, host, nodos, bucket, comentario,time.strftime("%d/%m/%Y %H:%M:%S") )
	cursor.execute(add_backup, data_backup)
	back_no = cursor.lastrowid

	cnx.commit()

#	cursor.close()
#	cnx.close()
	if host == 'stark':
		ip = '172.22.200.101'
	else:
		ip = '172.22.200.103'

	if nodos != 'todos':
		if bucket:
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang --single-node -b "+bucket
		else: 
			cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang --single-node"
	elif bucket:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubunut/backups -u Administrator -p marromang -b "+bucket
	else:
		cad="sh /opt/couchbase/bin/cbbackup http://"+ip+":8091 /home/ubuntu/backups -u Administrator -p marromang"
	
	os.system("ssh ubuntu@172.22.200.101 "+cad)
	print lista
	redirect("/backups")
      	#return template('static/pages/backups/nuevo2.tpl', usuario=usuario, cad=cad)

@route('/restaurar')
def inicio():
	host = request.forms.get('host')
	
	return template("static/pages/backups/restaurar.tpl", usuario=usuario, host=host)

@route('/restaurar2', method='post')
def inicio():
	host = request.forms.get('host')
	print host
	#if host = stark:
		#lista = commands.getstatusoutput("ssh -q ubuntu@172.22.200.101 'ls /home/backups'")
	#else: 
		#lista = commands.getstatusoutput("ssh -q ubuntu@172.22.200.103 'ls /home/backups'")
	lista = commands.getstatusoutput("ssh -q ubuntu@172.22.200.101 'ls /home/ubuntu/descargas'")
	lista2= []
	for i in xrange(len(lista)):
		if i > 0:
			lista2.append(lista[i].splitlines())
	for x in lista2:
		lis = x
        return template("static/pages/backups/restaurar2.tpl", usuario=usuario, dirs=lis, host=host)

@route('/restaurar3', method='post')
def inicio():
	label = request.forms.get('label')        
   	host = request.forms.get('host')
       	directorio = request.forms.get('dir')
        origen = request.forms.get('origen')
        destino = request.forms.get('destino')
	comentario = request.forms.get('comentario')

	add_restore = ("INSERT INTO restore VALUES (%s, %s, %s, %s, %s, %s)")

        data_restore = (label, host, directorio, origen, destino, comentario)
        cursor.execute(add_restore, data_restore)
        back_no = cursor.lastrowid

        cnx.commit()
        if host == 'stark':
                ip = '172.22.200.101'
        else:
                ip = '172.22.200.103'

        if not destino:
        	cad = "cbrestore ~/backups http://"+ip+":8091 -b "+origen
        elif dir:
                cad="cbrestore /backup/"+directorio+" http://Admin:pass@"+ip+":8091 --bucket-source="+origen
                if destino:
                	cad = cad+" --bucket-destination="+destino
	print cad
	redirect('/backups')

@route('/stark')
def inicio():
	redirect('http://172.16.103.53/zabbix')

@route('/pepper')
def inicio():
	redirect('http://172.16.103.53/zabbix')


@route('/docs')
def inicio():
        return template('static/pages/docs.tpl', usuario=usuario)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=8081)

