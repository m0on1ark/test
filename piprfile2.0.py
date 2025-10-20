
def split_price(price):
    price_zl = price // 100
    price_gr = price % 100
    return (price_zl,price_gr)
 
def get_description(name, price): 
    price_zl_gr = split_price(price)
    return f'price of {name} is {price_zl_gr[0]},{price_zl_gr[1]:02}.'

def print_description(name, price):
    description = get_description(name, price)
    print(description)  
print_description('Oranges', 201)   
