import src.product_menu as p
import src.client_menu as c
import src.transaction_menu as t

MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
X. Exit
"""

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""
TRANSACTIONS_MENU = """
1. Add
2. Display all
3. Back
"""

products = {
    0: {
        'name': 'Nike shoes',
        'manufacturer': 'China',
        'category': 'football',
        'price': 100,
        'stock': 50
    },
    1: {
        'name': 'BMX',
        'manufacturer': 'Romania',
        'category': 'Bike',
        'price': 2000,
        'stock': 20
    }
}

clients = {
    1: {
        'last_name': 'Doe',
        'first_name': 'John',
        'date_of_birth': '26/04/1965',
        'email': 'john.doe@test.com'
    }
}

transactions = {
    1: {
        'name_of_product': 'BMX, 2',


    }
}
while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_second_menu = True
            while display_second_menu:
                print(PRODUCTS_MENU)


                option = input('Select an option from the product menu: ').lower()

                if option == '1':
                    p.add_product(products)
                elif option == '2':
                    p.remove_product(products)
                elif option == '3':
                    p.update_product(products)
                elif option == '4':
                    p.display_products(products)
                elif option == 'x':
                    display_second_menu = False
                else :
                    print('No such option')

        case '2':
            display_third_menu = True
            while display_third_menu:
                print(PRODUCTS_MENU)

                option = input('Select an option from the product menu: ').lower()

                if option == '1':
                    c.add_client(clients)
                elif option == '2':
                    c.remove_client(clients)
                elif option == '3':
                    c.update_client(clients)
                elif option == '4':
                    c.display_clients(clients)
                elif option == 'x':
                    display_third_menu = False
                else:
                    print('No such option')

        case '3':
            display_transaction_menu=True
            while display_transaction_menu:
                print(TRANSACTIONS_MENU)
                option=int(input('Select an option from the transaction menu: '))

                if option=='1':
                    t.add_transaction(transactions)
                elif option =='2':
                    t.display_transactions(transactions)
                else :
                    display_transaction_menu=False

















