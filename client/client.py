from flask import Flask, render_template, request
import mysql.connector as connector
from redis import Redis
import random
import requests
import os

config_db = {
    'user': 'db',
    'password': '1224',
    'host': 'db',
    'port': '3306',
    'database': 'db'
}


def show_items(url):
    request_url = url + "/showItems?"
    return requests.get(request_url)


def buy_album(url, id):
    pass


def buy_song(url, id):
    pass


def operate(index, url):
    if index == 1:
        items = show_items(url)
        print(items)
    elif index == 2:
        id = input("Write album id: ")
        buy_album(url, id)
    elif index == 3:
        id = input("Write song id: ")
        buy_song(url, id)
    else:
        print('Now exiting...')
        exit()


def print_app():
    print("Choose an option:\n")
    print("1: Visualize the items in shop")
    print("2: Buy an album")
    print("3: Buy a song")
    print("4: Exit")


if __name__ == "__main__":
    print("Welcome to the Online Music Shopping")
    url = "http://127.0.0.1:8888/"
    while True:
        print_app()
        option = input("Write option: ")

        option = int(option)
        if option < 1 or option > 6:
            print("Given option not in range [1, 6]")
            continue
        operate(int(option), url)
