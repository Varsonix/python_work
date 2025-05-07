from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry, the file {path} could not be found.')
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['Chapter 10/Files/alice.txt', 'Chapter 10/Files/siddharta.txt',
             'Chapter 10/Files/moby_dick.txt', 'Chapter 10/Files/little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)