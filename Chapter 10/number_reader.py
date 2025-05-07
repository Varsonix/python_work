from pathlib import Path
import json

path = Path('Chapter 10/Files/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)