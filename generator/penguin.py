import random

def penguin_name(name, month):
    names = ["frosty", "snow", "igloo", "ice", "fisher" ]
    random_name = random.choice(names)
    d_name = name[0][-1].lower()
    d_month = month[0][-1].upper()
    result = d_month + random_name + d_name
    return (f"Your penguin name is {result}")


