from generator.dragon import dragon_name
from generator.penguin import penguin_name

def get_category():
   
    return category.lower()

def get_name():
     name = input("\nWhat is your first name?\n")
     return name

def get_month():
     month = input("\nWhich month you were born?\n")
     return month
     


def run():
    while True:
            category = input("\nHello, would you like to have a dragon name 🐉 or a penguin name 🐧? Type 'dragon' or 'penguin' (or 'exit').\n").lower()

            if category == "exit":
                print("Sorry to see you go!")
                break
            elif category == "dragon":
                result = dragon_name(get_name(), get_month())
                print(f"\n{result}\n")
            elif category == "penguin":
                result = penguin_name(get_name(), get_month())
                print(f"\n{result}\n")
            else:
                print("\nSorry, there's been an error!\n")


if __name__ == "__main__":
    run() # pragma: no cover
