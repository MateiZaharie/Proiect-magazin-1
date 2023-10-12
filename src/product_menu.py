def add_product(products: dict):
    name = input('Please provide a name: ')
    manufacturer = input('Please provide a manufacturer: ')
    category = input('Please provide a category: ')
    price = float(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[max(list(products.keys())) + 1] = product_info


def remove_product(products):
    product_id_to_delete = int(input('Please provide a product_id you want to delete: '))
    del products[product_id_to_delete]


def update_product(products):
    product_id_update = int(input('Please provide a product_id you want to update: '))
    product_name = products[product_id_update]['name']
    product_manufacturer = products[product_id_update]['manufacturer']
    print(f'the name of the product is {product_name}')
    print(f'the manufacturer of the product is {product_manufacturer}')

    category = input('Please provide a category: ')
    price = float(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': product_name,
        'manufacturer': product_manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[product_id_update] = product_info


def display_products(product_dict: dict):
    for product in product_dict:
        print(product_dict[product])
