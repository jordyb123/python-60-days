import random

def generate_name(first_names, last_names):
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"

def generate_multiple_names(first_names, last_names, count):
    names = []
    for _ in range(count):
        names.append(generate_name(first_names, last_names))
    return names

def add_name(name_list, name):
    name_list.append(name)