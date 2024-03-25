#Step 1
import random
import hangman_words
import hangman_art







end_of_game = False

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
stage_level = len(hangman_art.stages) - 1





guess_word = []

for letter in chosen_word:
    guess_word.append("_")

print(hangman_art.logo)




print("Start game")


print(guess_word)
while end_of_game != True:
    letter = input("Enter a letter: ").lower()
    number_of_floor = guess_word.count("_")
    for position in range(len(chosen_word)):
        if letter == chosen_word[position]:
            guess_word[position] = letter

    if number_of_floor == guess_word.count("_"):
        stage_level -= 1
        print("You writed wrong letter !!!")

    print(hangman_art.stages[stage_level])
    if stage_level == 0:
        print(f"correct answear was {chosen_word}")
        end_of_game = True
        print("You loose!")



    if "_" not in guess_word:
        print(chosen_word)
        end_of_game = True
        print("You win!")


    print(guess_word)















