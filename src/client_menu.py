def add_client(clients: dict):
    last_name = input('Please provide the client last name: ')
    first_name = input('Please provide the client first name: ')
    date_of_birth = float(input('Please provide the client date of birth: '))
    email = (input('Please provide the client email: '))

    client_info = {
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email,

    }
    clients[max(list(clients.keys())) + 1] = client_info


def remove_client(clients):
    client_id_to_delete = int(input('Please provide a client_id you want to delete: '))
    del clients[client_id_to_delete]


def update_client(clients):
    client_id_update = int(input('Please provide a client_id you want to update: '))


    last_name = input('Please provide the client last name: ')
    first_name = input('Please provide the client first name: ')
    date_of_birth =(input('Please provide the client date of birth: '))
    email=input('Please provide the client email: ')
    client_info = {
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email,
    }
    clients[client_id_update] = client_info


def display_clients(client_dict: dict):
    for client in client_dict:
        print(client_dict[client])