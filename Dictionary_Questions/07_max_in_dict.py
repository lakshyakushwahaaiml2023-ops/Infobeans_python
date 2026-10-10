marks = {
    "science" : 45,
    "maths": 60,
    "english" : 70
}

max = float('-inf')

for value in marks.values():
    if max < value:
        max = value

print(max)