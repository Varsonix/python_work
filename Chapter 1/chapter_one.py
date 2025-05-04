# Jordan Gibbard - 2025/05/03

first_name = "jordan"
last_name = "gibbard"
full_name  = f"{first_name} {last_name}"
final_message = f"Greetings! Welcome back, {full_name.title()}!"

print(final_message)
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.lstrip().rstrip()

print(favorite_language)

#Various String Ideas and Modulation / Mutables
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

my_name = "Jordan Gibbard"
print(f"Hello {my_name}. What would you like to learn today?")

my_name_upper = my_name.upper()
my_name_lower = my_name.lower()
my_name_title = my_name.title()

print(f"\n{my_name_upper}\n{my_name_lower}\n{my_name_title}")

famous_person = " albert einstein "
famous_quote = '     A person who never made a mistake never tried anything new.'

famous_message = f"{famous_person.rstrip().lstrip().title()} once said, {famous_quote.lstrip()}"

print(famous_message)

file_name = 'python_notes.txt'
file_name_sanitized = file_name.removesuffix('.txt')
print(file_name_sanitized)

def functionMe():
    print('hello'.upper())
    assert True

first_name = 'ada'
last_name = 'lovelace'
FULL_NAME = f'{first_name} {last_name}'
message = f"Hello, {full_name.title()}!"

print(message)

# Testing long strings for PEP8 compliance
message_test = (
    "This is a long string that spans multiple lines, but is neatly "
    "formatted within parentheses."
)
message_test_two = "This is a long string that spans multiples lines, but is " \
                    "Neatly formatted using a backslash."
message_test_three = """This is also a long string that spans multiple lines,
                        but is neatly formatted using triple quotes"""
print(message_test)
print(message_test_two)
print(message_test_three)