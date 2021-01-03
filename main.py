# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020


class Cell:
    def __init__(self, identity):
        self.id = int(identity)
        self.val = str(identity)
        self.claimed = False

    def set_value(self, value):
        if not self.claimed:
            self.val = str(value)
            self.claimed = True
            return True
        return False

    def is_claimed(self):
        return self.claimed

    def get_id(self):
        return self.id

    def get_value(self):
        return self.val


def cell_is_claimed(cell):
    for x in range(grid_size):
        for y in range(grid_size):
            if this_game[x][y].is_claimed() and this_game[x][y].get_id() == int(cell):
                return True
    return False


def check_for_winner():
    # select diagonals
    nwse = []
    swne = []
    for i in range(grid_size):
        nwse.append(this_game[i][i])
        swne.append(this_game[abs(i - grid_size + 1)][i])
    win_sets = [nwse, swne]

    # select each row and column
    for x in range(grid_size):
        horizontal = this_game[x]
        vertical = []
        for y in range(grid_size):
            vertical.append(this_game[y][x])
        win_sets.append(vertical)
        win_sets.append(horizontal)

    # interrogate sets until a winner is found
    for this_set in win_sets:
        tally_x, tally_o = 0, 0
        for member in this_set:
            # print(member.get_value(), end=", ")  # DEBUG: print the winning sets
            this_value = member.get_value()
            if this_value == "X":
                tally_x += 1
            elif this_value == "O":
                tally_o += 1
        # print()  # DEBUG: newline between sets
        if tally_x == grid_size:
            return "X"
        if tally_o == grid_size:
            return "O"
    return None


def claim_cell(cell, player):
    for x in range(grid_size):
        for y in range(grid_size):
            if not this_game[x][y].is_claimed() and this_game[x][y].get_id() == int(cell):
                this_game[x][y].set_value(player)
                return True
    return False


def display(game):
    for x in range(grid_size):
        print("\t", end="")
        for y in range(grid_size):
            print(game[x][y].val, end=" ")
            if y != grid_size - 1:
                print(" | ", end=" ")
        if x != grid_size - 1:
            print()
            print("\t", end="")
            if grid_size <= 4:
                print("-" * (5 * grid_size))
            elif grid_size <= 7:
                print("-" * (6 * grid_size))
            else:
                print("-" * (7 * grid_size))
    print()


def get_play():
    display(this_game)
    while True:
        this_play = input("make a play: ")
        if this_play.isdigit():
            cell = int(this_play)
            if 0 < cell < grid_size * grid_size + 1:
                if not cell_is_claimed(cell):
                    return cell
        print(this_play + " is not a valid play. Please, ", end="")


def get_player():
    if get_turn() % 2 == 0:
        player = "O"
    else:
        player = "X"
    return player


def get_turn():
    turn = 1
    for x in range(grid_size):
        for y in range(grid_size):
            if this_game[x][y].is_claimed():
                turn += 1
    print("Turn number: " + str(turn))
    return turn


def init_game(size):
    grid = []
    cell = 1
    for x in range(1, size + 1):
        row = []
        for y in range(1, size + 1):
            row.append(Cell(cell))
            cell += 1
        grid.append(row)
    row = []
    for cell in range(1, size * size + 1):
        row.append(Cell(cell))
    grid.append(row)
    return grid


def play_one_player():
    print("one player: Work in progress...")


def play_two_player():
    while not stalemate():
        player = get_player()
        if claim_cell(get_play(), player):
            winner = check_for_winner()
        if winner is not None:
            print("Game over, " + winner + " won the game.")
            display(this_game)
            break
    if stalemate():
        print("Game over: stalemate")


def stalemate():
    for x in range(grid_size):
        for y in range(grid_size):
            if not this_game[x][y].is_claimed():
                return False
    return True


if __name__ == '__main__':
    grid_size = 3  # Ostensibly, allow for games on grids of any size
    while True:
        this_game = init_game(grid_size)
        print()
        intention = input("Would you like to play a two-player game of Tic-Tac-Toe? [<2>, 1, y(es), n(o)] ")
        if intention == "" or intention[0].lower() == "y" or intention[0] == "2":
            play_two_player()
        elif intention[0].lower() == "n" or intention[0] == "1":
            play_one_player()
