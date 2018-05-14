#!/usr/bin/python
# coding=utf-8

# Imprimir los headers HTTP
print("Content-Type: text/html")
print("")

# Imprimir el contenido de la pagina
print("<h2>Hola mundo</h2>")
print("<p>Prueba de ejecución de script Python en modo CGI.</p>")

# Mostrar la version de MySQL
import pymysql
con = pymysql.connect(db='', user='mypywebapp', passwd='tuxteno', host='localhost')
c = con.cursor()
c.execute("select @@version")
v = c.fetchall()[0]
print("<p>La versión de MySQL es: <b>%s</b></p>" % v)
