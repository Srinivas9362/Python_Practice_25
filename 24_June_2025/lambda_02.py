# def transform(name):
#     return name.strip().title()

names = [" alice", "BOB ", " charlie"]
cleaned = list(map(lambda x: x.strip().title(), names))
print(cleaned)  # ['Alice', 'Bob', 'Charlie']


name = ' Srinivas '
print(name.strip())
