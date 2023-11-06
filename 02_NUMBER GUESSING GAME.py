from random import randint
def num_generator(start:int, end:int) -> int:
    number: int = randint(start, end)
    return number

random_number: int = num_generator(1,10)

score = 5

print("Guess a number between 1 to 10.")

while True:
    if score <= 0: 
        print("Sorry, No moves available. Try Again..")
        break
    try:
        guess:int = int(input("Guss: "))
    except ValueError: 
        print("Invalid value")
        score -= 1
        continue

    if guess> random_number: 
        print("Number is lower.")
        score -= 1
        continue
    elif guess < random_number: 
        print("Number is higher.")
        score -= 1
        continue
    else: 
        print(f"Yes, You guessed it right.\nSCORE : {score}") 
        break
    
    
    
    