dict = {1: 1,
        2: 1}

def fibo(num):
    if num in dict:
        return dict[num]
    
    dict[num] = fibo(num -1) + fibo(num - 2)
    return dict[num]

print(fibo(35))
