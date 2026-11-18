import random
from rich.console import Console
from rich.prompt import Prompt

console=Console()

def roll_die():
    return random.randint(1,6)

def sort_dice(a,b,c):
    if a >= b and a >= c:
        if b >= c :
            return (a,b,c)
        else:
            return (a,c,b)
    elif b >= a and b >= c:
        if a >= c:
            return (b,a,c)
        else:
            return(b,c,a)
    else:
        if a >= b:
            return (c,a,b)
        else:
            return (c,b,a)

def throw_dice():
        a=roll_die()
        b=roll_die()
        c=roll_die()
        return sort_dice(a,b,c)
        

def render_dice(a, b, c):
    values = (a, b, c)
    pips = {
        1: [(1, 1)],
        2: [(0, 0), (2, 2)],
        3: [(0, 0), (1, 1), (2, 2)],
        4: [(0, 0), (0, 2), (2, 0), (2, 2)],
        5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
        6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
    }
    blocks = []
    for value in values:
        grid = [[" "] * 3 for _ in range(3)]
        for r, c in pips[value]:
            grid[r][c] = "●"
        block = ["┌───────┐"]
        for row in grid:
            block.append("│ " + " ".join(row) + " │")
        block.append("└───────┘")
        blocks.append(block)

    # Print all blocks line by line, side by side
    for line_parts in zip(*blocks):
        print("  ".join(line_parts))

a, b, c = throw_dice()   # e.g. (5, 3, 1)
#render_dice(a, b, c)

def are_three_of_a_kind(a,b,c):
    if a == b == c:
        return True
    else:
        return False

def are_421(a,b,c):
    if a == 4 and b == 2 and c == 1:
        return True
    else:
        return False

def are_two_aces(a,b,c):
    if a != 1 and b == 1 and c == 1:
        return True
    else:
        return False

def are_straight(a,b,c):
    if a == b+1 == c+2:
        return True
    else:
        return False

def combination_name(a,b,c):
    if are_421(a,b,c) == True:
        return("four twenty one")
    elif are_three_of_a_kind(a,b,c) == True:
        return("three of a kind")
    elif are_two_aces(a,b,c) == True:
        return("two aces")
    elif are_straight(a,b,c) == True:
        return ("straight")
    else:
        return("nothing")

def combination_value(a,b,c):
    if are_421(a,b,c) == True:
        return(8)
    elif are_three_of_a_kind(a,b,c) == True:
        if a == b == c ==1:
            return(7)
        else:
            return (a+0.8)
    elif are_two_aces(a,b,c) == True:
        return(a+0.9)
    elif are_straight(a,b,c) == True:
        return (2+a/10)
    else:
        return(1+a/10+b/100+c/1000)

def combination_chips(a, b, c):
    return int(combination_value(a,b,c))

def test_combination():
    '''Roll three dice and display the combination's name, value and chips (provided).'''
    a, b, c = throw_dice()
    console.print(f"Dice rolled: {a}, {b}, {c}")
    console.print(f"Combination: {combination_name(a, b, c)}")
    console.print(f"Value:       {combination_value(a, b, c)}")
    console.print(f"Chips:       {combination_chips(a, b, c)}")

def play_turn_phase1():
    a1,b1,c1 = throw_dice()
    print(a1,b1,c1)
    a2,b2,c2 = throw_dice()
    print(a2,b2,c2)
    if combination_chips(a1, b1, c1) > combination_chips(a2, b2, c2):
        return(1,combination_chips(a1, b1, c1))
    elif combination_chips(a1, b1, c1) == combination_chips(a2, b2, c2):
        return(1,0)
    else:
        return(2,combination_chips(a2, b2, c2))

def play_phase1():
    bank = 11 # Bank has 11 chips at the begining of the game and players have none.
    bank1 = 0
    bank2 = 0
    while bank > 0:
        console.clear()
        console.print(f"PHASE 1 - There are {bank} chips in the bank. "
                    f"Player one has {bank1} chips and player two {bank2}."
                      )
        Prompt.ask("Press Enter to continue...")

        winner, chips = play_turn_phase1()
        chips = min(chips, bank) # We dont want to remove more chips than chips remaining in bank
        if winner == 1:
            bank1 += chips
        else:
            bank2 += chips
        bank -= chips
        Prompt.ask("Press Enter to continue...")

    return bank1, bank2 # the number of chips each player has at the end of Phase 1

print(play_phase1())
