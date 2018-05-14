from bottle import *
from lxml import etree
#import sesion
import requests
from sys import argv
import os
import getpass

usuario = getpass.getuser()

active = 0
@route('/')
def inicio():
	active = 2
	return template('index.tpl', usuario=usuario, active=active)


@route('/metrica')
def inicio():
	return template('static/pages/monitorizacion.tpl', usuario=usuario)


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

