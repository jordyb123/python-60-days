def clean(text):
    return text.strip().lower()

def is_valid_rps_choice(choice):
    return choice in ("1", "2", "3")

MOVE_MAP = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

def map_choice(choice):
    return MOVE_MAP.get(choice)

def line():
    print("-" * 30)

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
