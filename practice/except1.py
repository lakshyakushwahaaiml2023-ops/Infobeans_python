try:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = a/b
        print(c)
    except ValueError as e:
        print("ValueError | Inner Except...")
    finally:
        print("Inner Finally...")

except ZeroDivisionError as e:
    print("Zero Division Error | Outer Except")

finally:
    print("Outer Finally")
