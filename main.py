import random


def play(m):
    r = int(input(f"Enter row number (1-{len(m)}): ")) - 1
    c = int(input(f"Enter column number (1-{len(m[0])}): "))-1
    return r, c


def solve(m):
    _shot = False
    while not _shot:
        r = random.randint(1, s-1)
        c = random.randint(1, s-1)

        if m[r][c] == "M" or m[r][c] == "X":
            continue
        else:
            _shot = True
    return r, c


def display_map(m):
    for r in m:
        print(r)


def create_map(_size):
    g = list()
    for i in range(_size):
        g.append(list())
        for j in range(_size):
            g[i].append("W")
    return g


def populate_map(m, sl):
    for ship in range(sl):
        can_not_be_placed = True
        direction = random.randint(0, 1)
        if direction == 0:
            while can_not_be_placed:
                r = random.randint(0, len(m)-3)
                c = random.randint(0, len(m)-3)
                if m[r][c] == "0" or m[r][c+1] == "0" or m[r][c+2] == "0":
                    continue
                else:
                    m[r][c] = "0"
                    m[r][c+1] = "0"
                    m[r][c+2] = "0"
                    can_not_be_placed = False
        elif direction == 1:
            while can_not_be_placed:
                r = random.randint(0, len(m) - 3)
                c = random.randint(0, len(m) - 3)
                if m[r][c] == "0" or m[r+1][c] == "0" or m[r+2][c] == "0":
                    continue
                else:
                    m[r][c] = "0"
                    m[r+1][c] = "0"
                    m[r+2][c] = "0"
                    can_not_be_placed = False
    return m


win = False
fail = False
ship_count = 0
size = int(input("How many rows do you want the battle field to be: "))
ship_limit = int(input("How many ships do you want: "))
s = size
grid = create_map(s)
grid = populate_map(grid, ship_limit)

while not win:
    fail = False
    try:
        row, column = play(grid)
    except:
        print(f"Please enter a number between 1 and {s}!")
        fail = True
    if not fail:
        try:
            shot = grid[row][column]
            if shot == "0":
                print("Hit!")
                grid[row][column] = "X"
                if column > 1 and column < len(grid[0])-2 and row > 1 and row < len(grid)-2:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 0 and row > 1 and row < len(grid)-2:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0])-2 and row > 1 and row < len(grid)-2:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == 0:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == len(grid)-2:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row > 1 and row < len(grid)-2:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0])-1 and row > 1 and row < len(grid)-2:
                    if grid[row][column - 1] == "X" and grid[row][column - 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row + 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row - 1][column] == "X" and grid[row - 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column + 1] == "X" and grid[row][column - 1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row - 1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == 1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == len(grid)-1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row - 1][column] == "X" and grid[row - 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column + 1] == "X" and grid[row][column - 1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 0 and row == 0:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0])-1 and row == len(grid)-1:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row == 1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0])-2 and row == len(grid)-2:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 0 and row == 1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row == 0:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 1 and row == len(grid) - 2:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 2 and row == len(grid) - 1:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 1 and row == 0:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 1 and row == 1:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 2 and row == 1:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0]) - 2 and row == 0:
                    if grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 0 and row == len(grid)-1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row == len(grid)-1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row == len(grid)-2:
                    if grid[row][column + 1] == "X" and grid[row][column + 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row - 1][column] == "X" and grid[row - 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column + 1] == "X" and grid[row][column - 1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 0 and row == len(grid)-2:
                    if grid[row][column + 1] == "X" and grid[row][column + 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row - 1][column] == "X" and grid[row - 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == 1 and row > 1 and row < len(grid)-2:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row+2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column == len(grid[0])-2 and row < len(grid)-2:
                    if grid[row][column - 1] == "X" and grid[row][column - 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row + 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row - 1][column] == "X" and grid[row - 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column + 1] == "X" and grid[row][column - 1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row - 1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == 1:
                    if grid[row][column+1] == "X" and grid[row][column+2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column-1] == "X" and grid[row][column-2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row + 2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column + 1] == "X" and grid[row][column - 1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row + 1][column] == "X" and grid[row - 1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                elif column > 1 and column < len(grid[0])-2 and row == len(grid)-2:
                    if grid[row][column + 1] == "X" and grid[row][column + 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column - 1] == "X" and grid[row][column - 2] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row-1][column] == "X" and grid[row-2][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row][column+1] == "X" and grid[row][column-1] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
                    elif grid[row+1][column] == "X" and grid[row-1][column] == "X":
                        print("You sunk a ship!")
                        ship_count += 1
            elif shot == "W":
                print("Miss!")
                grid[row][column] = "M"
            else:
                print("You already shot there!")
        except:
            print(f"Please enter a number between 1 and {s}!")

    if ship_count >= ship_limit:
        win = True

if win:
    print("Congrats! You won Battleship!")
