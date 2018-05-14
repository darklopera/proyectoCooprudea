from flask import Flask, request
from flaskext.mysql import MySQL
from flask import jsonify
import time

# from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
# CORS(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'libreriamovil'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

@app.route("/", methods=['GET'])
def saludo():
    return jsonify("Bienvenido Cooprudea")

@app.route("/obtenerTodosProductos", methods=['GET'])
def obtenerTodosProductos():
    cursor.execute("SELECT Codigo, Titulo, Autor from productos where Id_Estado_Producto='1'")
    data = jsonify(cursor.fetchall())

    return (data)

@app.route("/obtenerProductosISBN", methods=['GET'])
def obtenerProductosISBN():
    isbn = request.args.get('isbn')
    cursor.execute(
        "SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, productos.Id_Categoria, productos.Id_Editorial, productos.Precio, productos.Cantidad, productos.Imagen_Path, editorial.Nombre AS Editorial, `categorias`.`Nombre` AS Nombre_Categoria FROM editorial INNER JOIN productos ON editorial.Codigo = productos.Id_Editorial INNER JOIN categorias ON categorias.Codigo = productos.Id_Categoria WHERE productos.Referencia = '"+isbn+"' AND productos.Id_Estado_Producto='1' AND categorias.`Estado`='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerProductosTitulo", methods=['GET'])
def obtenerProductoTitulo():
    titulo = request.args.get('titulo')

    cursor.execute("SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, productos.Id_Categoria, productos.Id_Editorial, productos.Precio, productos.Cantidad, productos.Imagen_Path, editorial.Nombre AS Editorial, `categorias`.`Nombre` AS Nombre_Categoria FROM editorial INNER JOIN productos ON editorial.Codigo = productos.Id_Editorial INNER JOIN categorias ON categorias.Codigo = productos.Id_Categoria WHERE productos.`Titulo` LIKE '%" + titulo + "%' AND productos.Id_Estado_Producto='1' AND categorias.`Estado`='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerProductosAutor", methods=['GET'])
def obtenerProductosAutor():
    autor = request.args.get('autor')

    cursor.execute(
        "SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, productos.Id_Categoria, productos.Id_Editorial, productos.Precio, productos.Cantidad, productos.Imagen_Path, editorial.Nombre AS Editorial, `categorias`.`Nombre` AS Nombre_Categoria FROM editorial INNER JOIN productos ON editorial.Codigo = productos.Id_Editorial INNER JOIN categorias ON categorias.Codigo = productos.Id_Categoria WHERE productos.`Autor` LIKE '%"+autor+"%' AND productos.Id_Estado_Producto='1' AND categorias.`Estado`='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerProductosCategoria", methods=['GET'])
def obtenerProductosCategoria():
    categoria = request.args.get('categoria')

    cursor.execute(
        "SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, productos.Id_Categoria, productos.Id_Editorial, productos.Precio, productos.Cantidad, productos.Imagen_Path, editorial.Nombre AS Editorial, `categorias`.`Nombre` AS Nombre_Categoria FROM editorial INNER JOIN productos ON editorial.Codigo = productos.Id_Editorial INNER JOIN categorias ON categorias.Codigo = productos.Id_Categoria WHERE categorias.`Codigo` = '"+categoria+"' AND productos.Id_Estado_Producto='1' AND categorias.`Estado`='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerProductosEditorial", methods=['GET'])
def obtenerProductosEditorial():
    editorial = request.args.get('editorial')

    cursor.execute(
        "SELECT Codigo, Titulo, Autor from productos where Id_Editorial like '" + editorial + "' and Id_Estado_Producto='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerTodasCategorias", methods=['GET'])
def obtenerTodasCategorias():
    cursor.execute("SELECT Codigo, Nombre, Imagen_Path from categorias where Estado='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerDeseosUsuario", methods=['GET'])
def obtenerDeseosUsuario():
    codigoUsuario = request.args.get('codigoUsuario')

    cursor.execute(
        "SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, productos.Id_Categoria, productos.Id_Editorial, productos.Precio, productos.Imagen_Path, editorial.Nombre AS Editorial, `categorias`.`Nombre` AS Nombre_Categoria, deseos.`Cantidad` AS Cantidad_Deseos FROM editorial INNER JOIN productos ON editorial.Codigo = productos.Id_Editorial INNER JOIN categorias ON categorias.Codigo = productos.Id_Categoria INNER JOIN deseos ON deseos.`Id_Codigo_Producto`=`productos`.`Codigo` INNER JOIN usuarios ON `usuarios`.`Codigo`=`deseos`.`Id_Codigo_Usuario` WHERE  `usuarios`.`Codigo`='"+codigoUsuario+"'AND deseos.`Id_Estado_Deseos`='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerProducto", methods=['GET'])
