from pathlib import Path

path = Path('Chapter 10/Files/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy ")
if birthday in pi_string:
    print("Your birthday appers in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")