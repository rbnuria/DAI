# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import shelve
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p3.html')

@app.route('/enlace1',methods=['GET'])
def enlace1():
	session['link'] = 1

	if "visited_links" in session:
		if len(session['visited_links']) < 3:
			session['visited_links'].append("/enlace"+str(session['link']))
		else:
			session['visited_links'].pop(0)	
			session['visited_links'].append("/enlace"+str(session['link']))
	else:
		session['visited_links']=[]
		session['visited_links'].append("/enlace"+str(session['link']))


	if "user" not in session:
		session['user'] = ""

	return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])

@app.route('/enlace2',methods=['GET'])
def enlace2():
	session['link'] = 2

	if "visited_links" in session:
		if len(session['visited_links']) < 3:
			session['visited_links'].append("/enlace"+str(session['link']))
		else:
			session['visited_links'].pop(0)	
			session['visited_links'].append("/enlace"+str(session['link']))
	else:
		session['visited_links']=[]
		session['visited_links'].append("/enlace"+str(session['link']))


	if "user" not in session:
		session['user'] = ""

	return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])

@app.route('/enlace3',methods=['GET'])
def enlace3():
	session['link'] = 3

	if "visited_links" in session:
		if len(session['visited_links']) < 3:
			session['visited_links'].append("/enlace"+str(session['link']))
		else:
			session['visited_links'].pop(0)	
			session['visited_links'].append("/enlace"+str(session['link']))
	else:
		session['visited_links']=[]
		session['visited_links'].append("/enlace"+str(session['link']))


	if "user" not in session:
		session['user'] = ""

	return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])



@app.route('/signup', methods=['POST'])
def logup():
	username = str(request.form['username'])
	name = str(request.form['name'])
	mail = str(request.form['mail'])
	address = str(request.form['address'])
	gender = str(request.form['gender'])
	password = str(request.form['password'])
	rpassword = str(request.form['password-repeat'])

	print(gender)

	#Comprobamos si las contraseñas son las mismas
	if password != rpassword:
		return render_template('logup.html', user = username, name = name, mail = mail, address = address , gender = gender, error = 1)

	db[username] = {'name': name, 'mail': mail, 'address': address, 'gender':gender, 'psw': password}

	print(gender)

	#Almacenamos el usuario en session
	session['user'] = username

	return render_template('p3.html', user = username)

@app.route('/login',methods=['POST'])
def login():
	#Comprobaciones para no mandar atributos vacíos
	if "visited_links" not in session:
		session['visited_links'] = []

	if "link" not in session:
		session['link'] = ""

	username = str(request.form['username'])
	password = str(request.form['password'])

	#Almacenamos el usuario en session
	session['user'] = username

	#Si el usuario ya está registrado
	if username in db:
		#Comprobamos que haya metido bien las contraseñas
		if password != db[username]['psw']:
			#Si la contraseña está mal mandamos mensaje error
			return render_template('p3.html', last = session['visited_links'], link = session['link'], wrongpassword = True)
		else: #Si todo está ok mandamos
			return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])
	else:
		#Si no está registrado lo registramos
		return render_template('logup.html', user = username)

@app.route('/logout',methods=['GET'])
def logout():
	session.pop('user', None)

	if "user" not in session:
		session['user'] = ""

	if "visited_links" not in session:
		session['visited_links'] = []

	if "link" not in session:
		session['link'] = ""

	return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])


@app.route('/userdata')
def userdata():
	if "user" not in session:
		username = ""
	else:
		username = session['user']

	return render_template('changedata.html', user = username, name = db[username]['name'], mail = db[username]['mail'], address = db[username]['address'], gender = db[username]['gender'],psw = db[username]['psw'])

@app.route('/changedata', methods=['POST'])
def changedata():

	#Si es la primera vez que entro (precaución por el reenvio con errores)
	if session['link'] != 4:
		session['link'] = 4

		if "visited_links" in session:
			if len(session['visited_links']) < 3:
				session['visited_links'].append("/enlace"+str(session['link']))
			else:
				session['visited_links'].pop(0)	
				session['visited_links'].append("/enlace"+str(session['link']))
		else:
			session['visited_links']=[]
			session['visited_links'].append("/enlace"+str(session['link']))
 

	username = session['user']

	name = str(request.form['name'])
	mail = str(request.form['mail'])
	address = str(request.form['address'])
	gender = str(request.form['gender'])
	lpsw = str(request.form['password'])
	newpsw = str(request.form['new-password'])

	if lpsw != db[username]['psw']:
		return render_template('changedata.html', user = username, name = db[username]['name'], mail = db[username]['mail'],address = db[username]['address'], gender = db[username]['gender'], psw = db[username]['psw'], error = True)
	else:
		#Comprobación porque a la contraseña no le asignamos valor por defecto (porque si no se ve)
		db[username] = {'name': name, 'mail': mail, 'address': address, 'gender':gender,'psw': newpsw}


	return render_template('p3.html', last = session['visited_links'], link = session['link'], user = session['user'])


if __name__ == '__main__':
	#Secret key para session
	app.secret_key = os.urandom(24)

	#Abrimos archivo 
	#flag por defecto -> escritura y lectura
	#writeback = true, para poder modificar elementos de la base de datos sin tener que introducirlos de nuevo.
	db = shelve.open('database',writeback=True)
	app.run(host='0.0.0.0', debug=True)



