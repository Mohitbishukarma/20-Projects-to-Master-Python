from random import randint

def num_generator(start:int, end:int) -> int:
    number: int = randint(start, end)
    return number

def main():
    while True:
        faces = []
        num_of_dice = input("How many dice do you want roll? ")
        
        if num_of_dice.lower() == "exit":
            print("Thank's for playing!")
            break
        for i in range(int(num_of_dice)):
            dice_face = num_generator(1,6)
            faces.append(dice_face)
        
        print(*faces,sep=", ")

if __name__ == "__main__":
    main()
        