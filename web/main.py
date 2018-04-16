from bottle import *
from lxml import etree
import requests
from sys import argv
import os


@route('/')
def inicio():
	return template('index.tpl')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='172.16.103.45',port=8080, debug=True)
