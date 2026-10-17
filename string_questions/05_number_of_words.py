string = "My name is Lakshya"
w_count = 1
for i in string:
    word = ""
    if i == " ":
        w_count += 1
print(f"Word count : {w_count}")