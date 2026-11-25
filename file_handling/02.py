f = open("abc.txt", "w")
print(f.tell())
f.write("Hello, World...")
print(f.tell())
