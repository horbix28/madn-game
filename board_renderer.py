from colorama import just_fix_windows_console, Fore, Style
from sys import platform
if platform == "win32":
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
    for color in ["red", "blue", "yellow", "green"]:
        figs = []
        if figures_on_b_fields.get(color):
            for _ in range(figures_on_b_fields.get(color,0)):
                if color == "red":
                    term_color = Fore.RED
                elif color == "blue":
                    term_color = Fore.BLUE
                elif color == "yellow":
                    term_color = Fore.YELLOW
                elif color == "green":
                    term_color = Fore.GREEN
                # print(color, "appending")
                figs.append(term_color)
        while len(figs) < 4:
                figs.append(Fore.BLACK)
        print(color, figs)
        for fig in figs:
            index = len(fields)
            fields[index] = fig
            # print(index, fig)
    # while len(fields) < 55:
    #     index = len(fields)
    #     fields[index] = Fore.BLACK

    # print(figures_on_b_fields)
    # sorry for this code from hell :=)
    field = Style.BRIGHT +"""
    {48}O{r}{49}O{r}      {28}o{r} {29}o{r} {30}O{r}      {52}O{r}{53}O{r}
    {50}O{r}{51}O{r}      {27}o{r} O {31}o{r}      {54}O{r}{55}O{r}
            {26}o{r} O {32}o{r}
            {25}o{r} O {33}o{r}
    {20}O {21}o{r} {22}o{r} {23}o{r} {24}o{r} O {34}o{r} {35}o{r} {36}o{r} {37}o{r} {38}o{r}
    {19}o{r} O O O O   O O O O {39}o{r}
    {18}o{r} {17}o{r} {16}o{r} {15}o{r} {14}o{r} O {4}o{r} {3}o{r} {2}o{r} {1}o{r} {0}O
            {13}o{r} O {5}o{r}
            {12}o{r} O {6}o{r}
    {44}O{r}{45}O{r}      {11}o{r} O {7}o{r}      {40}O{r}{41}O{r}
    {46}O{r}O{47}      {10}O {9}o{r} {8}o{r}      {42}O{r}{43}O{r}
    """.format(*fields.values(), r=Fore.BLACK) + Fore.RESET
    print(field)


if __name__ == "__main__":
    game_positions = {
        "red": [-1, 10, 16, -1],
        "blue": [-1, -1, 4, -1],
        "yellow": [17, -1, 7, 11],
        "green": [-1,-1,-1,-1]
    }

    render_board(game_positions)
