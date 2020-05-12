import sys
import requests 


def print_options():
    print("Choose an option from the range [0-3]: ")
    print("0: Exit the program")
    print("1: Add a product in data base")
    print("2: Delete a product from data base")
    print("3: Show all items from data base")


def main():
    url = "http://172.17.0.1:5000"
    print("Accessing " + url)
    req_url = url + "/connect"
    print("Testing connection...")
    response = requests.get(url = req_url, params = None)
    print("Connection succeded!")
    result = response.text
    print(result)

    while True:
        print_options()
        option = input()
        if option == '0':
            print('Exiting...')
            print('Goodbye.')
            exit()
        elif option == '1':
            req_url = url + "/add_album"
            id_prod = input("Write item id: ")
            name = input("Write album name: ")
            artist = input('Write album artist: ')
            price = input("Write album price: ")
            params = {'id' : id_prod, 'name' : name, 'price' : price, 'artist': artist}
            response = requests.get(url = req_url, params = params)
            print(response.text)
        elif option == '2':
            req_url = url + "/remove_album"
            id_prod = input("Write item id:")
            response = requests.get(url = req_url, params = {'id' : id_prod})
            print(response.text)
        elif option == '3':
            req_url = url + "/show_database_items"
            response = requests.get(url = req_url, params = None)
            print(response.text)
        else:
            print("Invalid option, give a valid one")


if __name__ == "__main__":
    main()
