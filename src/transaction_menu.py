def add_transaction(transactions:dict):
    name_of_product=input('Write the name and quantity of the products transactioned: ')


    transactions_info = {
        'name_of_product' : name_of_product

    }
    transactions[max(list(transactions.keys()))+1] = transactions_info

def display_transactions(transaction_dict: dict):
    for transaction in transaction_dict:
        print(transaction_dict[transaction])