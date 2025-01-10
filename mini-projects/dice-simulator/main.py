import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def main():
    while True:
        roll = input("Roll the dice (y/n): ").strip().lower()
        if roll == 'y':
            dice1, dice2 = roll_dice()
            print(f"You rolled a {dice1} and a {dice2}. Total: {dice1 + dice2}")
        elif roll == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
