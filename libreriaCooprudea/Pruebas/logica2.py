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

@app.route("/agregarProductoCompra", methods=['POST'])
def agregarProductoCompra():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = int(request.form['cantidad'])
    bandera = 0

    try:
        #El Usuario tiene una compra activa
        bandera = cursor.execute(
        "SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='1'")

        if str(bandera) == '1':

            codigoCompra = str(cursor.fetchone()[0])

            #El producto ya esta en la compra
            bandera = cursor.execute("SELECT Id_Codigo_Producto FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"'")

            if str(bandera) == '1':

                #El producto esta activo en la compra
                bandera = cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '1'")

                if str(bandera) == '1':
                    productoXcompraEncontrado = cursor.fetchone()
                    productoEncontrado = str(productoXcompraEncontrado[0])
                    cantidadEncontrada = str(productoXcompraEncontrado[1])

                    nuevaCantidad = str(int(cantidadEncontrada) + cantidad)

                    #Actualizacion de datos
                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+nuevaCantidad+"' WHERE Id_Codigo_Producto = '"+productoEncontrado+"' AND Id_Codigo_Compra = '"+codigoCompra+"' AND Estado = '1'")
                    conn.commit()

                    if str(bandera) == '1':

                        #Informacion nueva en la bd
                        cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '1'")
                        productoXcompraActualizado = cursor.fetchone()
                        productoActualizado = str(productoXcompraActualizado[0])
                        cantidadActualizado = str(productoXcompraActualizado[1])

                        return jsonify({"Resultado":str (bandera), "Producto": productoActualizado, "Nueva Cantidad": cantidadActualizado})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion"})
                else:

                    bandera = cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '0'")
                    productoXcompraEncontrado = cursor.fetchone()
                    productoEncontrado = str(productoXcompraEncontrado[0])
                    cantidadEncontrada = str(cantidad)

                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+cantidadEncontrada+"', Estado = '1' WHERE Id_Codigo_Producto = '"+productoEncontrado+"' AND Id_Codigo_Compra = '"+codigoCompra+"' AND Estado = '0'")
                    conn.commit()

                    if str(bandera) == '1':
                        cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '1'")
                        productoXcompraActualizado = cursor.fetchone()
                        productoActualizado = str(productoXcompraActualizado[0])
                        cantidadActualizado = str(productoXcompraActualizado[1])

                        return jsonify({"Resultado":str (bandera), "Producto": productoActualizado, "Nueva Cantidad": cantidadActualizado})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se realizo la actualizacion de Estado"})
            else:

                # El usuario tiene una compra activa pero el producto no se encontro
                estado = "1"
                bandera = cursor.execute('''INSERT INTO productoxcompra (Id_Codigo_Compra, Id_Codigo_Producto, Cantidad, Estado) VALUES (%s,%s,%s,%s)''',(codigoCompra, codigoProducto, cantidad, estado))
                conn.commit()

                if str(bandera) == '1':
                    cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '1'")
                    productoXcompraActualizado = cursor.fetchone()
                    productoActualizado = str(productoXcompraActualizado[0])
                    cantidadActualizado = str(productoXcompraActualizado[1])
                    return jsonify({"Resultado":str (bandera), "Producto": productoActualizado, "Nueva Cantidad": cantidadActualizado})
                else:
                    return jsonify({"Resultado":str (bandera), "Mensaje": "No se agrego el producto no existente en la compra"})

        else:

            fecha = time.strftime("%Y/%m/%d")
            estadoCompra= '1'
            bandera = cursor.execute('''INSERT INTO compra (Id_Codigo_Usuario, Id_Estado_Compra, Fecha) VALUES (%s,%s,%s)''',(codigoUsuario, estadoCompra, fecha))
            conn.commit()

            if str(bandera) == '1':

                bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='1'")

                if str(bandera) == '1':

                    codigoCompra = str(cursor.fetchone()[0])
                    estado = "1"

                    bandera = cursor.execute('''INSERT INTO productoxcompra (Id_Codigo_Compra, Id_Codigo_Producto, Cantidad, Estado) VALUES (%s,%s,%s,%s)''',(codigoCompra, codigoProducto, cantidad, estado))
                    conn.commit()

                    if str(bandera) == '1':
                        cursor.execute("SELECT Id_Codigo_Producto, Cantidad FROM productoxcompra WHERE Id_Codigo_Compra = '"+codigoCompra+"' AND Id_Codigo_Producto ='"+codigoProducto+"' AND Estado = '1'")
                        productoXcompraActualizado = cursor.fetchone()
                        productoActualizado = str(productoXcompraActualizado[0])
                        cantidadActualizado = str(productoXcompraActualizado[1])
                        return jsonify({"Resultado":str (bandera), "Producto": productoActualizado, "Nueva Cantidad": cantidadActualizado})
                    else:
                        return jsonify({"Resultado":str (bandera), "Mensaje": "No se agrego el producto no existente en la nueva compra"})

            else:
                return jsonify({"Resultado":str (bandera), "Mensaje":"No se la nueva lista de compras"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})

if __name__ == "__main__":
    app.run()