def obtenerProducto():
    codigoProducto = request.args.get('codigoProducto')

    cursor.execute(
        "SELECT productos.Codigo, productos.Referencia, productos.Titulo, productos.Autor, categorias.Nombre, editorial.Nombre, productos.Precio, productos.Cantidad, productos.Imagen_Path from productos INNER JOIN categorias on productos.Id_Categoria = categorias.Codigo INNER JOIN editorial on productos.Id_Editorial = editorial.Codigo where productos.Codigo like '" + codigoProducto + "' and productos.Id_Estado_Producto='1'")
    data = jsonify(cursor.fetchall())

    return (data)


@app.route("/obtenerCompraUsuario", methods=['GET'])
def obtenerCompraUsuario():
    codigoUsuario = request.args.get('codigoUsuario')

    cursor.execute(
        "SELECT productoxcompra.Id_Codigo_Compra, productos.Titulo, productoxcompra.Cantidad, productos.Precio FROM productoxcompra INNER JOIN productos ON productoxcompra.Id_Codigo_Producto = productos.Codigo INNER JOIN compra ON productoxcompra.Id_Codigo_Compra = compra.Codigo WHERE compra.Id_Estado_Compra='1' AND productos.Id_Estado_Producto='1' AND productoxcompra.Estado='1' AND compra.Id_Codigo_Usuario = '" + codigoUsuario + "'")
    data = jsonify(cursor.fetchall())

    return data


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
    deseoEncontrado = ''

    try:
        #El Usuario tiene una lista de deseos activa
        bandera = cursor.execute("SELECT codigo, Id_Codigo_Producto, Id_Codigo_Usuario, Id_Estado_Deseos, cantidad FROM deseos WHERE Id_Codigo_Producto ='"+codigoProducto+"' AND Id_Codigo_Usuario ='"+codigoUsuario+"'")

        if str(bandera) == '1':
            deseoEncontrado = cursor.fetchone()
            if str(deseoEncontrado[3])== '1':
                bandera = cursor.execute("UPDATE deseos SET Cantidad = '"+cantidad+"' WHERE codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()

                if str(bandera) == '1':
                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":"1012", "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})
            else:
                bandera = cursor.execute("UPDATE deseos SET Cantidad = '"+cantidad+"', Id_Estado_Deseos = '"+estado+"' WHERE codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()

                if str(bandera) == '1':

                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":"1013", "Mensaje": "No se realizo la actualizacion de Estado en la lista"})
        else:

            bandera = cursor.execute('''INSERT INTO deseos (Id_Codigo_Producto, Id_Codigo_Usuario, Fecha_Creado, Id_Estado_Deseos, Cantidad) VALUES (%s,%s,%s,%s,%s)''',(codigoProducto, codigoUsuario,fecha, estado, cantidad))
            conn.commit()

            if str(bandera) == '1':

                deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
            else:
                return jsonify({"Resultado":"1014", "Mensaje": "No se agrego el producto no existente en la lista de deseos"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


def obtenerProductoCompra(Compra ,Producto , Estado):
    cursor.execute("SELECT * FROM productoxcompra WHERE Id_Codigo_Compra = '"+Compra+"' AND Id_Codigo_Producto ='"+Producto+"' AND Estado = '"+Estado+"'")
    return (cursor.fetchone())


@app.route("/agregarProductoCompra", methods=['POST'])
def agregarProductoCompra():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    estado = "1"
    bandera = 0

    try:

        bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='"+estado+"'")
        #El Usuario tiene una compra activa
        if str(bandera) == '1':

            compraEncontrada = cursor.fetchone()
            bandera = cursor.execute("SELECT * FROM productoxcompra WHERE Id_Codigo_Compra = '"+str(compraEncontrada[0])+"' AND Id_Codigo_Producto = '"+codigoProducto+"'")
            if str(bandera)== '1':

                productoEncontrado= cursor.fetchone()

                if str(productoEncontrado[3])== '1':

                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+cantidad+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"' AND Estado = '"+estado+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                    else:
                        return jsonify({"Resultado":"1007", "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})

                else:

                    bandera = cursor.execute("UPDATE productoxcompra SET Cantidad = '"+cantidad+"', Estado = '"+estado+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                    else:
                        return jsonify({"Resultado":"1008", "Mensaje": "No se realizo la actualizacion del estado en la Lista de deseos"})

            else:

                bandera = cursor.execute('''INSERT INTO productoxcompra (Id_Codigo_Compra, Id_Codigo_Producto, Cantidad, Estado) VALUES (%s,%s,%s,%s)''',(str(compraEncontrada[0]), codigoProducto, cantidad, estado))
                conn.commit()

                if str(bandera) == '1':

                    productoEncontrado = obtenerProductoCompra(str(compraEncontrada[0]), codigoProducto, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Nueva Cantidad": productoEncontrado[2]})
                else:
                    return jsonify({"Resultado":"1009", "Mensaje": "No se realizo la actualizacion de Estado en la lista"})
        else:

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
                        return jsonify({"Resultado":"1010", "Mensaje": "No se agrego el producto y no existente en la nueva compra"})

            else:
                return jsonify({"Resultado":"1011", "Mensaje":"No se la nueva lista de compras"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


@app.route("/quitarProductoCompra", methods=['POST'])
def quitarProductoCompra():

    codigoProducto = request.form['codigoProducto']
    codigoUsuario = request.form['codigoUsuario']
    cantidad = request.form['cantidad']
    estado = "0"
    bandera = 0

    try:

        bandera = cursor.execute("SELECT Codigo FROM compra WHERE Id_Codigo_Usuario = '"+codigoUsuario+"' AND Id_Estado_Compra='1'")
        #El Usuario tiene una compra activa
        if str(bandera) == '1':

            compraEncontrada = cursor.fetchone()
            bandera = cursor.execute("SELECT * FROM productoxcompra WHERE Id_Codigo_Compra = '"+str(compraEncontrada[0])+"' AND Id_Codigo_Producto = '"+codigoProducto+"'")
            if str(bandera)== '1':

                productoEncontrado= cursor.fetchone()

                if str(productoEncontrado[3])== '1':

                    cantidad = str(productoEncontrado[2]+int(cantidad))
                    bandera = cursor.execute("UPDATE productoxcompra SET Estado = '"+estado+"' WHERE Id_Codigo_Compra = '"+str(productoEncontrado[0])+"' AND Id_Codigo_Producto = '"+str(productoEncontrado[1])+"' AND Estado = '"+str(productoEncontrado[3])+"'")
                    conn.commit()

                    if str(bandera) == '1':

                        productoEncontrado = obtenerProductoCompra(str(productoEncontrado[0]), str(productoEncontrado[1]), estado)
                        return jsonify({"Resultado":str (bandera), "Producto": productoEncontrado[1], "Estado": productoEncontrado[3]})
                    else:
                        return jsonify({"Resultado":"1000", "Mensaje": "No se realizo la actualizacion de la cantidad en la Compra"})

                else:
                    return jsonify({"Resultado":"1001", "Mensaje":"El producto ya esta inactivo en la Compra"})
            else:
                return jsonify({"Resultado":"1002", "Mensaje":"El producto no existe en la Compra"})
        else:
            return jsonify({"Resultado":"1003", "Mensaje":"No existe Compra relacionada al usuario"})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


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

            if str(deseoEncontrado[3])== '1':
                bandera = cursor.execute("UPDATE deseos SET Id_Estado_Deseos = '"+estado+"' WHERE Codigo = '"+str(deseoEncontrado[0])+"'")
                conn.commit()

                if str(bandera) == '1':

                    deseoEncontrado = obtenerProductoDeseo(codigoProducto, codigoUsuario, estado)
                    return jsonify({"Resultado":str (bandera), "Producto": deseoEncontrado[1], "Nueva Cantidad": deseoEncontrado[4]})
                else:
                    return jsonify({"Resultado":"1004", "Mensaje": "No se realizo la actualizacion de la cantidad en la Lista de deseos"})
            else:
                return jsonify({"Resultado":"1005", "Mensaje":"El deseo no esta activo en la Lista"})
        else:
            return jsonify({"Resultado":"1006", "Mensaje":"El producto no esta en la Lista "})

    except:
        return jsonify({"Resultado":"666", "Mensaje":"Problemas con la solicitud a la base de datos"})


if __name__ == "__main__":
    app.run(host='127.0.0.1',port='80')
