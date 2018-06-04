from bottle import *
#from lxml import etree
#import sesion
import requests
from sys import argv
import os
import getpass
import psutil

usuario = getpass.getuser()

active = 0

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
        label = request.forms.get('label')
	tipo = request.forms.get('tipo')
	comentario = request.forms.get('comentario')
        return template('static/pages/backups/nuevo2.tpl', usuario=usuario, label=label, tipo=tipo, comentario=comentario)


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

