import pickle

class Product:
    def __init__(self, pid, pname, price, brand, desc):
        self.__pid = pid
        self.__pname = pname
        self.__price = price
        self.__brand = brand
        self.__desc = desc

    def __getstate__(self):
        return {
            "product_id" : self.__pid,
            "product_name" : self.__pname,
            "product_price" : self.__price,
            "product_brand" : self.__brand
        }

    def __setstate__(self, state):
        self.__pid = state["product_id"]
        self.__pname = state["product_name"]
        self.__price = state["product_price"]
        self.__brand = state["product_brand"]

    def __str__(self):
        return f"{self.__pid} | {self.__pname} | {self.__price} | {self.__brand}"

def write(pid, pname, price, brand, desc):
    try:
        with open("products.pkl", "a+b") as f:
            p = Product(pid, pname, price, brand, desc)
            pickle.dump(p, f)
            print("Data saved succesfully...")
    except OSError as e:
        print(e)

def read():
    try:
        with open("products.pkl", "rb") as f:
            while True:
                p = pickle.load(f)
                print(p)
    except EOFError as e:
        print("End of file reached...")
    except OSError as e:
        print(e)

# write(1001, "Predator Helios Neo 16", 125000, "Acer", "Unleash the gamer inside you...")
# write(1002, "Macbook Pro 14", 200000, "Apple", "The best laptop for developers...")
# write(1003, "Thinkpad X1 Carbon", 150000, "Lenovo", "The best laptop for business...")
read()



