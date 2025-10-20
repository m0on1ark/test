def generate_filenname(id):
    print(f'{id}\t->  data_{id:04}.txt')

       

generate_filenname(10)    
generate_filenname(1011)
generate_filenname(100)
def print_description(name, price):
    description = get_description(name, price)
    print(description)  
print_description('Oranges', 201)   