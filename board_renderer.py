from colorama import just_fix_windows_console, Fore

just_fix_windows_console


def render_board(game_positions):
    fields = {i: Fore.WHITE for i in range(40)}
    figures_on_b_fields = {key: 0 for key in game_positions.keys()}
    for color in game_positions:
        if color == "red":
            term_color = Fore.RED
        elif color == "blue":
            term_color = Fore.BLUE
        elif color == "yellow":
            term_color = Fore.YELLOW
        elif color == "green":
            term_color = Fore.GREEN
        term_reset = Fore.RESET
        for field_id in game_positions[color]:
            if field_id == -1:
                figures_on_b_fields[color] += 1
            else:
                fields[field_id] = term_color
    # print(fields)
    # print(figures_on_b_fields)
    # sorry for this gore code from hell :=)
    field = """
    OO      {28}o{reset} {29}o{reset} {30}O      OO
    OO      {27}o{reset} O {31}o{reset}      OO
            {26}o{reset} O {32}o{reset}
            {25}o{reset} O {33}o{reset}
    {20}O {21}o{reset} {22}o{reset} {23}o{reset} {24}o{reset} O {34}o{reset} {35}o{reset} {36}o{reset} {37}o{reset} {38}o{reset}
    {19}o{reset} O O O O   O O O O {39}o{reset}
    {18}o{reset} {17}o{reset} {16}o{reset} {15}o{reset} {14}o{reset} O {4}o{reset} {3}o{reset} {2}o{reset} {1}o{reset} {0}O
            {13}o{reset} O {5}o{reset}
            {12}o{reset} O {6}o{reset}
    OO      {11}o{reset} O {7}o{reset}      OO
    OO      {10}O {9}o{reset} {8}o{reset}      OO
    """.format(*fields.values(), reset=term_reset)
    print(field)


if __name__ == "__main__":
    game_positions = {
        "red": [-1, 10, 16, -1],
        "blue": [-1, -1, 4, -1],
        "yellow": [17, -1, 7, 11],
    }

    render_board(game_positions)
