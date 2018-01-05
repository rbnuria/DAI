# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask import render_template
from flask import request
import os
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p4.html')

@app.route('/database')
def showDatabase():
	result = col.find({"borough": "Manhattan"}).limit(10)
	return render_template('p4.html', rows = result)


@app.route('/animaciones')
def animaciones():
    return render_template('p4.html', animaciones = True)

@app.route('/pagination')
def pagination():
	result = col.find({"borough": "Manhattan"})

	return render_template('p4.html', data = result) 


@app.route('/getlist')
def responde():
	num = int(request.args.get('pagina',''))

	result = col.find({"borough": "Manhattan"}).skip(num*10).limit(10)

	lista = []
	for var in result:
		lista.append({"name" : var["name"], "address" : var["address"]["street"], "cuisine" : var["cuisine"]})

	return jsonify(lista)


if __name__ == '__main__':
	client = MongoClient('localhost', 27017)
	db = client['test']
	col = db['restaurants']
	app.run(host='0.0.0.0', debug=True)


