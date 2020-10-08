"""
Sea battle game
"""
import copy
from battle_ship import utils


if __name__ == '__main__':
    empty_field = utils.generate_field(utils.generate_size())  # generates empty field with random size
    print('Game field:\n')
    utils.print_field(empty_field)

    print('\nSet ships field of player 1')
    pl_1_field = utils.set_ships(empty_field)
    pl_2_map = copy.deepcopy(empty_field)  # makes map of enemy game field

    print('\nGame field of player 2')
    pl_2_field = utils.set_ships(empty_field)
    pl_1_map = copy.deepcopy(empty_field)

    while True:

        while utils.check_defeat(pl_1_field) is False and utils.check_defeat(pl_2_field) is False:
            print(f'\nPlayer 1 shot:\n')
            utils.print_field(pl_1_map)
            if utils.play_shot(pl_2_field, pl_1_map):
                continue
            else:
                break

        while utils.check_defeat(pl_1_field) is False and utils.check_defeat(pl_2_field) is False:
            print(f'\nPlayer 2 shot\n')
            utils.print_field(pl_2_map)
            if utils.play_shot(pl_1_field, pl_2_map):
                continue
            else:
                break

        if utils.check_defeat(pl_1_field) is True:
            print('Player 2 has WON!')
            utils.print_field(pl_1_field)
            break

        if utils.check_defeat(pl_2_field) is True:
            print('Player 1 has WON!')
            utils.print_field(pl_2_field)
            break
