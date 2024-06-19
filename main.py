"""
The following code is mainly generated by ChatGPT-4o - it can contain logic and coding errors. So far it's not well tested.
"""
import random
from colorama import Fore, just_fix_windows_console
import logging, sys

just_fix_windows_console()
from time import sleep
from board_renderer import render_board


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


START_POSITIONS = {"red": 0, "blue": 10, "yellow": 20, "green": 30}
END_POSITIONS = {
            "red": 39,
            "blue": 9,
            "yellow": 19,
            "green": 29,
        }


class Color:
    def __init__(self, name, rgb, term_color):
        self.name = name
        self.rgb = rgb
        self.start_position = START_POSITIONS.get(name)
        self.end_position = END_POSITIONS.get(name)
        self.term_color = term_color
class MenschAergereDichNicht:
    def __init__(self, players):
        # Check if player count is between 2 and 4.
        if len(players) < 2 or len(players) > 4:
            raise ValueError("Player count needs to be between 2 and 4.")
        self.game_over = False
        self.players = players
        self.start_positions = {player: player.start_position for player in players}
        self.end_positions = {player: player.end_position for player in players}
        self.positions = {player: [-1, -1, -1, -1] for player in players}
        self.starting_color = random.choice(players)

    def calc_newpos(self, color, piece_index, steps):
        logging.debug("Calculating newpos for color: %s figure: %s steps %s", color, piece_index, steps)
        current_pos = self.positions[color][piece_index]

        # Check if figure is on b field
        if current_pos == -1:
            if steps == 6:
                calculated_pos = self.start_positions[color]
            else:
                calculated_pos = None
        else:
            calculated_pos = (current_pos + steps) % 39
        logging.debug("calculated newpos: %s", calculated_pos)
        logging.debug("checking if newpos '%s' is in list of own figures: %s", calculated_pos, self.positions[color])
        if calculated_pos in self.positions[color]:
            logging.debug("own figure is blocking")
            return None
        # return new position
        return calculated_pos
    def move_piece(self, color, piece_index, steps):
        if color not in self.players:
            raise ValueError(f"{color} is not playing.")
        new_pos = self.calc_newpos(color, piece_index, steps)

        # Wenn die neue Position im Endbereich liegt
        if new_pos == self.end_positions[color]:
            if all(p != new_pos for p in self.positions[color]):
                self.positions[color][piece_index] = new_pos
            else:
                print(
                    f"{color.capitalize()} piece {piece_index} cannot move to end position {new_pos}."
                )
        else:
            self.positions[color][piece_index] = new_pos
        # Check if other figure gets kicked out
        for opponent_name, pieces in self.positions.items():
            if opponent_name != color:
                for i, pos in enumerate(pieces):
                    if pos == new_pos:
                        self.positions[opponent_name][i] = -1
                        print(
                            f"{color.capitalize()} piece {piece_index} knocked out {opponent_name.capitalize()} piece {i}!"
                        )

    def display_board(self):
        # Darstellung der Positionen der Spielfiguren
        logging.debug("Current board positions:")
        for color_name, positions in self.positions.items():
            logging.debug(f"{color_name.capitalize()}: {positions}")

    def display_color_pieces(self, color):
        out = ""
        for piece_index, piece_pos in enumerate(self.positions[color]):
            out += f"{piece_index}: {piece_pos}, "
        return out

    def calc_dice_roll_effect(self, color, dice_roll):
        moveable_figures = {}
        immovable_figures = []

        for piece_index, _ in enumerate(self.positions[color]):
            future_pos = self.calc_newpos(color, piece_index, dice_roll)
            if future_pos is not None:
                moveable_figures[piece_index] = future_pos
            else:
                immovable_figures.append(piece_index)
        return moveable_figures, immovable_figures

    def roll_dice(self):
        return random.randint(1, 6)

    def game_loop(self):
        current_player = random.randint(0, len(self.players) - 1)
        while not self.game_over:
            player = self.players[current_player]
            print(player.name + "s", "player turn.")
            # self.display_board()
            # print("\nYour figures now: ", self.display_color_pieces(player))
            # roll = self.roll_dice()
            roll = int(input("Würfel: "))
            print(f"Rolled: {roll}:")
            movable_figures, _ = self.calc_dice_roll_effect(
                player, roll
            )
            if movable_figures:
                print(
                    "Movable figures now: ",
                    " ".join(
                        [
                            f"Figure {i} -> {movable_figures[i]} | "
                            for i in movable_figures
                        ]
                    ),
                    "\nwhich one do u like to move?",
                )
                move_fig = None
                while not move_fig in movable_figures:
                    move_fig = int(input("Move Figure: (nr): "))
                print("Moving figure", move_fig)
                self.move_piece(player, move_fig, roll)
                print("Your figures now: ", self.display_color_pieces(player))

            else:
                print("No movable figure")
            print("\n\n\n\n\n\n")
            render_board(self.positions)
            sleep(0.5)
            if current_player < len(self.players) - 1:
                current_player += 1
            else:
                current_player = 0



"""
OO      o o O      OO
OO      o O o      OO
        o O o
        o O o
O o o o o O o o o o o
o O O O O   O O O O o
o o o o o O o o o o O
        o O o
        o O o
OO      o O o      OO
OO      O o o      OO
"""

if __name__ == "__main__":
    players = [Color("red",(255,0,0), Fore.RED), Color("blue", (0,0,255), Fore.BLUE), Color("yellow", (255,255,0), Fore.YELLOW), Color("green", (0,255,0), Fore.GREEN)]  # Zwei Spieler: red und blue
    game = MenschAergereDichNicht(players)
    game.game_loop()


# game.display_board()
# game.move_piece('red', 0, 6)  # rede Figur 0 startet
# game.display_board()
# game.move_piece('blue', 0, 6)  # bluee Figur 0 startet
# game.display_board()
# game.move_piece('red', 0, 4)  # rede Figur 0 bewegt sich 4 Schritte
# game.display_board()
