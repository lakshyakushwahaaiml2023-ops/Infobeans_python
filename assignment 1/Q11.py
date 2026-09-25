age = int(input("Enter your age: "))
assert (age<20 or age>60), "ERROR!!: Enter a valid age(20-60)"

gen = input("Enter your gender(M or F): ")
mar_stat = input("Marital Status(y or N): ")

if gen == 'F':
    print("Work in urban areas")
if gen == 'M' and age >=40 and age <= 60:
    print("Work in urban areas")
else:
    print("Can work anywhere")