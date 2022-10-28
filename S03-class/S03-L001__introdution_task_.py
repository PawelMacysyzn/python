
cake_list = []

cake_01 = {'taste' : 'vanilia', 'glaze' : 'chocolade', 'text' : 'Happy Brithday', 'weight' : 0.7}
cake_02 = {'taste' : 'tee', 'glaze' : 'lemon', 'text' : 'Happy Python Coding', 'weight' : 1.3}


cake_list.append(cake_01)
cake_list.append(cake_02)


def show_cake_info(cake_list):
    for num, cake in enumerate(cake_list):
        print('{}. - {} cake with {} glaze with text "{}" of {} kg'.format(
            num, cake['taste'].capitalize(), cake['glaze'], cake['text'], cake['weight']))
 
show_cake_info(cake_list)





