import pickle

data = {
    "ID" : 1002,
    "Name" : "Diksha",
    "Contact" : 8109927290
}

try:
    with open("data.pkl", "a+b") as f:
        e = pickle.dump(data, f)
        print("Data saved successfully...")
except OSError as e:
    print(e)


