shop_list = []
type_of_article = ['shirt','scarf','glove','heat']
sizes = ['s','m','l','xl','xxl']


shop_list = [(a,b) for a in type_of_article for b in sizes] *20
print(shop_list)

removed_last = shop_list.pop()
print('Last item was sold: ',removed_last)

n = int(input('Which item nr would you like to remove: (0-398)'))
remove_item = shop_list[n]
shop_list.remove(remove_item)
print('This item was removed: ',remove_item)


restock = [removed_last, remove_item]
shop_list.append(restock)
# or shop_list = shop_list + restock
print(shop_list)
