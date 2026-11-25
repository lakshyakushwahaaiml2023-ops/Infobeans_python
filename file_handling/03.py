f = None
try:
    f = open("f1.txt", "w+")

except FileNotFoundError as e:
    print("File not found...")


else:
    print("File Exists...")
    f.writelines((str(i) + "\n" for i in range(10)))
    f.seek(0)
    print(f.read())

finally:
    try:
        f.close()
    except AttributeError as e:
        print("File is None Object ")