from aocd import get_data

input = get_data(day=2, year=2022)

total_score = 0

move_options = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

def play_round(op_move, your_move):
    if op_move == 'A':
        if your_move == 'X':
            return 3
        elif your_move == 'Y':
            return 6
       
    elif op_move == 'B':
        if your_move == 'Y':
            return 3
        elif your_move == 'Z':
            return 6
       
    else:
        if your_move == 'Z':
            return 3
        elif your_move == 'X':
            return 6
    
    return 0

for round in input.split('\n'):
    moves = round.split(' ')
    round_score = play_round(moves[0], moves[1])
    total_score += move_options[moves[1]] + round_score 


print(total_score)