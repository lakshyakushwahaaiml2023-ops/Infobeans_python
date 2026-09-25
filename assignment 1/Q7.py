num_classes = int(input("Enter number of classes: "))
num_attended = int(input("Enter number of classes attended: "))
attend_perc = num_attended * 100/num_classes

print(attend_perc,"% Attendance")
if(attend_perc < 75):
    print("Not allowed to sit in the exam")
else:
    print("Allowed to sit in the exam")