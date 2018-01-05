# -*- coding: utf-8 -*-

from flask import Flask
from flask import send_file
from flask import render_template
from PIL import Image
from flask import request
import mandelbrot
from mandelbrot import renderizaMandelbrotBonito
from random import randint, uniform,random
import os.path as path
import os,time,sys

app = Flask(__name__)




@app.route('/')
def index():
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="static/style/style_form.css" />
    </head>
    <body>
        <h1> PÁGINA PRINCIPAL </h1>
        <center>
            <img src="./static/logo.png"/>
        </center>
    </body>
    '''


@app.route('/user/zerjillo')
def hellozerjillo():
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="/static/style/style_form.css" media="all"/>
    </head>
    <body>
        <h1> HOLA ZERJILLO </h1>
        <center>
            <img src="/static/logo.png"/>
        </center>
    </body>
    '''

@app.route('/user/pepe')
def hellopepe():
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="/static/style/style_form.css" />
    </head>
    <body>
        <h1> HOLA PEPE </h1>
        <center>
            <img src="/static/logo.png"/>
        </center>
    </body>
    '''



@app.route('/user/<username>') #Captura una parte de la URL
def mostrarPerfilUsuario(username): #La pasa como parámetro a la f
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="/static/style/style_form.css" />
    </head>
    <body>
        <h1> HOLA %s </h1>
        <center>
            <img src="/static/logo.png"/>
        </center>
    </body>
    '''%username


def cleanCache():
    #Fijamos el path que queremos limpiar
    path = "/Users/nuria/DAI/P2/imagenes"

    #Obtenemos tiempo actual
    now = time.time()

    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - 24*3600:
            if os.path.isfile(f):
                os.remove(f)



@app.route('/mandelbrot', methods=['GET'])
def formulario():
    #Comprobamos si viene el parametro por GET
    return render_template('formulario_get.html')


@app.route('/mandelbrot', methods=['POST'])
def pintar():
    cleanCache()
	#Obtenemos los valores metidos
    x1 = float(request.form['x1'])
    x2 = float(request.form['x2'])
    y1 = float(request.form['y1'])
    y2 = float(request.form['y2'])
    ancho = int(request.form['ancho'])
    iteraciones = int(request.form['iteraciones'])
    color1 = request.form['color1']
    color1 = color1[1:len(color1)]

    rr1 = (int(color1[0:2],16))
    gg1 = (int(color1[2:4],16))
    bb1 = (int(color1[4:6],16))

    color2 = request.form['color2']
    color2 = color2[1:len(color2)]

    rr2 = (int(color2[0:2],16))
    gg2 = (int(color2[2:4],16))
    bb2 = (int(color2[4:6],16))

    color3 = request.form['color3']
    color3 = color3[1:len(color3)]

    rr3 = (int(color3[0:2],16))
    gg3 = (int(color3[2:4],16))
    bb3 = (int(color3[4:6],16))

    #Nombre del nuevo fractal
    name = "mandelbrot" + str(x1) + str(x2) + str(y1) + str(y2) + str(ancho) + str(iteraciones) + color1 + color2+ color3+ ".png"

    if path.exists("./imagenes/"+name):
        #mandamos la imagen pues ya existe
        return send_file("./imagenes/"+name, mimetype = "image/png")
    else:
        #Creamos la imagen
        renderizaMandelbrotBonito(x1,y1,x2,y2,ancho,iteraciones,name,[(rr1,gg1,bb1),(rr2,gg2,bb2),(rr3,gg3,bb3)],3)
        return send_file("./imagenes/"+name, mimetype = "image/png")


@app.route('/dinamica')
def dinamica():
    #Tenemos tres opciones de dibujo (círculo, rectángulo, elipse, polígono)
    #Elegimos un número aleatorio (0,1,2,3) para ver cual de estas opciones sale:
    option = randint(0,2)

    return_str = '''
    <html>
    <head>
            <link rel="stylesheet" href="static/style/style_form.css" />

    </head>
    <body>
    <h1>IMAGEN DINÁMICA </h1>
    <svg width="10000" height="10000">'''


    #Todas ellos los vamos a dibujar de diferentes colores: (tanto relleno como borde)
    colours = ['salmon', 'pink', 'blue', 'orangered', 'tomato','cadetblue','darkcyan','brown', 'lightgreen', 'blueviolet']

    for i in range(1,15):
        option = randint(0,2)

        if option == 0: #círculo
            #Tenemos que generar aleatoriamente: cx,cy, ratio, stroke, storke-width, fill
            cx = randint(50,1200)
            cy = randint(100,800)
            ratio = randint(30,200)
            aux_stroke = randint(0,9)
            stroke = colours[aux_stroke]
            stroke_width = uniform(1,10)
            aux_fill = randint(0,9)
            fill = colours[aux_fill]
            opacity = uniform(0,1)

            return_str = return_str + "<circle cx=%s cy=%s r=%s stroke=%s stroke-width=%s fill=%s opacity=%s />"%(cx,cy,ratio,stroke,stroke_width,fill, opacity)

        elif option == 1:
            x = randint(50,1200)
            y = randint(100,800)
            width = randint(30,200)
            height = randint(30,200)
            aux_stroke = randint(0,9)
            stroke = colours[aux_stroke]
            stroke_width = uniform(1,10)
            aux_fill = randint(0,9)
            fill = colours[aux_fill]
            opacity = uniform(0,1)

            return_str = return_str + "<rect x=%s y=%s width=%s height=%s stroke=%s stroke-width=%s fill=%s opacity=%s />"%(x,y,width,height,stroke, stroke_width, fill, opacity)

        elif option == 2:
            cx = randint(50,1200)
            cy = randint(100,800)
            rx = randint(30,200)
            ry = randint(30,200)
            aux_stroke = randint(0,9)
            stroke = colours[aux_stroke]
            stroke_width = uniform(1,10)
            aux_fill = randint(0,9)
            fill = colours[aux_fill]
            opacity = uniform(0,1)

            return_str = return_str + "<ellipse cx=%s cy=%s rx=%s ry=%s stroke=%s stroke-width=%s fill=%s opacity=%s />"%(cx,cy,rx,ry,stroke,stroke_width,fill, opacity)

    return return_str + "</svg></body></html>"
   
@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
