def get_nr_items(input_list):
    items = input_list.split(",")
    return len(items)


lista1 = "apple, banana, coco"
print(get_nr_items(lista1))
