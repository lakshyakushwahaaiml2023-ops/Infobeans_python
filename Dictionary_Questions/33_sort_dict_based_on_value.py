d1 = {
  "a" : 30,
  "b" : 10,
  "c" : 40,
  "d" : 0,
  "e" : 20
}
 
items = list(d1.items())
for i in range(len(items)):
  for j in range(len(items) - i - 1):
    if items[j][1] > items[j+1][1]:
      items[j], items[j+1] = items[j+1], items[j]
res = dict(items)
print(f"Original Dictionary: {d1}")
print(f"Sorted Dictionary: {res}")