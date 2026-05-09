# AVOIDING GLOBAL VARIABLES
# It is usually better to pass values into functions and return updated values.

def add_point(current_score):
    current_score = current_score + 1
    return current_score


score = 0

score = add_point(score)
score = add_point(score)
score = add_point(score)

print("Final score:", score)
