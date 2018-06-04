from bottle import *
#from lxml import etree
#import sesion
import requests
from sys import argv
import os
import getpass
import psutil

#usuario activo en jarvis
usuario = getpass.getuser()

#conexion a couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('username', 'password')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('bucket-name')

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

@route('/')
def inicio():
	active = 2
	return template('index.tpl', usuario=usuario, active=active)


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
	return template('static/pages/monitorizacion.tpl', usuario=usuario)


@route('/backups')
def inicio():
	return template('static/pages/backups/backups.tpl', usuario=usuario)

@route('/nuevo')
def inicio():
	return template("static/pages/backups/nuevo.tpl", usuario=usuario)

@route('/nuevo2', method='post')
def inicio():
	host = request.forms.get('host')
	tipo = request.forms.get('tipo')
	bucket = request.forms.get('bucket')
	nodos = request.forms.get('nodo')

	if host == 'stark':
		ip = '172.22.200.101'
	else:
		ip = '172.22.200.103'

	if nodos != 'todos':
		if bucket:
			cad="cbbackup http://"+ip+":8091 /backups -u Admin -p pass --single-node -b "+bucket
		else: 
			cad="cbbackup http://"+ip+":8091 /backups -u Admin -p pass --single-node"
	elif bucket:
		cad="cbbackup http://"+ip+":8091 /backups -u Admin -p pass -b "+bucket
	else:
		cad="cbbackup http://"+ip+":8091 /backups -u Admin -p pass"
        return template('static/pages/backups/nuevo2.tpl', usuario=usuario, cad=cad)


@route('/programar')
def inicio():
        return template('static/pages/backups/programar.tpl', usuario=usuario)

@route('/eliminar')
def inicio():
        return template('static/pages/backups/eliminar.tpl', usuario=usuario)


@route('/docs')
def inicio():
        return template('static/pages/docs.tpl', usuario=usuario)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=8081)

