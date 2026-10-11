marks = {
    "Lakshya": 100,
    "Riya" : 45,
    "Diksha" : 60,
    "Ishant": 50
}

items = list(marks.items())

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

items = dict(items)
print(items)