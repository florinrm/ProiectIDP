from flask import Flask, render_template, request
import mysql.connector as connector
from redis import Redis
import random
import os

config_db = {
'user': 'db',
'password': '1224',
'host': 'db',
'port': '3306',
'database': 'db'
}


def show_items():
    pass


def buy_album():
    pass


def buy_song():
    pass


def operate(index):
    if index == 1:
        show_items()
    elif index == 2:
        buy_album()
    elif index == 3:
        buy_song()
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
    while True:
        print_app()
        option = input("Write option: ")

        option = int(option)
        if option < 1 or option > 6:
            print("Given option not in range [1, 6]")
            continue
        operate(int(option))
