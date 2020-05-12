from flask import Flask
from flask import request
import mysql.connector
import jsonify
import sys

id_client = 0
products_client = {}

app = Flask(__name__)
cursor = None
db = None

'''
Initializes database tables (in this case "album" table)
'''
def init_db():
    global db, cursor
    result = cursor.execute("""CREATE TABLE IF NOT EXISTS albums (
                    id VARCHAR(255) NOT NULL, 
                    name VARCHAR(255) NOT NULL,
                    artist VARCHAR(255) NOT NULL, 
                    price INT, 
                    count INT DEFAULT 0) """)
    db.commit()


'''
Establishes server-database connection
'''
def connect_db():
    global db, cursor
    db = mysql.connector.connect(host='database',
                                database='mysql',
                                user='root',
                                password='password')
    if db.is_connected():
        print("Connection to database succeded")
        cursor = db.cursor()
        cursor.execute("Use mysql")
    else:
        print("Connection to database failed")

'''
Shows all albums from shop
'''
@app.route("/show_albums", methods=["GET"])
def show_albums():
    global cursor, db
    cursor.execute("SELECT * from albums")
    rows = cursor.fetchall()
    return str(rows)


'''
Adds an album to client's shopping cart
'''
@app.route("/add_album_cart", methods=["GET"])
def add_album_cart():
    global products_client, cursor, db
    product_id = request.args.get('item_id')
    client_id = request.args.get('client_id')
    cursor.execute("SELECT * from albums WHERE id = %s", (product_id,))
    row = cursor.fetchone()
    if row == None:
        return "The item doesn't exist in our shop"
    if client_id not in products_client.keys():
        products_client[client_id] = {}
    products_client[client_id][product_id] = {'name' : row[1], 'artist': row[2], 'price' : row[3], 'count' : 1}
    cursor.execute("UPDATE albums SET count=count-1 WHERE id = %s", (product_id,))
    db.commit()

    return "Item added in buying cart"


'''
Removes an album from client's shopping cart
'''
@app.route("/remove_album_cart", methods=["GET"])
def remove_album_cart():
    global products_client, cursor, db
    id_product = request.args.get('item_id')
    client = request.args.get('client_id')

    # checking if item exists in shop
    cursor.execute("SELECT * from albums WHERE id = %s", (id_product,))
    row = cursor.fetchone()
    if row == None:
        return "The item doesn't exist in our shop"
    elif row[4] == '0' or row[4] == 0:
         return str("Deleted item: " + id_product)

    products_client[client].pop(id_product)
    query = "UPDATE albums SET count=count+1 WHERE id = %s"
    cursor.execute(query, (id_product,))
    db.commit()
    return "Item deleted from buying cart"


'''
Shows the items from buying cart
'''
@app.route("/show_buying_cart", methods=["GET"])
def show_buying_cart():
    global products_client
    client = request.args.get('client_id')
    if client in products_client:
        return products_client[client]
    else:
        return {}


'''
Finishing the transaction
'''
@app.route("/finalise_buying", methods=["GET"])
def finalise_buying():
    client = request.args.get('client_id')
    products_client[client] = {}
    return "Transaction finished."


'''
Adding an album in shop
'''
@app.route("/add_album", methods=["GET"])
def add_album():
    global cursor, db

    album_count = '1'
    id_product = request.args.get('id')
    name = request.args.get('name')
    price = request.args.get('price')
    artist = request.args.get('artist')

    cursor.execute("SELECT * from albums WHERE id = %s", (id_product,))
    rows = cursor.fetchone()

    if rows == None:
        cursor.execute("INSERT INTO albums (id, name, artist, price, count) VALUES (%s, %s, %s, %s, %s)", 
            (id_product, name, artist, price, album_count))
    else:
        cursor.execute("UPDATE albums SET count=count+1 WHERE id = %s", (id_product,))

    db.commit()

    return "Item added: " + name + " - " + artist

'''
Removing an album from shop
'''
@app.route("/remove_album", methods=["GET"])
def remove_album():
    global cursor, db
    id_product = request.args.get('id')

    # checking if item exists in shop
    cursor.execute("SELECT * from albums WHERE id = %s", (id_product,))
    row = cursor.fetchone()
    if row == None:
        return "The item doesn't exist in our shop"
    elif row[4] == '0' or row[4] == 0:
         return str("Deleted item: " + id_product)

    cursor.execute("UPDATE albums SET count=count-1 WHERE id = %s", (id_product,))
    db.commit()
    return str("Deleted item: " + id_product)

'''
Shows items from the database of the shop
'''
@app.route("/show_database_items", methods=["GET"])
def show_database_items():
    global cursor, db
    cursor.execute("SELECT * from albums")
    rows = cursor.fetchall()
    return str(rows)

'''
Connection to the server and assigning an id for the client
'''
@app.route("/connect", methods=["GET"])
def connect():
    global id_client
    id_client += 1
    return str(id_client)


def main():
    global db, cursor
    connect_db()
    init_db()
    app.run('0.0.0.0', debug=True)


if __name__ == "__main__":
    main()