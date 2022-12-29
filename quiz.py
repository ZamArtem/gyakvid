def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
#-----------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#-----------------------------------
def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")

    score = ((correct_guesses/len(questions))*100)
    print(f"Your score is: {score} %")
#-----------------------------------
def play_again():
    
    response = input("Do u want to play again? (yes or no): ")
    response = response.upper
    if response == "YES":
        return True
    else:
        return False  
#-----------------------------------

questions = {
    "1+1?" : "A",
    "2+2?" : "C",
    "3+3?" : "D",
    "4+4?" : "D"
}
options = [["A. 2","B. 3","C. 4","D. 5"],
           ["A. 6","B. 7","C. 4","D. 3"],
           ["A. 8","B. 11","C. 4","D. 6"],
           ["A. 2","B. 3","C. 6","D. 8"]]


new_game()
