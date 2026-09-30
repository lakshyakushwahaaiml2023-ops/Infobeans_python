num = input("Enter a number: ")
ans = num[len(num)-1] + num[1:len(num)-1] + num[0]
print(ans)