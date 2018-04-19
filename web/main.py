from bottle import *
from lxml import etree
#import sesion
import requests
from sys import argv
import os

"""
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    #'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)
"""

@route('/')
def inicio():
	return template('index.tpl')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='172.16.103.45',port=8080)

