# STRETCH CHALLENGE - MULTIPLAYER QUIZ

player1_score = 0
player2_score = 0


def ask_question(question, answer):

    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1

    else:
        print("Incorrect!")
        return 0


print("PLAYER 1 TURN")
player1_score += ask_question("What is 2 + 2?", "4")
player1_score += ask_question("Capital of France?", "Paris")


print("\nPLAYER 2 TURN")
player2_score += ask_question("What colour is grass?", "green")
player2_score += ask_question("What keyword creates a loop?", "for")


print("\nFINAL SCORES")
print("Player 1:", player1_score)
print("Player 2:", player2_score)


if player1_score > player2_score:
    print("Player 1 wins!")

elif player2_score > player1_score:
    print("Player 2 wins!")

else:
    print("It's a draw!")
