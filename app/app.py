from flask import Flask, render_template, send_from_directory
from prometheus_flask_exporter import PrometheusMetrics
import mysql.connector
import random
import os

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'db'
}


@app.route('/showItems')
def show_items():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query_albums = 'select title, artist, price, album, song_id, release_year from song'
    query_songs = 'select title, artist, price, album_id, release_year from album'
    cursor.execute(query_albums)
    albums = cursor.fetchall()
    list_albums = []
    for album in albums:
        list_albums.append(album[0], album[1], album[2],
                           album[3], album[4], album[5])
    cursor.close()
    conn.close()
    return list_albums



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

