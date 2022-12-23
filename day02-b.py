from aocd import get_data

input = get_data(day=2, year=2022)

'''
Rock = 1
Paper = 2
Scissors = 3

'''

#        R  P  S
beats = [3, 1, 2]
#           R  P  S
loses_to = [2, 3, 1]

total_score = 0

move_scores = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

def play_round(op_move, outcome):
    if outcome == 'X':
        your_move = beats[move_scores[op_move] - 1] 
        return your_move    
    elif outcome == 'Y':
        return 3 + move_scores[op_move]
    elif outcome == 'Z':
        your_move = loses_to[move_scores[op_move] - 1] 
        return 6 + your_move

for round in input.split('\n'):
    moves = round.split(' ')
    round_score = play_round(moves[0], moves[1])

    total_score += round_score 


print(total_score)