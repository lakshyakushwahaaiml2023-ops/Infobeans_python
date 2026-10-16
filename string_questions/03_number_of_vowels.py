name = "My name is Lakshya"
v_count = 0
c_count = 0
for i in name:
    if i in {'a', 'e', 'i', 'o', 'u'}:
        v_count += 1
    elif i.isalnum():
        c_count += 1
print(f"Vowels count: {v_count}")
print(f"Consonant count: {c_count}")