"""
Your name:Prince Chabveka
Your student number:A01261829

All of your code must go in this file.
"""
import random
from art import text2art
from colorama import Fore, Style, Back
import itertools


def story_intro_level_zero_maputo_area() -> None:
    """Print story introduction.

    A function to print game story introduction. The string is printed when user starts the game in the
     area of Maputo at level zero.

    :postcondition: prints the string of game story introduction

    """
    print(Fore.LIGHTYELLOW_EX + "Once upon a time in the great land of ZAMUNDA, people lived in harmony.\nAll the "
                                "tribes including the AZIZI, the TIMON, and the PUMBA worked together in peace and "
                                "harmony.\nThey were hunter gatherers, blacksmiths, rainmakers, farmers - a powerful "
                                "society.\nAnd they all worshipped KING MUFASA.\nSCAR, MUFASA's brother got jealous and"
                                "stole RAFIKIS's (the wizard) magic portion to kill MUFASA.\nAfter Mufasa's death, all"
                                " the tribes turned against each other and peace was no more.\nSCAR killed MUFASA, but"
                                " not MUFASA's 4 children who managed to escape.\nNow, it is time for revenge.\n"
                                "MUFASA's children have different powers (classes) and you can choose one to embark on "
                                "your journey of revenge.\nHere you are at the grasslands of MAPUTO.\n"
                                "May the gods be with you\n\n" + Style.RESET_ALL)


def game_continuation() -> None:  # Chris said no Unit/Doc Test
    """Continue game.

    A function to allow the user to press Enter for the game to continue. This is invoked when player starts the game
    and when player reaches new levels/areas of the game.

    :postcondition: Asks for user input, that is, pressing enter to continue game

    """

    player_start = False
    while not player_start:
        input("Press ENTER  to continue")
        player_start = True


def maputo_welcome() -> None:  # Chris said no Unit/Doc Test
    """Print string Maputo.

    A function to print the string Maputo. The string is styled with art and printed in color.

    :postcondition: prints string Maputo in color and art style

    """
    maputo = text2art("Maputo", font='black', chr_ignore=True)
    print(Fore.BLACK + Back.YELLOW + maputo + Style.RESET_ALL)


def zaire_welcome() -> None:  # Chris said no need to test ASCII art
    """Print string ZAIRE.

    A function to print the string ZAIRE. The string is styled with art and printed in color.

    :postcondition: prints string ZAIRE in color.

    """

    zaire = text2art("ZAIRE", font='black', chr_ignore=True)
    print(Fore.BLACK + Back.YELLOW + zaire + Style.RESET_ALL)


def story_intro_level_one_zaire_area(character: dict) -> None:
    """Print zaire area introduction.

    A function to print introduction of zaire area to the user. The string is formatted in yellow color.

    :precondition: character is a dictionary with character attributes
    :precondition: character dictionary must have 'Current level' key with value
    :postcondition: prints string in yellow color.
    :postcondition: dictionary character is not changed

    """
    print(
        Fore.LIGHTYELLOW_EX + f"Rumours have spread like wildfire that a {character['Current level']} "
                              f"made it through the grasslands of MAPUTO.\nScar still thinks this is a joke so he sends"
                              f"the Zaire tribes to spy. If they find you, they will battle you.\nAny scratch from"
                              f"them is deadlier.\nBut you are now a {character['Current level']} so you feel"
                              f"prepared. ZAMUNDA's peace must be restored!\nMay the gods be with you" + Style.RESET_ALL
    )


def story_level_two_zamunda_area(character: dict) -> None:  # Chris said Unit/Doc Test
    """Print zamunda area introduction.

    A function to print introduction of zamunda area. The string is styled in color.

    :param character: a dictionary with character's attributes
    :precondition: character is a dictionary
    :precondition: character dictionary has 'Current Level' key and its value
    :postcondition: prints zamunda introduction story
    :postcondition: the string printed is formatted with the character's Current Level
    :postcondition: character dictionary is not changed

    """

    print(Fore.BLUE + f"SCAR thought you were a joke.\nNot until you defeated the level two tribes, including the all "
                      f"mighty RAFIKI tribe.\nYou are taken through the entrance of ZAMUNDA.\n" +
          Fore.RED + "▂▃▅▇█▓▒░۩۞۩        ۩۞۩░▒▓█▇▅▃▂ " + Style.RESET_ALL +
          "The rest of the tribes gather around."
          f"\nEveryone wants a glimpse of the almighty {character['Current level']}.\nCan you defeat SCAR?\n"
          f"Drums beat and horns blow as you prepare for battle.\n"
          f"A circle forms and you are pushed into the middle.\nThe tribes make way for SCAR who studs towards you")


def zamunda_welcome() -> None:  # Chris said no need to test ASCII art
    """Print ZAMUNDA.

    A function to print string ZAMUNDA. The string is styled with art and color.
    :postcondition: prints styled string ZAMUNDA

    """

    zaire = text2art("ZAMUNDA", font='black', chr_ignore=True)
    print(Fore.BLACK + Back.YELLOW + zaire + Style.RESET_ALL)


def print_stars() -> None:  # Chris said don't use recursion
    """Print star pattern.

    A function to print multiple * in a pattern.

    :postcondition: prints multiple * in a pattern

    """
    rows = 6
    columns = 9
    for row_num in range(rows, -1, -1):  # loop backwards, iterates through rows
        for column_num in range(columns, 0, -1):  # columns
            print(end=" ")
        columns += 1
        for column_num in range(0, row_num + 1):  # print stars in each row
            print("*", end=" ")  # single space for stars
        print("")


def print_star_transition() -> None:
    """Print transition stars.

    A function to print star pattern 3 times.

    :postcondition: prints multiple * 3 times

    """
    for _ in range(3):
        print_stars()


