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


@app.route("/agregarProductoCompra", methods=['POST'])
def agregarProductoCompra():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    #fecha = time.strftime("%Y/%m/%d")
    estado = "1"
    bandera = 0

    try:

        bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='"+estado+"'")
        print "Primer Select"
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
                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+cantidad+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"' AND Estado = '"+estado+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})

                else:
                    print "Existe producto inactivo"

                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+cantidad+"', Estado = '"+estado+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion del estado en la Lista de deseos"})

            else:
                print "El producto no existe"

                bandera = cursor.execute('''INSERT INTO productoxcompra (Id_Codigo_Compra, Id_Codigo_Producto, Cantidad, Estado) VALUES (%s,%s,%s,%s)''',(str(compraEncontrada[0]), codigoProducto, cantidad, estado))
                conn.commit()

                if str(bandera) == '1':

                    productoEncontrado = obtenerProductoCompra(str(compraEncontrada[0]), codigoProducto, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                else:
                    return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de Estado en la lista"})
        else:

            print "No existe Compra relacionada al usuario"

            fecha = time.strftime("%Y/%m/%d")
            estadoCompra= '1'

            bandera = cursor.execute('''INSERT INTO compra (Id_Codigo_Usuario, Id_Estado_Compra, Fecha) VALUES (%s,%s,%s)''',(codigoUsuario, estadoCompra, fecha))
            conn.commit()

            if str(bandera) == '1':

                bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='"+estadoCompra+"'")

                if str(bandera) == '1':

                    codigoCompra = str(cursor.fetchone()[0])

                    bandera = cursor.execute('''INSERT INTO productoxcompra (Id_Codigo_Compra, Id_Codigo_Producto, Cantidad, Estado) VALUES (%s,%s,%s,%s)''',(codigoCompra, codigoProducto, cantidad, estado))
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(codigoCompra, codigoProducto, estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se agrego el producto y no existente en la nueva compra"})

            else:
                return jsonify({"Resultado":str (bandera), "Mensaje":"No se la nueva lista de compras"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


if __name__ == "__main__":
    app.run()
