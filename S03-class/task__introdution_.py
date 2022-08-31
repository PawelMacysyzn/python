

cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7
}

cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}


def show_cake_info_from_list(func):
    def wrapper(*args, **kwargs):

        if type(*args) is list:
            for arg in list(args):
                for ar in arg:
                    func(ar)

        else:
            func(*args)

        return None
    return wrapper


@show_cake_info_from_list
def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'].capitalize(), cake['glaze'].capitalize(), cake['text'], cake['weight']))


show_cake_info(cake_01)


cake_list = list()

cake_list.extend([cake_01, cake_02])

show_cake_info(cake_list)
