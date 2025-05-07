"""Quick Guest Book Testing"""

from pathlib import Path
from random import choice, randint

def guest_book():
    guests = ['Jordan', 'Josh', 'Jeff', 'Jake', 'Jean']
    # Create a huge list of guests off the 5 above.
    guest_list = [choice(guests) for _ in range(1000)]
    guest_book = ''

    for guest in guest_list:
        guest_book += f"{guest}\n"

    path = Path('Chapter 10/Files/Guestbook.txt')
    path.write_text(guest_book)

guest_book()