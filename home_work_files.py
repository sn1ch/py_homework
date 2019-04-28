from pprint import pprint


def composition_dict(list):
    if len(list) == 3:
        composition = {'ingridient_name': list[0], 'quantity': list[1], 'measure': list[2]}
    elif len(list) == 4:
        composition = {'ingridient_name': list[0] + ' ' + list[1], 'quantity': list[2], 'measure': list[3]}
    return composition


def main():
    with open('r.txt', encoding='utf8') as f:
        cook_book = {}
        for line in f:
            name = line.strip()
            amount = int(f.readline().strip())
            for i in range(amount):
                add_line = f.readline().replace('|', '').split()
                cook_book.setdefault(name, [])
                cook_book[name].append(composition_dict(add_line))
            f.readline()

        pprint(cook_book)

        def get_shop_list_by_dishes(dishes, person_count):
            shop_list = {}
            for items in dishes:
                if items in cook_book:
                    for ingredients_dict in cook_book[items]:
                        # print(k)
                        for items in ingredients_dict.values():

                            if items not in shop_list:
                                shop_list.setdefault(ingredients_dict['ingridient_name'],
                                                     {'measure': ingredients_dict['measure'],
                                                      'quantity': int(ingredients_dict['quantity']) * person_count})
                            else:
                                shop_list[items]['quantity'] += shop_list[items]['quantity']

            return shop_list

        pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


main()
