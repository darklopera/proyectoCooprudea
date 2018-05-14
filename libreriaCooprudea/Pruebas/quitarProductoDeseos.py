from flask import Flask, request
from flaskext.mysql import MySQL
from flask import jsonify
import time

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'libreriamovil'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

def obtenerProductoDeseo(Producto ,Usuario , Estado):
    cursor.execute("SELECT codigo, Id_Codigo_Producto, Id_Codigo_Usuario, Id_Estado_Deseos, cantidad FROM deseos WHERE Id_Codigo_Producto ='"+Producto+"' AND Id_Codigo_Usuario ='"+Usuario+"' AND Id_Estado_Deseos='"+Estado+"'")
    return (cursor.fetchone())


@app.route("/quitarProductoDeseos", methods=['POST'])
def quitarProductoDeseos():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    estado = "2"
    bandera = 0

    try:
        #El Usuario tiene una lista de deseos activa
        bandera = cursor.execute("SELECT codigo, Id_Codigo_Producto, Id_Codigo_Usuario, Id_Estado_Deseos, cantidad FROM deseos WHERE Id_Codigo_Producto ='"+codigoProducto+"' AND Id_Codigo_Usuario ='"+codigoUsuario+"'")

        if str(bandera) == '1':

            deseoEncontrado = cursor.fetchone()
            print "Se hizo el select"

            if str(deseoEncontrado[3])== '1':
                print "Esta activo el producto en la lista"
                print "UPDATE deseos SET Id_Estado_Deseos = '"+estado+"' WHERE Codigo = '"+str(deseoEncontrado[0])+"'"
                bandera = cursor.execute("UPDATE deseos SET Id_Estado_Deseos = '"+estado+"' WHERE Codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()
                print "se hizo la actualizacion"

                if str(bandera) == '1':

                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})
            else:
                print "El deseo no esta activo"
                return "El deseo no esta activo"

        else:
            print "El deseo no existe"
            return "El deseo no existe"

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


if __name__ == "__main__":
    app.run()
