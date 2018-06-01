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

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
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


@route('/metrica')
def inicio():
	mem = psutil.virtual_memory()
	avail = bytes2human(mem.available)
	return template('static/pages/monitorizacion.tpl', usuario=usuario, avail=avail)
	
@route('/stark')
def inicio():
	return template('static/pages/monit-stark.tpl', usuario=usuario)

@route('/backups')
def inicio():
	return template('static/pages/backups/backups.tpl', usuario=usuario)


@route('/docs')
def inicio():
        return template('static/pages/docs.tpl', usuario=usuario)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=8080)

