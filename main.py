
from random import randint


def print_welcome_message():
    print("Welcome to hangman game, please tell me you name")
    player_name = input()
    print("Hello " + player_name + " I hope that you'll have fun!")

def get_random_word():
    #print("Get Random Word")
    
    words_file = open("words.txt", "r")
    all_words = words_file.readlines()
    random_index = randint(0, len(all_words)-1)

    random_word = all_words[random_index].rstrip()
    random_word = random_word.lower()
    return random_word


def make_display_string(selected_word):
    #print("Make Display String")
    display_string = []
    for char in selected_word:
        display_string.append("_")
    
    return display_string

def update_display_string(display_string, selected_word, letter):
    #print("Update Display String")

    for i, char in enumerate(selected_word):
        if char == letter:
            display_string[i] = letter

def draw_screen(display_string, number_of_lives):
    print("Lives left: ", number_of_lives)

    pretty_display = ""

    for char in display_string:
        pretty_display += char + " "
    
    print(pretty_display)

def player_guessed(selected_word, letter):

    if letter in selected_word:
        return True
    else:
        return False

def check_win(display_string):
    
    if "_" not in display_string:
        return True
    else:
        return False

def read_letter():
    
    letter = None
    while letter == None:
        print("Please enter a letter")
        letter = input()
        if letter.isalpha() and len(letter) == 1:
            return letter.lower()
        else:
            letter = None
    

def main():
    number_of_lives = 5
    player_won = False
    selected_word = get_random_word()
    display_string = make_display_string(selected_word)

    print_welcome_message()

    while number_of_lives > 0 and not player_won:
        draw_screen(display_string, number_of_lives)
        
        letter = read_letter()

        if player_guessed(selected_word, letter):
            update_display_string(display_string, selected_word, letter)
        else:
            number_of_lives -= 1
        
        if check_win(display_string):
            player_won = True

    if player_won:
        print("Congratulations, you won!")
        print("Word was " + selected_word)

    else:
        print("You lost, better luck next time")
        print("Word was " + selected_word)
    
    exit()

if __name__ == "__main__":
    
    main()