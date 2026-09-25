age1 = int(input("Enter the age1: "))
age2 = int(input("Enter the age2: "))
age3 = int(input("Enter the age3: "))
if age1>age2 and age1>age3:
    print(f"Oldest is {age1}")
elif age2>age3 and age2>age1:
    print(f"Oldest is {age2}")
elif age3>age2 and age3>age1:
    print(f"Oldest is {age3}")

if age1<age2 and age1<age3:
    print(f"Youngest is {age1}")
elif age2<age3 and age2<age1:
    print(f"Youngest is {age2}")
elif age3<age2 and age3<age1:
    print(f"Youngest is {age3}")

