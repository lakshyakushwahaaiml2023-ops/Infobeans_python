def powerTwo(num):
    return not num & num - 1

print(powerTwo(2))
print(powerTwo(3))
print(powerTwo(0))
print(powerTwo(20))