def make_class() -> dict:
    """"Create dictionary of classes.

    A function to create a dictionary of 4 classes for adventure game.

    :postcondition: creates a dictionary with 4 main keys representing game classes for the user to choose from
    :return: a dictionary

    """
    fighter_levels = ['novice', 'soldier', 'ultimate']
    witcher_levels = ['tinkerbell', 'vampire', 'witcher']
    thief_levels = ['novice', 'gambit', 'aladin']
    hunter_levels = ['Bantu', 'Zulu', 'Masai']
    classes = {'fighter': {'levels': fighter_levels, 'special_attack': 'sword',
                           'max_damage_points': list(zip(fighter_levels, [20, 30, 40])),

                           'max_Current_HP': list(zip(fighter_levels, [50, 70, 80])),

                           'experience_to_next_level': {'soldier': 200, 'ultimate': 400},

                           'weapon': 'AK gun ' + Fore.RED + '︻デ═一 ' + Style.RESET_ALL},

               'witcher': {'levels': witcher_levels, 'special_attack': 'magic',

                           'max_damage_points': list(zip(witcher_levels, [40, 50, 55])),

                           'max_Current_HP': list(zip(witcher_levels, [50, 70, 80])),

                           'experience_to_next_level': {'vampire': 300, 'witcher': 500},

                           'weapon': 'x gun ' + Fore.RED + '╦̵̵̿╤─ ҉ ~' + Style.RESET_ALL},

               'thief': {'levels': thief_levels, 'special_attack': 'steal',

                         'max_damage_points': list(zip(thief_levels, [30, 40, 50])),

                         'experience_to_next_level': {'gambit': 390, 'aladin': 550},

                         'max_Current_HP': list(zip(thief_levels, [30, 40, 50])),

                         'weapon': 'sm gun ' + Fore.RED + '︻╦╤─' + Style.RESET_ALL},

               'hunter': {'levels': hunter_levels, 'special_attack': 'knobkerrie',

                          'max_damage_points': list(zip(hunter_levels, [40, 60, 80])),

                          'experience_to_next_level': {'Zulu': 400, 'Masai': 600},

                          'max_Current_HP': list(zip(hunter_levels, [50, 60, 70])),

                          'weapon': 'sm gun ' + Fore.RED + '︻╦̵̵͇̿̿̿̿╤──' + Style.RESET_ALL}}
    return classes


def make_character(level=0) -> dict:  # no doctest, requires user input
    """"Make character dictionary.

    A function to make character dictionary for adventure game.

    :precondition: level is an integer
    :precondition: level is less than 3
    :postcondition: creates character dictionary with user's chosen class
    :return: a dictionary with character attributes

    """

    available_classes = {'1': 'fighter', '2': 'witcher', '3': 'thief', '4': 'hunter'}
    name = input("What shall I call you?: \n").upper()
    valid_class = False
    character = {}
    while not valid_class:
        print(f'Welcome ' + Fore.BLUE + name + Style.RESET_ALL +
              '.\nThe following classes are available\n'
              f'___________________________________________________________________\n' +

              Fore.YELLOW + f'Fighter: An established warrior' + Style.RESET_ALL +

              Fore.MAGENTA + f'\nWitcher: A master of the dark arts\n' + Style.RESET_ALL +

              Fore.CYAN + f'Thief: Street smart. Cunning. Can convince black is white.\n' + Style.RESET_ALL +

              Fore.BLUE + 'Hunter: Mighty and fast and furious Safari' + Style.RESET_ALL)

        chosen_class = input(

            "Choose class: \nfighter `----> Press 1 \nwitcher ----> Press 2 \nthief ----> Press 3 \nhunter "
            "----> Press 4 \n"
        )

        if chosen_class not in list(available_classes.keys()):
            print(
                Fore.RED + 'Invalid class, only possible classes are ["1 for fighter", "2 for witcher", "3 for thief", '
                           '"4 for hunter"]\nPlease enter a valid class' + Style.RESET_ALL
            )
            continue
        else:
            valid_class = True
            character['class_attributes'] = make_class()[available_classes[chosen_class]]  # class & attributes
            character = {'xp': 0,

                         'name': name,

                         'class': available_classes[chosen_class],

                         'class_attributes': make_class()[available_classes[chosen_class]],

                         'Current level': character['class_attributes']['levels'][level],

                         'location levels': ['Maputo', 'Zaire', 'Zamunda'],

                         'Current location': 'Maputo',

                         'Current HP': character['class_attributes']['max_Current_HP'][level][1],

                         'X-coordinate': 0, 'Y-coordinate': 0,

                         'Current_damage_points': character['class_attributes']['max_damage_points'][level][1],

                         'weapon': character['class_attributes']['weapon']}

    print('You have chosen {}.\n A great adventure awaits!'.format(character['class'].upper()))
    return character


