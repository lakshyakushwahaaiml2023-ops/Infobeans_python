string1 = "Lakshya"
string2 = "laksHya"

if len(string1) != len(string2):
    print("Not equal")
else:
    for i in range(len(string1)):
        if string1[i].lower() != string2[i].lower():
            print("Not equal")
            break
    else:
        print("Strings are equal")