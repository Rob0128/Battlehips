import random


def is_sunk(ship):
#finds length of the input ship and compares the int value to the number of hits on the ship
    ship_len = ship[3]
    count = 0
    boat = ship[4]
    for hit in boat:
        count += 1


    if ship_len == count:
        return True
    else:
        return False

def ship_type(ship):
    #returns ship type depending on length(int) of input ship
    type_ship = ""
    if ship[3] == 1:
        type_ship = "submarine"
    elif ship[3] == 2:
        type_ship = "destroyer"
    elif ship[3] == 3:
        type_ship = "cruiser"
    elif ship[3] == 4:
        type_ship = "battleship"
    return type_ship

def is_open_sea(row, column, fleet):
    #creates a list of squares that are part of a ship in fleet or next to a ship in fleet
    spot = (row, column)
    no_go = []
    for ship in fleet:
        bottoml = ship[0] - 1
        bottomr = ship[1] - 1
        bottom = (bottoml, bottomr)
        horizontal = ship[2]

        if horizontal == True:
            #iterates through current ships in fleet and adds all squares that are adjacent to some ship to list 'no_go'
            for j in range(0, (ship[3] + 2)):
                new_botr = bottomr + j
                for i in range(0, 3):
                    new_botl = bottoml + i
                    new_tup = (new_botl, new_botr)
                    no_go.append(new_tup)
        else:
            for j in range(0, 3):
                new_botr = bottomr + j
                for i in range((ship[3] + 2)):
                    new_botl = bottoml + i
                    new_tup = (new_botl, new_botr)
                    no_go.append(new_tup)

    if spot in no_go:

        return False
    else:
        return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    #checks if row, column is an occupied square or is next to an occupied square
    ship = []
    if horizontal == True:
        for i in range(0, length):
            new_spot = (row, column + i)
            if new_spot[0] > 9 or new_spot[1] > 9:
                return False
            else:
                ship.append((row, column + i))
    else:
        for i in range(0, length):
            new_spot = (row + i, column)
            if new_spot[0] > 9 or new_spot[1] > 9:
                return False
            else:
                ship.append((row + i, column))
    count = 0
    for part in ship:
        x = part[0]
        y = part[1]
        ok = is_open_sea(x, y, fleet)
        if ok == True:
            count += 1
        else:
            count = count

    if count == length:
        return True
    else:
        return False


def place_ship_at(row, column, horizontal, length, fleet):
#returns a new fleet with a new ship added after it is checked by the 'ok_to_place_ship_at' function
    if ok_to_place_ship_at(row, column, horizontal, length, fleet):
        new_fleet = fleet
        ship = []
        if horizontal == True:
            for i in range(0, length):
                ship.append((row, column + i))

        else:
            for i in range(0, length):
                ship.append((row + i, column))

        x = row
        y = column
        l = len(ship)
        hits = set()

        ship_formatted = (x, y, horizontal, l, hits)
        new_fleet.append(ship_formatted)

        return new_fleet

    else:
        return fleet


def randomly_place_all_ships():

#iterates through all 4 ship types and places the required amount of each using the 'ok_to_place_ship_at' funcation

    list = []
    for x in range(0, 10):
        for y in range(0, 10):
            list.append((x, y))

    fleet = []

    for battleship in range(0, 1):
        done = False
        while done == False:
            z = random.choice(list)
            k = z[0]
            s = z[1]
            r = random.randint(0, 1)
            hor = True
            if r == 0:
                hor = False
            else:
                hor = True

            test_new = ok_to_place_ship_at(k, s, hor, 4, fleet)
            new_fleet = fleet

            if test_new == True:
                new_fleet = place_ship_at(k, s, hor, 4, fleet)
                fleet = new_fleet
                done = True

    for cruiser in range(0, 2):
        done = False
        while done == False:
            z = random.choice(list)
            k = z[0]
            s = z[1]
            r = random.randint(0, 1)
            hor = True
            if r == 0:
                hor = False
            else:
                hor = True

            test_new = ok_to_place_ship_at(k, s, hor, 3, fleet)


            if test_new == True:
                fleet = place_ship_at(k, s, hor, 3, fleet)
                done = True


    for destroyer in range(0, 3):
        done = False
        while done == False:
            z = random.choice(list)
            k = z[0]
            s = z[1]
            r = random.randint(0, 1)
            hor = True
            if r == 0:
                hor = False
            else:
                hor = True

            test_new = ok_to_place_ship_at(k, s, hor, 2, fleet)

            if test_new == True:
                fleet = place_ship_at(k, s, hor, 2, fleet)
                done = True



    for sub in range(0, 4):
        done = False
        while done == False:
            z = random.choice(list)
            k = z[0]
            s = z[1]
            r = random.randint(0, 1)
            hor = True
            if r == 0:
                hor = False
            else:
                hor = True

            test_new = ok_to_place_ship_at(k, s, hor, 1, fleet)

            if test_new == True:
                fleet = place_ship_at(k, s, hor, 1, fleet)
                done = True


    return fleet



