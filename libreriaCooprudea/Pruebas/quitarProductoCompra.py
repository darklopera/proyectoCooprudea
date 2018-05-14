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

def obtenerProductoCompra(Compra ,Producto , Estado):
    #cursor.execute("SELECT codigo, Id_Codigo_Producto, Id_Codigo_Usuario, Id_Estado_Deseos, cantidad FROM deseos WHERE Id_Codigo_Producto ='"+Producto+"' AND Id_Codigo_Usuario ='"+Usuario+"' AND Id_Estado_Deseos='"+Estado+"'")
    cursor.execute("SELECT * FROM productoxcompra WHERE Id_Codigo_Compra = '"+Compra+"' AND Id_Codigo_Producto ='"+Producto+"' AND Estado = '"+Estado+"'")
    #productoXcompraActualizado = cursor.fetchone()
    return (cursor.fetchone())


@app.route("/quitarProductoCompra", methods=['POST'])
def quitarProductoCompra():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    #fecha = time.strftime("%Y/%m/%d")
    estado = "0"
    bandera = 0

    try:

        bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='1'")
        print "Primer Select"
        print "SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='"+estado+"'"
        print bandera
        #El Usuario tiene una compra activa
        if str(bandera) == '1':

            compraEncontrada = cursor.fetchone()
            print "Existe una compra"
            bandera = cursor.execute("SELECT * FROM productoxcompra WHERE Id_Codigo_Compra = '"+str(compraEncontrada[0])+"' AND Id_Codigo_Producto = '"+codigoProducto+"'")
            if str(bandera)== '1':

                productoEncontrado= cursor.fetchone()

                if str(productoEncontrado[3])== '1':

                    print "Existe producto activo"
                    cantidad = str(productoEncontrado[2]+int(cantidad))
                    bandera = cursor.execute("UPDATE productoxcompra SET Estado = '"+estado+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"' AND Estado = '"+str(productoEncontrado[3])+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Estado": productoEncontrado[3]})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})

                else:
                    print "Existe producto inactivo"
                    return "Existe producto inactivo"

            else:
                print "El producto no existe"
                return "El producto no existe"
        else:

            print "No existe Compra relacionada al usuario"
            return "No existe Compra relacionada al usuario"
    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


if __name__ == "__main__":
    app.run()
