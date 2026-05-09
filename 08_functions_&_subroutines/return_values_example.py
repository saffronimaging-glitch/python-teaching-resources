# RETURN VALUES
# A function returns a value back to the main program.

def add_points(current_score, points_to_add):
    new_score = current_score + points_to_add
    return new_score


score = 0

score = add_points(score, 1)

print("Current score:", score)
