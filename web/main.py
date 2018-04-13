import bottle
from lxml import etree
import requests
from sys import argv
import os


@route('/')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

run(host='0.0.0.0',port=8080, debug=True)