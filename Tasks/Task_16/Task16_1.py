import re
text = input()
print(re.sub(r'\w+\s?', lambda x: x.group()[0].title(), text))