name = "nitin"
rev = ""
for i in range(len(name) - 1, -1, -1):
    rev += name[i]
if rev == name:
    print("Palindrome")
else:
    print("Not Palindrome")