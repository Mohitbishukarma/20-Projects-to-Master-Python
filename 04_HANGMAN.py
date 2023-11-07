from random import choice

def run_game(word:str):
    guessed: str = ''
    tries: int = 3
    
    while tries > 0:
        blanks: int = 0
        print("Word :", end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print("_",end="")
                blanks += 1
                
        print("")
           
        if blanks == 0:
            print("You have got it.")
            break
                
        guess: str = input("Enter a Char: ")
        
        if len(guess) > 1:
            print("You can't enter more than one letter.")
            continue
        
        if guess in guessed:
            print(f"Already guessed: {guess}. Try another char..")
            continue
        
        guessed += guess
        if guess not in word:
            tries -= 1
            print(f"Sorry, That was wrong guess... ( {tries} tries remaining)")
            if tries == 0:
                print("No more tries are left. You Lose.....")
        
            
        
        

if __name__ == "__main__":
    word: str = choice(['banana', 'orange', 'kitty','breed','apple'])
    username: str = input("Would you like to share your name? -> ")
    print(f"Welcome to Hangman, {username}!")
    
    run_game(word)