def digits_check(string):
    for i in string:
        if i not in {'0', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9'}:
            return 0
    return 1

string = "1235621"
print(f"{string} only contains digits") if digits_check(string) else print(f"{string} does not only contain digits")