"""
Modules for sea battle game
"""
import random
import copy
from battle_ship import const


def generate_size():
    """
    Generates random size of game field
    :return: int
    """
    return random.randint(*const.RAND_LIMIT)


def generate_field(size):
    """
    Generates a game field matrix
    :param size: int
    :return: nested list
    """
    field = [[const.EMPTY] * (size + 1) for i in range(0, size + 1)]
    field[0] = [' '] + [str(x) for x in range(0, size)]
    i = 1
    while i <= size:
        field[i][0] = str(i - 1)
        i += 1
    return field


def set_ships(empty_field):
    """
    Set ships on game field
    :param empty_field: nested list
    :return: nested list
    """
    temp_field = copy.deepcopy(empty_field)
    ship_count = len(empty_field) - 1
    while ship_count > 0:
        x, y = input_coordinates()
        if coordinates_correct(temp_field, x, y) and is_empty(temp_field, x, y):
            x, y = int(x), int(y)
            temp_field[y + 1][x + 1] = const.SHIP
            print_field(temp_field)
            ship_count -= 1
        else:
            continue
    return temp_field


def input_coordinates():
    """
    Takes two symbols separated by space, checks if input is correct
    :return: tuple(x, y), entered coordinates
    """
    x, y = None, None
    while x is None or y is None:
        try:
            x, y = input('\nShip coordinates x y (two digits separated by a space): ').split(' ')
        except Exception:
            print('\nMust be two digits SEPARATED by a space\n')
    return x, y


def coordinates_correct(temp_field, x, y):
    """
    Checks if coordinates are correct:
    - if they are convertible to integers
    - if they are within the playing field
    :param temp_field: nested list
    :param x: any
    :param y: any
    :return: bool
    """
    try:
        int(x) and int(y)
    except ValueError:
        print('\nMust be two DIGITS separated by a space\n')
        print_field(temp_field)
        return False
    try:
        temp_field[int(y) + 1][int(x) + 1]
    except IndexError:
        print('\nEntered coordinates outside the playing field\n')
        print_field(temp_field)
        return False
    return True


def is_empty(temp_field, x, y):
    """
    Checks if x, y cell in game field is empty
    :param temp_field: nested list
    :param x: int
    :param y: int
    :return: bool
    """
    if const.EMPTY != temp_field[int(y) + 1][int(x) + 1]:
        print('\nThis place is not empty\n')
        # print_field(temp_field)
        return False
    return True


def if_hit(pl_field, x, y):
    """
    Checks if there is a ship at the specified coordinates
    :param pl_field: nested list
    :param x: int
    :param y: int
    :return: bool
    """
    if const.SHIP == pl_field[int(y) + 1][int(x) + 1]:
        return True
    else:
        return False


def print_field(field):
    """
    Prints the game field
    """
    for i in field:
        print(i, end='\n')


def play_shot(target_field, enemy_map):
    """
    Takes coordinates of player`s shot, check them,
    changes enemy field and enemy map according to result
    :param target_field: nested list, game field of enemy
    :param enemy_map: nested list, map of enemy
    :return: bool
    """
    x, y = input_coordinates()
    if is_empty(enemy_map, x, y):
        if coordinates_correct(target_field, x, y):
            if if_hit(target_field, x, y) is True:
                target_field[int(y) + 1][int(x) + 1] = const.KILLED
                enemy_map[int(y) + 1][int(x) + 1] = const.KILLED
                print(f'\nHit!')
                return True
            else:
                enemy_map[int(y) + 1][int(x) + 1] = const.MISS
                print('\nMiss!\n')
                print_field(enemy_map)
                return False
    else:
        return True


def check_defeat(check_field):
    """
    Checks if there is any alive ship on the game field of enemy
    :param check_field: nested list
    :return: bool
    """
    check_list = []
    for i in range(0, len(check_field)):
        for j in range(0, len(check_field)):
            check_list.append(check_field[i][j])
    if const.SHIP in check_list:
        return False
    else:
        return True


if __name__ == '__main__':
    size = generate_size()
    assert len(generate_field(size)) == size + 1
    assert len(generate_field(size)[0]) == size + 1
    assert generate_field(size)[0][0] == ' '
    assert generate_field(size)[1][1] == '-'
    assert len(generate_field(size)) <= const.RAND_LIMIT[1] + 1
    (check_defeat([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]))
