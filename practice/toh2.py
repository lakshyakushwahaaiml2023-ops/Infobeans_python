def toh(nums, source, aux, dest):
    if nums == 0:
        return
    toh(nums-1, source, dest, aux)
    print(f"{source} --> {dest}")
    toh(nums - 1, aux, source, dest)

toh(3, "A", "B" , "C")