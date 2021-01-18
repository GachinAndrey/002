my_list = [28, 'True', False, None, 36.6, 'Текст']
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)