def check_if_hits(row, column, fleet):
    #first checks if this shot is already registered as a hit
    for ship in fleet:
        for hit in ship[4]:
            if ((row, column)) == hit:
                return False
    #then finds all ship occupied squares and returns them in a list
    else:
        fleet_tups = []
        for ship in fleet:
            ship_across = ship[1]
            ship_down = ship[0]
            ship_start = (ship_down, ship_across)
            ship_hor = ship[2]
            ship_len = ship[3]
            if ship_hor == True:
                for ship_part in range(0, ship_len):
                    new_across = ship_across + ship_part
                    full_ship = (ship_down, new_across)
                    fleet_tups.append(full_ship)
            else:
                for ship_part in range(0, ship_len):
                    new_down = ship_down + ship_part
                    full_ship = (new_down, ship_across)
                    fleet_tups.append(full_ship)


        #searches the 'fleet_tups' list of shi occupied squeares to see if the shot is a hit
        tup = (row, column)
        if tup in fleet_tups:
            return True
        else:
            return False


def hit(row, column, fleet):
    #adds a hit to the hit ship and returns that updated ship to the fleet and removes the old version of the ship
    fleet1 = fleet
    hit_ship = ()
    for ship in fleet:
        if ship[2] == True:

            for i in range(0, ship[3]):
                h = (ship[0], ship[1] + i)
                if ((row, column)) == h:
                    hit_ship = ship
                    fleet1.remove(ship)

        else:

            for j in range(0, ship[3]):
                h = (ship[0] + j, ship[1])
                if ((row, column)) == h:
                    hit_ship = ship
                    fleet1.remove(ship)


    hit_ship[4].add((row, column))
    fleet1.append(hit_ship)
    return(fleet1, hit_ship)


def are_unsunk_ships_left(fleet):
#iterates through every shi in fleet an returns true if hits is equal to total squares occupied by a full fleet
    hit_tot = 0
    for ship in fleet:
        for hit in ship[4]:
            hit_tot += 1

    if hit_tot == 20:
        return False
    else:
        return True


board = []
#creates the board that will be printed via 'print_board' function when 'main' runs
board.append(' ' ' ' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9')
board.append(' ' ' ' + '-' * 10)
for x in range(0, 10):

    board.append(([str(x)] + ['|'] + ['.'] * 10))

def print_board(board):
    for row in board:
        print (" ".join(row))


def main():
    #initiates the game and prints the board visualisation
    current_fleet = randomly_place_all_ships()
    ship_hit = ()
    print(current_fleet)
    print_board(board)

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()
        #below tests if the input was correct (exactly two numbers bet as input)
        checked = False
        check_len = False
        check_num = False
        while checked == False:
            if len(loc_str) == 2:
                check_len = True
            else:
                check_len = False
            if check_len == True:
                check_first = loc_str[0].isnumeric()
                check_second = loc_str[1].isnumeric()
                if check_first == True and check_second == True and int(loc_str[0]) >= 0 and int(
                        loc_str[0]) < 10 and int(loc_str[1]) >= 0 and int(loc_str[1]) < 10:
                    check_num = True
            if check_len == True and check_num == True:
                checked = True
            else:
                print("Incorrect input, please input 2 numbers seperated by a space")
                loc_str = input("Enter row and colum to shoot (separted by space): ").split()

        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1


        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            board[current_row + 2][current_column+2] = 'H'
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")

                for x in ship_hit[4]:
                    board[x[0]+2][x[1]+2] = 'S'

        else:
            print("You missed!")
            board[current_row + 2][current_column + 2] = 'x'

        if not are_unsunk_ships_left(current_fleet): game_over = True

        print_board(board)


    print("Game over! You required", shots, "shots.")


if __name__ == '__main__':
   main()
