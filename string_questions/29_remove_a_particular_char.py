def remove_char(string, target):
    ans = ""
    for i in string:
        if i != target:
            ans += i
    return ans

string = "Lakshya"
target = "a"
print(f"After removing \'{target}\' from \'{string}\': {remove_char(string, target)}")