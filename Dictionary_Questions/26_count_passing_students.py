result = {
    "lakshya" : 45,
    "diksha" : 34,
    "riya" : 50,
    "ishant" : 20
}
count = 0

for name in result:
    if result[name] < 40:
        print(f"{name} : Fail")
    else:
        print(f"{name} : Pass")
        count += 1
print(f"No. of students passed: {count}")