def make_board_map_maputo(rows: int, columns: int) -> list:  # requires random int, no doctest
    """Create nested list.

    A function to create nested list representing game board map for maputo area in level zero.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows is an integer and >= 25
    :precondition: columns is an integer and >= 25
    :postcondition: creates a nested list representing a 25 by 25 game board
    :return: a nested list

    """
    board = [['\u001b[37;1m*\u001b[0m' for _ in range(rows)] for _ in range(columns)]
    for _ in range(25):
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[31m🐍\u001b[0m'
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[32m🐫\u001b[0m'
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[34m🐘\u001b[0m'
    board[24][20] = 'SCR'  # Boss fixed position at the end
    return board


def make_board_map_zaire(rows: int, columns: int) -> list:
    """Create nested list.

        A function to create nested list representing game board map for zaire area in level one.

        :param rows: an integer
        :param columns: an integer
        :precondition: rows is an integer and >= 25
        :precondition: columns is an integer and >= 25
        :postcondition: creates a nested list representing a 25 by 25 game board
        :return: a nested list

    """
    board = [['\u001b[37;1m*\u001b[0m' for _ in range(rows)] for _ in range(columns)]
    for _ in range(25):
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '🐒'
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[32m🦏\u001b[0m'
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '🦒'
    board[24][20] = 'SCR'  # Boss fixed position
    return board


def make_board_map_boss(rows: int, columns: int) -> list:
    """Create nested list.

    A function to create nested list representing game board map at level two, in Zamunda area. The character is
    automatically facing Scar, the boss near bottom right corner.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows is an integer and >= 25
    :precondition: columns is an integer and >= 25
    :postcondition: creates a nested list representing a 25 by 25 game board
    :return: a nested list

    """
    board = [[Fore.RED + '*' + Style.RESET_ALL for _ in range(rows)] for _ in range(columns)]
    for _ in range(25):
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = Fore.LIGHTWHITE_EX + '⤀' + Style.RESET_ALL
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[32m🐫\u001b[0m'
        board[random.randint(0, rows - 2)][random.randint(0, rows - 2)] = '\u001b[34m🐘\u001b[0m'
    board[24][19] = 'YOU'
    board[24][20] = '🦁'  # Boss fixed position at the end
    board[23][21] = ''
    board[23][19] = ''
    board[23][20] = ''
    board[24][21] = ''
    return board


def random_descriptions(character: dict) -> str:
    """Return location description.

    A function to return random description of character's location based on character's area on game board.

    :param character: a dictionary with character's attributes
    :precondition: dictionary character has 'Current location' key
    :postcondition: dictionary character is not changed
    :postcondition: finds random string in respective list of character's area
    :return: a string

    """
    maputo_descriptions = [
        "MAPUTO is a land of beauty. And this scenery is an example. Sometimes you scratch your head"
        "because you don't know where to go.\n(⊙.☉)7\nA Hornbill bird flies by,  enjoying the sun."
        "You could kill it but Hornbills are a sign of good luck.\nYou keep moving\n"
        "___________________________________________________________________\n",

        "This is the village of LILONGWE. You see a member of the Timon_tribe but he is drunk\n'Come here!"
        "he says'. He gives an old wooden cup with opaque beer\n（ ^_^）o自自o（^_^ \nYou are friends for now.\n"
        "___________________________________________________________________\n",

        "You look down.\n(._.)\nYou see animal footprints.Hmmm, something was here.\nBut remember, animals "
        "always come from behind. better be careful.\n"
        "___________________________________________________________________\n",

        "There is a small pond here. You drink some water.\n"
        + Fore.LIGHTBLUE_EX + '`·.¸¸ ><((((º>.·´¯`·><((((º>' + Style.RESET_ALL + "\nThe small fish"
        "looks beautiful.\n___________________________________________________________________\n",

        "Here lie the remains of an elephant. You wonder which tribe hunted it. Or which animal.\nYou pick "
        "a bone which might be useful later and put it in your bag.\nYou light up a cigarette."
        "  (̅_̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅_̅̅_̅()\n'Rest Bafethu', you hear the wind whisper\n"
        "___________________________________________________________________\n",

        "This seems like a quiet place. You sit down to write some ideas.\nPerhaps its about how you will "
        "defeat SCAR?\n" + Fore.LIGHTRED_EX + "((̲̅ ̲̅(̲̅C̲̅r̲̅a̲̅y̲̅o̲̅l̲̲̅̅a̲̅( ̲̅((> " + Style.RESET_ALL +
        "\nFailing to plan is planning to fail\n___________________________________________________________________\n"

    ]

    zaire_descriptions = [
        "You see a sign. It says 'MUFASA_TRIBE'.\n" + Fore.RED + "➶➶➶➶➶ƭεรƭ➷➷➷➷➷" + Style.RESET_ALL +
        "This gives you shivers. But you are brave.\nbThe sun is setting. Maybe you need some rest?\n"
        "___________________________________________________________________\n",

        "You are on top of the Kilimanjaro mountains. From here you can see ZAMUNDA. Still a bit"
        "far, but you can make it. 人人人人人人\n"
        "___________________________________________________________________\n",

        "You see a gate\n" + Fore.GREEN + "▂▃▅▇█▓▒░zaire-ruins░▒▓█▇▅▃▂" + Style.RESET_ALL +
        "\n.These are the old Zaire ruins. Deserted and nothing much to see here.You enter and roam "
        "around.\n(˚ㄥ_˚)\nWho built this? and why did they leave? MUST BE SCAR! he needs to be stopped\n"
        "___________________________________________________________________\n",

        "Zaire means the land of the fortune.The Nala tribe named it. And you find a little treasure\n" +
        Fore.BLACK + "[¯ↂ■■ↂ¯]" + Style.RESET_ALL + "YOu hear some music from this little treasure\nHow is "
                                                    "this possible? The gods must be crazy\n"
        "___________________________________________________________________\n",

        "ᕦ(ò_óˇ)ᕤ\nSomeone who needs to fight scar must exercise. You do so here and feel rejuvenated.\n"
        "Well done!\n ___________________________________________________________________\n"

    ]

    if character['Current location'] == 'Maputo':
        return maputo_descriptions[random.randint(0, len(maputo_descriptions) - 1)]
    elif character['Current location'] == 'Zaire':
        return zaire_descriptions[random.randint(0, len(zaire_descriptions) - 1)]


def make_board_descriptions(rows: int, columns: int, character: dict) -> dict:
    """Create board descriptions dictionary.

    A function to map random descriptions to board map.

    :param rows: a positive integer value
    :param columns: a positive integer value
    :param character: a dictionary of character's attributes
    :precondition: parameter rows is a positive integer
    :precondition: character dictionary has key 'Current location'
    :precondition: character dictionary's 'Current location' is one of 'Maputo' or 'Zaire'
    :precondition: parameter columns is a positive integer
    :precondition: rows and columns are equal
    :precondition: function random_descriptions must be implemented first
    :postcondition: creates a dictionary for each row and columns tuple key,
                    there is a generated random string as value
    :postcondition: created key of rows and columns serve as a set of X and Y
                    coordinates on the game board
    :postcondition: for each tuple key, the generated value is a string
    :return: a dictionary with rows and columns as tuple keys and value as a string

    """
    board_description = {(row, column): random_descriptions(character) for row in range(rows) for column in
                         range(columns)}
    return board_description


def describe_current_location(character: dict, board_description: dict) -> None:
    """Print character's current location.

    A function to print a description of character's current location on game board.

    :param character: a dictionary with character's X and Y coordinates
    :param board_description: a dictionary that maps coordinate tuples to string descriptions
    :precondition: param character is a dictionary  with X and Y coordinates as keys
                    and integer values
    :precondition: character's X and Y coordinates in dictionary must be less than or
                    equal to board's rows -1 and board's columns -1 respectively
    :precondition: character's X and Y coordinates are >= 0
    :precondition: param board is a dictionary with tuple (X,Y) coordinate keys and string values
    :postcondition: dictionary character is not changed
    :postcondition: dictionary board_description is not changed
    :postcondition: uses character's current X and Y coordinates to print description of
                    current location on game board
    :postcondition: dictionary character is not changed

    """
    print('You are at {}'.format((character['X-coordinate'], character['Y-coordinate'])))
    print(board_description[(character['X-coordinate'], character['Y-coordinate'])])


def area_level_foes(character: dict) -> tuple:
    """Generate random foe.

    A function to generate a random foe for the character to fight. The generated foe depends on the area the character
    is in.

    :param character: a dictionary with character's X and Y coordinates
    :precondition: param character is a dictionary  with X and Y coordinates as keys
                        and integer values
    :postcondition: creates 2 lists with respective foes and their area
    :postcondition: each list contains tuples in the form (foe_name, weapon)
    :precondition: param character has character's 'Current location' key
    :precondition: param character has 'class_attributes' key and list 'levels' as its value
    :postcondition: generates random foe depending on character's current area/level on game board
    :postcondition: character dictionary is not changed
    :return: a tuple with strings

    """
    # level one foes, the tribes of the Kalahari
    foes_level_maputo = [('Timon_tribe', 'GLAGWA'), ('Azizi_tribe', 'KPINGA'),
                         ('Babadou_tribe', 'NGUBA'), ('Pumba_tribe', 'ASSEGAI'),
                         ('Kamari_tribe', 'SHILED'), ('Zazu_tribe', 'SJAMBOK')]

    foes_level_zaire = [('Nala_tribe', 'SPEAR'), ('Rafiki_tribe', 'KNOBKERRY'),
                        ('Kovu_tribe', 'SHORT_SPEAR'), ('Mufasa_tribe', 'FIST')]

    for num, level in enumerate(character['class_attributes']['levels']):
        if level == character['Current level']:
            foe_level = num
            if foe_level == 0:
                return foes_level_maputo[random.randint(0, len(foes_level_maputo) - 1)]
            else:
                return foes_level_zaire[random.randint(0, len(foes_level_zaire) - 1)]


def get_user_choice() -> str:
    """Print valid directions and return user's chosen direction.

    A function to print valid directions and return user's chosen direction.

    :postcondition: prints valid direction options for the user
    :postcondition: gets user's desired direction as a string
    :postcondition: user's direction is one of East, West, North, South
    :return: a string of user's direction

    """
    all_directions = {"d": "East",
                      "a": "West",
                      "w": "North",
                      "s": "South",
                      'quit': 'quit'}
    valid_choice = False
    direction = ''
    while not valid_choice:
        direction = input(
            "Choose direction: \nEast `----> Press d \nWest ----> Press a \nNorth ----> Press w \nSouth "
            "----> Press s \nQUIT  ----> type 'quit'\n"
        )

        print(
            '____________________________________________________________________'
        )
        if direction not in all_directions.keys():
            print(
                Fore.RED + 'Invalid direction, only possible directions are ["d for East", "a for West", "w for North",'
                           '"s for South"]' + Style.RESET_ALL
            )
            continue
        else:
            direction = all_directions[direction]
            valid_choice = True
            print_stars()
    return direction


def validate_move(choice, character, rows, columns):
    """Validate user's direction.

        A function to validate user's choice of direction on game board.

        :param choice: a string of user's direction
        :param character: a dictionary with key,pair values of character's X and Y coordinates
                        location on game board and current HP
        :param rows: a positive integer
        :param columns: a positive integer
        :precondition: character is a dictionary with character's location on game board
        :precondition: dictionary character has X-coordinate and Y-coordinate keys with positive integer values
        :precondition: choice is a string
        :postcondition: checks if character can move in desired direction based on character's X, Y coordinates
        :postcondition: dictionary character is not changed
        :returns: a Boolean type, True if move is and False if move is invalid

    # check if you can move East
    >>> validate_move('East', {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5})
    True

    # check if you can move North
    >>> validate_move('North', {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5})
    False

    """

    if choice == 'East':
        return (character['X-coordinate'] + 1) <= rows - 1  # moving East
    elif choice == 'West':
        return (character['X-coordinate'] - 1) >= rows - rows  # moving West
    elif choice == 'South':
        return (character['Y-coordinate'] + 1) <= columns - 1  # moving south
    elif choice == 'North':
        return (character['Y-coordinate'] - 1) >= columns - columns  # moving West


def move_east(character: dict, board: list) -> None:
    """"Move East.

    A function to move character East of the game board. If character moves one step East and animal randomly appears
    West (one step behind him), the character eats the animal and gains extra experience points.

    :param character: a dictionary with character's X and Y coordinates and xp points
    :param board: nested list of representing game map
    :precondition: character is a dictionary
    :precondition: board is a 25 by 25 nested list
    :postcondition: updates character's X coordinate position on game board
    :postcondition: character's X coordinate is updated
    :postcondition: dictionary character is changed
    :postcondition: if animal appears at character's previous position on game board, character
                    dictionary xp key is updated

    """

    if board[character['Y-coordinate']][character['X-coordinate']] != '\u001b[37;1m*\u001b[0m':
        print(
            '\u001b[32;1mAnimals sneak from behind. As you move East An animal looms behind you. You turn around '
            'and smash the animal. It tastes good!\u001b[0m.'
        )
        character['X-coordinate'] += 1  # now update character
        character['xp'] += 25  # increase xp
    else:
        character['X-coordinate'] += 1  # now update character


def move_west(character, board):
    """"Move West.

    A function to move character West of the game board. If character moves West, X-coordinate decreases by 1. If
    animal then appears East (character's previous position),the character eats the animal
    and gains extra experience points.

    :param character: a dictionary with character's X and Y coordinates and xp points
    :param board: nested list of representing game map
    :precondition: character is a dictionary
    :precondition: board is a 25 by 25 nested list
    :postcondition: updates character's X coordinate position on game board
    :postcondition: character's X coordinate is updated
    :postcondition: dictionary character is changed
    :postcondition: if animal appears at character's previous position on game board, character
                    dictionary xp key is updated

    """

    if board[character['Y-coordinate']][character['X-coordinate']] != '\u001b[37;1m*\u001b[0m':
        print(
            '\u001b[32;1mAnimals sneak from behind. As you move West An animal looms behind you. You turn around '
            'and smash the animal. It tastes good!\u001b[0m.'
        )

        character['X-coordinate'] -= 1  # now update character
        character['xp'] += 25  # add xp points after eating
    else:
        character['X-coordinate'] -= 1  # now update character


def move_south(character, board):
    """"Move South.

        A function to move character South of the game board. If character moves South, Y-coordinate increases by 1. If
        animal then appears North (character's previous position),the character eats the animal
        and gains extra experience points.

        :param character: a dictionary with character's X and Y coordinates and xp points
        :param board: nested list of representing game map
        :precondition: character is a dictionary
        :precondition: board is a 25 by 25 nested list
        :postcondition: updates character's Y coordinate position on game board
        :postcondition: character's Y coordinate is updated
        :postcondition: dictionary character is changed
        :postcondition: if animal appears at character's previous position on game board, character
                    dictionary xp key is updated

       """
    if board[character['Y-coordinate']][character['X-coordinate']] not in ['\u001b[37;1m*\u001b[0m']:
        print(
            '\u001b[32;1mAnimals sneak from behind. As you move South An animal looms behind you. You turn around '
            'and smash the animal. It tastes good!\u001b[0m.'
        )
        character['Y-coordinate'] += 1  # now update character
        character['xp'] += 25
    else:
        character['Y-coordinate'] += 1  # now update character


def move_north(character, board):
    """"Move North.

        A function to move character North of the game board. If character moves North, Y-coordinate decreases by 1. If
        animal then appears South (character's previous position),the character eats the animal
        and gains extra experience points.

        :param character: a dictionary with character's X and Y coordinates and xp points
        :param board: nested list of representing game map
        :precondition: character is a dictionary
        :precondition: board is a 25 by 25 nested list
        :postcondition: updates character's Y coordinate position on game board
        :postcondition: character's Y coordinate is updated
        :postcondition: dictionary character is changed
        :postcondition: if animal appears at character's previous position on game board, character
                    dictionary xp key is updated

       """
    if board[character['Y-coordinate']][character['X-coordinate']] not in ['\u001b[37;1m*\u001b[0m']:
        print(
            '\u001b[32;1mAnimals sneak from behind. As you move North An animal looms behind you. You turn around '
            'and smash the animal. It tastes good!\u001b[0m.'
        )
        character['Y-coordinate'] -= 1  # now update character
        character['xp'] += 25
    else:
        character['Y-coordinate'] -= 1  # now update character


def print_character_on_map(character, direction):
    """"Show character on map.

    A function to show character on map.
    :param character: a dictionary with key,pair values of character's X and Y coordinates
                        location on game board and current HP
    :param direction: a string, one of ['North', 'East', 'West', 'South']
    :postcondition: prints map with character's position on game board
    :postcondition: prints map with randomly generated animals strings on game board
    :postcondition: character dictionary is changed

    """

    board = make_board_map_maputo(25, 25) if character['Current location'] == 'Maputo' else make_board_map_zaire(25, 25)
    if direction == 'East':
        move_east(character, board)
    elif direction == 'West':
        move_west(character, board)
    elif direction == 'South':
        move_south(character, board)
    else:
        move_north(character, board)
    board[character['Y-coordinate']][character['X-coordinate']] = '\u001b[33;1mYOU\u001b[0m'
    for _ in board:
        print(*_, sep='\t')


def check_for_foes() -> bool:
    """Check availability of foes.

    A function to check the availability of foes.

    :postcondition: Uses weighted probability to check if there is a foe
    :return: a boolean type, True if there is a foe or False if there is no foe

    >>> check_for_foes() in [True, False]
    True

    >>> check_for_foes() not in [True, False]
    False
    """
    possibility_of_finding_enemy = [True, False]
    probabilities = [0.2, 0.8]
    enemy = random.choices(possibility_of_finding_enemy, weights=probabilities)
    return enemy[0]


def character_run_away(character: dict) -> None:
    """Print character running away consequences.

    A function to notify user they ran away.

    :param character: a dictionary
    :precondition: character is a dictionary
    :postcondition: if character is damaged whilst running away,character dictionary is changed
    :postcondition: if character is not damaged whilst running away, character dictionary is not changed

    """
    print(Fore.YELLOW + "It is risky to turn your back on a foe." + Style.RESET_ALL)
    if check_if_character_is_damaged():  # check if user has been damaged whilst running
        print(
            u"\u001b[31;1mAs you turn your back, foe scratches you. Ouch! that cost 5 health points\u001b[0m"
        )
        character['Current HP'] -= 5  # update HP based on character level
    else:
        print(
            "\u001b[34;1mYou get away with it this time\u001b[0m"
        )  # print in blue if not scratched


def choose_to_battle() -> bool:
    """Check if character wants to fight foe.

    :postcondition: receives user input to check if they want to fight foe
    :postcondition: if chooser chooses no, dictionary character can be changed based on weighted probability that foe
                    damages them
    :postcondition: if choose choose yes, dictionary character is unchanged
    :return: A boolean type, True if user wants to fight else False if user chooses not to fight

    """

    print('____________________________________________________________________')
    fight_choice = False
    fight_foe = ''
    while not fight_choice:
        fight = input(
            "A tribe member is here, "
            "Would you like to fight?: \n Yes   -----> Press y\n No    -----> Press n: \n"
        )
        if fight not in ['y', 'n']:
            print(Fore.RED + "Invalid choice. Valid_choices are\n[y to fight or n to not fight]" + Style.RESET_ALL)
            continue
        else:
            fight_foe = True if fight == 'y' else False
            fight_choice = True
    return fight_foe


def fighting_scene(character: dict, there_is_a_challenger: bool) -> None:  # Chris said no test,
    """"Simulate fighting scene.

    :param character: a dictionary
    :param there_is_a_challenger: a boolean value
    :precondition: dictionary character has keys 'xp', 'Current HP', 'Current location', 'max_damage_points'
    :postcondition: simulates fighting scene from user's choice to battle until the end
    :postcondition: if user chooses not to fight and foe does not harm character,
                    dictionary character is not be changed
    postcondition: if user chooses not to fight and foe harms character, dictionary character is changed
    postcondition: if user chooses to fight and kills foe, dictionary character is changed

    """

    if there_is_a_challenger:
        choose_to_fight = choose_to_battle()  # tested
        if choose_to_fight:
            print(
                Fore.RED + "Foe says; 'It's unfortunate we have to resolve our differences this way.\n"
                           "They say when 2 elephants fight it's the grass that suffers\nYou draw out your " +
                character['weapon'] + " and make a loud HIYA sound as you prepare to fight\n"
                                      "____________________________________________________________________ "
                + Style.RESET_ALL
            )
            foe_health = 100
            battle(character, foe_health)  # no test for battle function
        else:
            character_run_away(character)  # tested


def foe_run_away(character: dict) -> bool:  # foe runs away
    """Check foe run away.

    A function to check if foe has run away during battle.

    :param character:  a dictionary
    :precondition: character is a dictionary with character's attributes
    :precondition: character has key 'xp'
    :postcondition: if foe runs away (True) dictionary character is changed. Value in key 'xp' is increased
    :postcondition: if foe doesn't run away, dictionary character is unchanged
    :return: a boolean type, True if foe runs away and False if foe doesn't run away

    """
    possibility_of_run = [True, False]
    probabilities = [0.2, 0.8]
    run = random.choices(possibility_of_run,
                         weights=probabilities)
    if run[0]:
        character['xp'] += 10
    return run[0]


def check_if_character_is_damaged() -> bool:  # check if character has been damaged
    """Check character damaged.

    A function to check if character has been damaged based on weighted probability.
    :postcondition: gets a boolean value based on weighted probability
    :return: a boolean type, True if character is damaged and False if not

    """
    possibility_of_damage = [True, False]
    probabilities = [0.2, 0.8]
    damage = random.choices(possibility_of_damage,
                            weights=probabilities)
    return damage[0]


def foe_damage_on_character(character: dict):  # remove HP points based on character current level
    """Reduce character HP points.

    A function to reduce character's HP based on character level if character is damaged.

    :param character: a dictionary of character's attributes
    :precondition: dictionary character has class attributes
    :postcondition: if character is damaged, user is notified
    :postcondition: if character is damaged, character's Current HP is reduced by a random number
    :postcondition: if character is at level 0, random number generated is in the range (15, 25)
    :postcondition: if character is at level 1, random number generated in the range (25,35)
    :postcondition: if character is damaged, dictionary character is changed
    :postcondition: if character is not damaged, dictionary character is not changed

    """
    if check_if_character_is_damaged():
        print(Fore.RED + "Foe's attack damages you" + Style.RESET_ALL)
        for num, level in enumerate(character['class_attributes']['levels']):
            if level == character['Current level']:
                foe_damage_level = num
                if foe_damage_level == 0:
                    character['Current HP'] -= random.randint(15, 25)  # range
                elif foe_damage_level == 1:
                    character['Current HP'] -= random.randint(25, 35)  # range


def battle(character: dict, foe_health: int) -> dict:
    """Simulate battle.

    A function to simulate character's battle with normal foe.

    :param character: a dictionary of character attributes
    :param foe_health: a positive integer
    :precondition: foe_health is a positive integer
    :precondition: character is a dictionary
    :precondition: character dictionary has keys 'xp', 'max_damage_points', 'Current  location', 'Current HP', 'weapon'
    :postcondition: dictionary character is changed
    :postcondition: if foe runs away, character's xp is increased
    :postcondition: if character runs away and is damaged, character's HP is reduced
    :postcondition: if character kills foe, character's xp increases
    :return: dictionary character

    """
    flee = False
    current_foe = area_level_foes(character)
    while not flee and foe_health > 0 and character['Current HP'] > 0:  # choose to fight and foe's not dead and alive
        print(
            f"Your foe is a member of the {current_foe[0]}. Foe takes his arrow and attacks.\n" +
            Fore.RED + "»»---------------------►'" + Style.RESET_ALL + "\n"
            f"The arrow is sharp and they attack with "
            "precision. You take out your gun and shoot\n.'̿' ̿'\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/'̿'̿ ̿'\n"
            f"Foe takes his special {current_foe[1]} and attacks again.\nFoe health now at {foe_health}\n"
            f"You current HP is {character['Current HP']}"
            f"\n____________________________________________________________________")

        check_foe_dying(foe_health)
        foe_health -= character['Current_damage_points']
        if foe_health > 0:  # first round has already gone
            stop_fighting = input(
                "Would you like to continue fight? :\nYes   -----> Press y\nRun away    -----> Press n"
            )
            flee = False if stop_fighting == 'y' else True
            if flee:  # character runs away
                character_run_away(character)  # condition met if stop_fighting = True
                flee = True  # character runs at end of round
            elif foe_run_away(character):  # chose to continue fight but foe ran away and no further damage to character
                print(Fore.RED + "Even though you are eager to fight\nFoe runs "
                                 "away\nYou earn 10 xp\n " + Style.RESET_ALL +
                      "points'____________________________________________________________________'")
                flee = True  # foe has run away
            elif not flee and not foe_run_away(character):  # foe is still there and you are fighting
                foe_damage_on_character(character)  # possible damage on character
        elif foe_health <= 0:  # foe dies
            character['xp'] += 100
            print(
                Fore.BLUE + 'Foe dies\nYou earn 100 experience points\nYou nurse your wounds\n'
                            'band-aid (̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ) ' + Style.RESET_ALL +
                '\n____________________________________________________________________'
            )
            flee = True
    print("Do you think that was a noble fight? Maybe!")
    return character


def check_foe_dying(foe_health):  # cannot doctest because of color,
    """Print if foe is dying.

    A function to notify user if foe is dying.

    :precondition: foe_health is a positive integer
    :postcondition: prints notification message based on foe's current health

    """

    if foe_health <= 30:
        print(Fore.RED + "Foe bleeds heavily, you are on the verge of victory" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "Foe has minor scratches, you have to fight harder!" + Style.RESET_ALL)


def check_new_level_attained(character: dict) -> bool:
    """Check character level attained.

    A function to check if character dictionary has earned enough experience points to go to the next class level.

    :param character: a dictionary of values
    :postcondition: checks if characters exp value is enough to go to next level
    :postcondition: character dictionary is not changed
    :return: A boolean type, True if new level is reached, False if not

    """

    for num, level in enumerate(character['class_attributes']['levels']):
        if level == character['Current level']:
            next_level = character['class_attributes']['levels'][num + 1]  # check next level
            return character['xp'] >= character['class_attributes']['experience_to_next_level'][next_level]


def update_character_level(character: dict) -> dict:  # new level has been attained
    """"Update character level.

    A function to update character's class level.

    :param character: a dictionary
    :postcondition: updates character's 'Current level', 'Current HP', 'Current_damage_points' and 'Current location'
                    key values
    :postcondition: dictionary character is changed
    :return: character dictionary

    """
    for num, level in enumerate(character['class_attributes']['levels']):
        if level == character['Current level']:  # check current level
            print(
                "\u001b[36;1mNEW LEVEL ATTAINED! 'One cannot stay {} for long\u001b[0m'".format(character['Current '
                                                                                                          'level'])
            )
            character['Current level'] = character['class_attributes']['levels'][num + 1]  # update level
            character['Current HP'] = character['class_attributes']['max_Current_HP'][num + 1][1]  # update Current Hp
            character['Current_damage_points'] = character['class_attributes']['max_damage_points'][num + 1][1]

            print(
                '\u001b[36;1mYou are now {}.\nYour maximum damage points have increased to {}.\nYour Current HP '
                'has increased to {}.\nYou can now battle stronger foes without hesitation!\n◄[🏆]► wow ◄[🥇]►\n'
                '\u001b[0m'.format(character['Current level'],
                                   character['Current_damage_points'], character['Current HP'])
            )
            character['Current location'] = character['location levels'][num + 1]  # update location
            return character


def can_fight_boss(character: dict) -> bool:
    """Check if character can fight boss.

    A function to check if character can fight boss.
    :postcondition: dictionary character is not changed
    :return: A boolean type, True if character can fight boss, False if character cannot

    >>> mock_character =  {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']}, 'Current level': 'novice'}
    >>> can_fight_boss(mock_character)
    False

    >>> mock_character ={'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']}, 'Current level': 'ultimate'}
    >>> can_fight_boss(mock_character)
    True

    """

    return character['Current level'] == character['class_attributes']['levels'][2]


def fight_boss(character: dict, boss_health: int) -> None:  # Chris said no test battle function
    """Fight boss.

    A function for character to fight boss.

    :param character: a dictionary
    :param boss_health: a positive integer
    :precondition: character dictionary has keys 'Current HP' and 'Current_damage_points'
    :postcondition: dictionary character is changed

    """
    print(
        Fore.RED + "'Who goes there!??', thunders the SCAR. This is an unfamiliar scent.'\n'You must be super brave to come "
                   "to my territory'\n"
                   f"You prepare your {character['class_attributes']['special_attack']} and say a little prayer."
                   f"\nThe gods took you all the way here not to let you die like a fly\nThe boss launches at you with fierce"
                   f" force and strikes first.\nYou stumble backwards and realize what is at stake here\n "
                   f"And you hit the boss back with equal force" + Style.RESET_ALL
    )
    boss_dead = False
    while not boss_dead and character['Current HP'] > 0:
        if boss_health > 0:
            print(
                f"You have {character['Current HP']} health left\nSCAR has {boss_health} health left"
            )
            input("Press ENTER to continue fight:\n")
            boss_health -= character['Current_damage_points']
            if boss_launch_special_attack():  # tested
                boss_special_attack(character)  # tested
                check_if_alive(character)  # tested
                check_boss_dying(boss_health)  # tested
            else:
                print(Fore.RED + "Scar attacks you. You lose 5 HP" + Style.RESET_ALL)
                character['Current HP'] -= 5
        else:
            boss_dead = True
            print(Fore.BLUE + "Scar is defeated! Zamunda is FREE\nAll praise thee" + Style.RESET_ALL)
    print("This is what we make of your story.")


def check_boss_dying(boss_health: int) -> None:
    """Print if boss is dying.

    A function to inform the user if the boss is dying.

    :param boss_health: an integer
    :precondition: boss_health is a positive integer
    :postcondition: check's boss_health and prints relative message if boss's health percentage is low or not

    """
    boss_health_percentage = (boss_health / 400) * 100
    if boss_health_percentage < 20:
        print(
            "\u001b[31;1mBoss bleeds heavily.\n You are on the verge of victory\u001b[0m"
        )
        print(
            f"\u001b[31;1mBoss health is at {boss_health}\u001b[0m\nThe tribes sing:"
        )
        for chant in itertools.repeat("SCAR IS DYING", 3):
            print(chant)
    else:
        print(
            "\u001b[34;1mBoss shows minor damage, you have to fight harder\u001b[0m"
        )
        print(
            f"\u001b[34;1mBoss health is at {boss_health}\u001b[0m"
        )


def boss_launch_special_attack() -> bool:  # 20 percent chance boss launches special attack on you
    """Check if boss launches special attack.

    A function to check if boss launches special attack based on weighted probability.

    :postcondition: checks if boss has launched special attack using probability
    :return: A boolean type, True if boss launches special attack, False if not

    """
    possibility_of_special_attack = [True, False]
    probabilities = [0.2, 0.8]
    special_attack = random.choices(possibility_of_special_attack, weights=probabilities)
    return special_attack[0]


def boss_special_attack(character: dict) -> None:
    """Boss attack character with random special attack.

    A function to randomly choose a special attack damage and type of attack.

    :param character: a dictionary
    :precondition: character is a dictionary
    :postcondition: dictionary character is changed

    """
    boss_attack_damage_levels = [10, 20, 30, 40]
    boss_attack_types = list(zip(list(map(lambda damage: 'deadly' if damage > 10 else 'mediocre',
                                          boss_attack_damage_levels)),
                                 boss_attack_damage_levels))

    attack_chosen_by_boss = boss_attack_types[random.randint(0, len(boss_attack_types) - 1)]
    print(Fore.RED + f"Boss launches special attack\n" + Style.RESET_ALL +
          f"This is {attack_chosen_by_boss[0]}!," +
          Fore.RED + f"You lose" + Style.RESET_ALL + f"{attack_chosen_by_boss[1]}")  # special attack reduces HP by more

    character['Current HP'] -= attack_chosen_by_boss[1]


def check_if_goal_attained(boss_health: int) -> bool:
    """"Check goal attained.

    A function to check if boss health has reduced to zero to denote goal achievement of killing the boss.

    :param boss_health: a positive integer
    :precondition: boss_health is an integer
    :postcondition: checks if boss health (int) is greater than zero
    :return: a boolean, True if boss health is >= 0 or False if boss health > 0

    >>> check_if_goal_attained(90)
    False

    >>> check_if_goal_attained(0)
    True
    """
    return boss_health <= 0


def check_if_alive(character: dict) -> bool:
    """Check if character's Current HP > 0.

    A function to check if character's Current HP is > 0, hence, still alive.

    :param character: a dictionary with character's X and Y coordinates
    :precondition: dictionary character is not empty
    :precondition: dictionay character has 'Current HP' key
    :postcondition: dictionary character is unchanged
    :return a boolean type. True if alive, False if killed

    >>> check_if_alive({'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0})
    You die
    False

    >>> check_if_alive({'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 1})
    True

    """
    if character['Current HP'] >= 30:
        print("Health-wise, you seem to be ok")
    elif character['Current HP'] > 0:
        print(Fore.RED + "You bleed heavily" + Style.RESET_ALL)
    else:
        print("You die")
    return character['Current HP'] > 0


def print_current_stats(character: dict) -> None:  # Chris said no Unit Test
    """Print character game stats.

    A function to print character's stats when playing the game.

    :precondition: character is a dictionary
    :precondition: dictionary character has keys 'xp', 'Current level', 'class_attributes', 'Current HP'
    :postcondition: prints character's relevant statistics for the user
    :postcondition: dictionary character is not changed

    """

    print(
        Fore.LIGHTBLUE_EX + f"Current HP:" + Style.RESET_ALL +
        f"{character['Current HP']} ==[]== " + Fore.RED + f"Current xp:" + Style.RESET_ALL +
        f"{character['xp']} ==[]== " + Fore.LIGHTYELLOW_EX + "Current level:" + Style.RESET_ALL +
        f"{character['Current level']} ==[]== " + Fore.LIGHTGREEN_EX + f"Points to next level:" + Style.RESET_ALL +
        f"{character['class_attributes']['experience_to_next_level']}"
    )


def recuperate(character: dict) -> None:
    """Increase Current HP.

    A function to increase Current HP in dictionary character.

    :param character: a dictionary
    :precondition: character dictionary has key 'Current HP'
    :postcondition: if value at key 'Current HP' <= 10 and > 0, dictionary character is changed
    :postcondition: if 'Current HP' is > 10, dictionary character is not changed

    >>> mock_character = {'Current HP': 20}
    >>> recuperate(mock_character)
    True
    """

    if 10 >= character['Current HP'] > 0:
        print(
            Fore.BLUE + "Not sure you can make it to Zamunda with this health. You pray to the gods for help.\nThey"
                        " hear you!.The gods increase your HP by 20" + Style.RESET_ALL)
        character['Current HP'] += 20


def check_update_to_zaire(character: dict) -> None:  # Chris said no Unit/Doctest (all called functions tested)
    """Check if character is updated to Zaire.

    A function to update character to Zaire level.

    :param character: a dictionary
    :precondition: character is a dictionary
    :precondition: character dictionary has all attributes from make_character function
    :postcondition: if character reaches new level, dictionary character is changed

    """
    character_at_new_level = check_new_level_attained(character)  # tested
    if character_at_new_level:  # so we go into boss level
        update_character_level(character)  # update character
        if character["Current location"] in ['Zaire', 'Maputo']:
            zaire_welcome()  # just prints
            game_continuation()
            story_intro_level_one_zaire_area(character)  # just prints


def boss_fight_scene(character: dict) -> None:  # Chris said no Unit/Doctest  # game function breakdown
    boss_health = 250
    fight_boss(character, boss_health)  # helper functions tested


def game(): # Chris said no Unit Test
    """Drive the main game loop.

    A function to drive the main game loop.

    """
    make_class()
    rows = 25
    columns = 25
    character = make_character()
    achieved_goal = False
    print('____________________________________________________________________')
    print_stars()
    print('____________________________________________________________________')
    story_intro_level_zero_maputo_area()
    game_continuation()
    maputo_welcome()
    print_star_transition()
    while not achieved_goal:
        print_current_stats(character)
        board_description = make_board_descriptions(rows, columns, character)
        check_update_to_zaire(character)  # character can have enough xp from eating animals
        if can_fight_boss(character):  # only met when reached level Zamunda to fight boss
            zamunda_welcome()
            game_continuation()
            story_level_two_zamunda_area(character)
            zamunda_map = make_board_map_boss(25, 25)
            for _ in zamunda_map:  # print board map
                print(*_, sep='\t')
            boss_fight_scene(character)
            achieved_goal = True
        else:
            direction = get_user_choice()
            if direction == 'quit':
                break
            else:
                valid_move = validate_move(direction, character, rows, columns)
                if valid_move:
                    print_character_on_map(character, direction)
                    describe_current_location(character, board_description)
                    there_is_a_challenger = check_for_foes()
                    fighting_scene(character, there_is_a_challenger)
                    achieved_goal = not check_if_alive(character)  # if character alive in level zero and one
                    recuperate(character)
                else:
                    print(u"\u001b[31;1m Ooops, you cannot move here\u001b[0m")
    print("But you've done what most dread!" + " \U0001f600 \U0001F602 " + "You are the bravest adventurer of all "
                                                                           "time\nYou "
                                                                           "receive star status. Dead or "
                                                                           "Alive!")
    print('____________________________________________________________________')


def main():
    game()


if __name__ == '__main__':
    main()
