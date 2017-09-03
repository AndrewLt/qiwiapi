def roulette() -> None:
    '''The main game loop'''
    # Initialisation of variables and stats

    Stats = {}

    Stats['red_numbers'] = [1, 3, 5, 7, 9, 12,
                            14, 16, 18, 19, 21, 23,
                            25, 27, 30, 32, 34, 36]

    Stats['black_numbers'] = [2, 4, 6, 8, 10, 11,
                              13, 15, 17, 20, 22, 24,
                              26, 28, 29, 31, 33, 35]

    Stats['zero_numbers'] = ['0', '00']

    Stats['ALL_NUMBERS'] = Stats['red_numbers'] + Stats['black_numbers'] + ['0'] + ['00']

    Stats['previous_spins'] = []

    Stats['spins'] = 0
    Stats['red'] = 0
    Stats['black'] = 0
    Stats['even'] = 0
    Stats['odd'] = 0
    Stats['first'] = 0
    Stats['second'] = 0

    Stats['player_money'] = 1000  # in pennies probably

    jet_fuel_cant_melt_steel_beams = True  # Illuminati Confirmed

    # Here we fucking go
    while jet_fuel_cant_melt_steel_beams:
        try:
            print_stats(Stats)
        except:
            print('Welcome to the best roulette simulator ever')  # sounds gr8 m8 i rate 8/8
        all_bets = []
        while jet_fuel_cant_melt_steel_beams:
            another = input('Do you want to make another bet? [yes/no] ')

            if another == 'yes':
                betting(all_bets, Stats)
            elif another == 'no':
                break
            else:
                print('Command not recognized, try again.')
                continue
        spin_wheel(all_bets, Stats)


# Twilight is best pony
def print_stats(Stats: dict) -> None:
    '''Prints stats to output.
    Does not work without stats'''
    for spin in Stats['previous_spins']:
        print('\t{:3}	{:5}	{:5}'.format(spin[0], spin[1],
                                              spin[2]))  # number, color, even. There should be a better way to do this
    print()
    print('\tRed : {:5.0f}%  Black:{:5.0f}%'.format(Stats['red'] / Stats['spins'] * 100,
                                                    Stats['black'] / Stats['spins'] * 100))
    print('\tEven: {:5.0f}%  Odd  :{:5.0f}%'.format(Stats['even'] / Stats['spins'] * 100,
                                                    Stats['odd'] / Stats['spins'] * 100))
    print('\t1-18: {:5.0f}%  19-36: {:5.0f}'.format(Stats['first'] / Stats['spins'] * 100,
                                                    Stats['second'] / Stats['spins'] * 100))
    print('Your money: $', Stats['player_money'])


# Nonon is cuter than Ryuko tbh


def betting(all_bets: list, Stats: dict) -> None:
    choices = ['red', 'black', 'even', 'odd', 'first', 'second', '1third', '2third', '3third', 'zeros']

    bet = input('''Do you want to bet [red], [black], [even], [odd], [first] half,
	 [second] half, [1third] (1-12), [2third] (13-24), [3third] (25-36),
	 single [number], or both [zeros]? ''')

    if bet in choices:
        ammount = int(input('You have ${} remaining.\nHow much do you want to bet? '.format(Stats['player_money'])))
        if ammount <= Stats['player_money']:
            Stats['player_money'] = Stats['player_money'] - ammount
            all_bets.append([bet, ammount])
        else:
            print('Not enough money')
    elif bet == 'number':
        num = input('Which number do you want to bet on (including 0 or 00) ? ')
        ammount = int(input('You have ${}.\nHow much do you want to bet? '.format(Stats['player_money'])))
        if ammount <= Stats['player_money']:
            Stats['player_money'] = Stats['player_money'] - ammount
            all_bets.append([bet, ammount])
        else:
            print('Not enough money')
    else:
        print('Command not recognized.')


# Pony is love. Pony is life.
def spin_wheel(all_bets: list, Stats: dict) -> None:
    '''Spins wheel and pays bets'''
    from random import choice

    num = choice(Stats['ALL_NUMBERS'])
    Stats['spins'] += 1
    if num in Stats['red_numbers']:
        color = 'red'
        Stats['red'] += 1
    elif num in Stats['black_numbers']:
        color = 'black'
        Stats['black'] += 1
    else:
        color = 'green'

    if num == '0' or num == '00':
        evenOrOdd = 'zero'  # why not have twice for good measure?
    elif num % 2 == 0:
        evenOrOdd = 'even'
        Stats['even'] += 1
    else:
        evenOrOdd = 'odd'
        Stats['odd'] += 1

    if (int(num) >= 1) and (int(num) <= 18):
        Stats['first'] += 1
    elif (int(num) >= 19) and (int(num) <= 36):
        Stats['second'] += 1
    spin = [str(num), color, evenOrOdd]
    Stats['previous_spins'].append(spin)
    if len(Stats['previous_spins']) > 20:
        Stats['previous_spins'].pop(0)  # there is a much better way to do this but I can't seem to find a fuck to give
    print(
        ' This spin: {:3}	{:5}	{:5}'.format(spin[0], spin[1], spin[2]))  # there should be a better way to do this
    winnings = 0

    for bet in all_bets:
        if (bet[0] == 'zeros') and ((num == '0') or (num == '00')):
            winnings += 18 * bet[1]
            print('Bet {} pays {}'.format(bet[0], 18 * bet[1]))
        elif bet[0] == num:
            winnings += 37 * bet[1]
            print('Bet {} pays {}'.format(bet[0], 37 * bet[1]))

        elif (bet[0] == color) or (bet[0] == evenOrOdd) or ((bet[0] == 'first') and (num < 19)) or (
            (bet[0] == 'second') and (num > 18)):
            winnings += 2 * bet[1]
            print('Bet {} pays {}'.format(bet[0], 2 * bet[1]))

        elif ((bet[0] == '1third') and (num >= 1) and (num < 13)) or (
                (bet[0] == '2third') and (num >= 13) and (num < 25)) or (
                (bet[0] == '3third') and (num >= 25) and (num <= 36)):  # such boolean. very branching. wow.
            winnings += 3 * bet[1]
            print('Bet {} pays {}'.format(bet[0], 3 * bet[1]))
        else:
            print('Bet {} loses ${}'.format(bet[0], bet[1]))

    Stats['player_money'] += winnings


roulette()