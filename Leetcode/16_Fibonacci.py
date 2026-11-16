dict = {0: 0,
        1: 1}
def fibo(num):
    if num in dict:
        return dict[num]
    
    dict[num] = fibo(num - 1) + fibo(num - 2)
    return dict[num]

print(fibo(3))
print(fibo(5))
print(fibo(8))
print(fibo(10))