import random


def generate_room_code() -> int:
    return random.randint(10000, 99999)
