import requests 
import json
import sys
from flask import Flask, request


def print_option():
    print('Select the option in range [0-5]: ')
    print("0: Exit the program")
    print('1: Show all items from shop')
    print('2: Add item in cart')
    print('3: Withdraw item from cart')
    print('4: See items from cart')
    print('5: Finalise')


def main():
    url = "http://172.17.0.1:5000"
    print("Accessing server: " + url)
    print(url)
    server_url = url + "/connect"
    print("Testing connection...")
    response = requests.get(url = server_url, params = None)
    print("Connection to server succeded!")
    id_client = response.text
    print("Your client id is " + response.text)
    while True:
        print_option()
        option = input()
        if option == '0':
            print('Exiting...')
            print('Goodbye.')
            exit()
        elif option == '1':
            print('Showing items...')
            server_url = url + "/show_albums"
            response = requests.get(url = server_url, params = None)
            print(response.text)
        elif option == '2':
            print('Adding item...')
            server_url = url + "/add_album_cart"
            data = input("Type the id of item to be added in cart: ")
            response = requests.get(url = server_url, params = {'client_id' : id_client, 'item_id' : data})
            print(response.text)
        elif option == '3':
            print('Removing item...')
            server_url = url + "/remove_album_cart"
            data = input("Type the id of item to be deleted from cart: ")
            response = requests.get(url = server_url, params = {'client_id' : id_client, 'item_id' : data})
            print(response.text)
        elif option == '4':
            print('Showing buying cart...')
            server_url = url + "/show_buying_cart"
            response = requests.get(url = server_url, params = {'client_id' : id_client})
            print(response.text)
        elif option == '5':
            print('Proceeding to finalise shopping')
            server_url = url + "/finalise_buying"
            response = requests.get(url = server_url, params = {'client_id' : id_client})
            print(response.text)
        else:
            print('Invalid option, choose a valid one')
        

if __name__ == "__main__":
    main()