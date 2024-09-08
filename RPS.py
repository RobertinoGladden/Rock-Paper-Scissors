# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

# Dictionary to define the winning move
winner = {
    "R": "P",  # Rock is beaten by Paper
    "P": "S",  # Paper is beaten by Scissors
    "S": "R"   # Scissors are beaten by Rock
}

def player(prev_play, opponent_history=[]):
    # Handle the first play case where prev_play is empty
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Maintain a dictionary of opponent's moves
    move_count = {"R": 0, "P": 0, "S": 0}
    
    # Keep track of opponent's history and count their moves
    opponent_history.append(prev_play)
    move_count[prev_play] += 1
    
    # Use a simple Markov chain approach to predict opponent's next move
    if len(opponent_history) >= 3:
        if opponent_history[-1] == opponent_history[-2]:
            prediction = winner[prev_play]
        else:
            most_common_move = max(move_count, key=move_count.get)
            prediction = winner[most_common_move]
    else:
        # Early game random move selection until history builds up
        prediction = random.choice(["R", "P", "S"])
    
    return prediction
