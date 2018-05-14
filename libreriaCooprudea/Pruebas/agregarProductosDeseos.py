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


@app.route("/agregarProductoDeseos", methods=['POST'])
def agregarProductoDeseos():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    fecha = time.strftime("%Y/%m/%d")
    estado = "1"
    bandera = 0

    try:
        #El Usuario tiene una lista de deseos activa
        bandera = cursor.execute("SELECT codigo, Id_Codigo_Producto, Id_Codigo_Usuario, Id_Estado_Deseos, cantidad FROM deseos WHERE Id_Codigo_Producto ='"+codigoProducto+"' AND Id_Codigo_Usuario ='"+codigoUsuario+"'")

        if str(bandera) == '1':

            deseoEncontrado = cursor.fetchone()

            if str(deseoEncontrado[3])== '1':
                cantidad = str(deseoEncontrado[4]+int(cantidad))
                bandera = cursor.execute("UPDATE deseos SET Cantidad = '"+cantidad+"' WHERE codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()

                if str(bandera) == '1':

                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})
            else:
                bandera = cursor.execute("UPDATE deseos SET Cantidad = '"+cantidad+"', Id_Estado_Deseos = '"+estado+"' WHERE codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()

                if str(bandera) == '1':

                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de Estado en la lista"})
        else:

            bandera = cursor.execute('''INSERT INTO deseos (Id_Codigo_Producto, Id_Codigo_Usuario, Fecha_Creado, Id_Estado_Deseos, Cantidad) VALUES (%s,%s,%s,%s,%s)''',(codigoProducto, codigoUsuario,fecha, estado, cantidad))
            conn.commit()

            if str(bandera) == '1':

                deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
            else:
                return jsonify({"Resultado":str (bandera), "Mensaje": "No se agrego el producto no existente en la lista de deseos"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


if __name__ == "__main__":
    app.run()
