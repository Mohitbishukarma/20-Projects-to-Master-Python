from random import choice
import sys
class RPS:
    def __init__(self):
        self.moves: dict = { 'rock':'🪨', 'paper':'📜', 'scissors':'✂️'}
        self.valid_moves: list = list(self.moves.keys())
        
        self.user_score = 0
        self.ai_score = 0
        
    def check_game(self, user_input:str, ai:str):
        if user_input == ai:
            print("It's a tie.")
        elif user_input == 'rock' and ai == 'scissors':
            self.user_score += 1
            print("You Win!")
        elif  user_input == 'paper' and ai == 'rock':
            self.user_score += 1
            print("You Win!")
        elif user_input == 'scissors' and ai == 'paper':
            self.user_score += 1
            print("You Win!")
        else:
            self.ai_score += 1
            print("AI Win!")
        
        
    def display_move(self, you, ai):
        print("-----------------------------")
        print(f"| You : {self.moves[you]}   | Your Score : {self.user_score} |")
        print(f"| AI  : {self.moves[ai]}   | AI Score : {self.ai_score}   |")
        print("-----------------------------")
        
    def run_game(self):
        user_input = input("Choose your move rock, paper or scissors? ").lower()
        if user_input == "exit":
            print("\nThanks for playing......")
            sys.exit()
        
        if user_input not in self.valid_moves:
            print("Invalid Move. Choose one of rock, paper and scissors.")
            return self.run_game()
        
            
        ai = choice(self.valid_moves)
        
        self.check_game(user_input, ai)
        self.display_move(user_input, ai)
        
if __name__ == "__main__":
    rps = RPS()
    print("Welcome to RPS by Mohit!")
    while True:
        rps.run_game()