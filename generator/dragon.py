import random

def dragon_name(name, month):
    names = ["arman", "falkor", "dagahra", "saphira", "darksmoke" ]
    random_name = random.choice(names)
    d_name = name[0][0].upper()
    d_month = month[0][0].lower()
    result = d_name + random_name + d_month
    return (f"Your dragon name is {result}")

