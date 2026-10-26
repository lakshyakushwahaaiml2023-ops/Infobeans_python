# marks = float(input("Enter the marks: "))
# match marks:
#     case m if  m > 80:
#             print("Your grade is A")
#     case m if m >=60:
#             print("Your grade is B") 
#     case m if m >=50:
#               print("Your grade is C")
#     case m if m >= 45:
#                 print("Your grade is D")
#     case m if m >= 25:
#                 print("Your grade is E")
#     case m if m < 25:
#                 print("Your grade is F")

def sec_max(arr):
    maxi = arr[0]
    s_max = float('-inf')
    for i in arr:
        if i > maxi:
            s_max = maxi
            maxi = i
        elif i < maxi and i > s_max:
            s_max = i
    return s_max
arr1 = [1,1,1,1,1,1]
print(sec_max(arr1))
