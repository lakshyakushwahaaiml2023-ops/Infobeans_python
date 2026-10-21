start = int(input("Enter start: "))
end = int(input("Enter end: "))
count = 0
for i in range(start, end+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        if i != 1 :
            print(i, end = " ") 
            count += 1
print(f"\nTotal prime numbers: {count}")