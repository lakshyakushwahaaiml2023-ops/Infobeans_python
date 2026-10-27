'''
3. ATM Banking Simulator
Beginner–Intermediate
Concepts: Nested conditions, loops, functions
Requirements
•	Verify a PIN.
•	Display balance, deposit, withdrawal, and exit options.
•	Prevent withdrawals exceeding the available balance.
•	Reject invalid amounts.
•	Use separate functions for deposit, withdrawal, and balance enquiry.
Bonus: Allow only three PIN attempts.
'''


verify = {}
data = {}


def get_name(func):
    def wrap():
        name = input("Enter name: ")
        return func(name)
    return wrap


def set_password(func):
    def wrap(name):
        password = input("Set 4-digit Security PIN: ")

        if len(password) != 4 or not password.isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        verify[name] = password
        data[name] = 1000 

        return func(name)
    return wrap


def balance(name):
    return data[name]


def deposit(name, amnt):
    if amnt <= 0:
        return "Enter a valid positive amount."

    data[name] += amnt
    return f"Deposit successful. Balance: {data[name]}"


def withdraw(name, amnt):
    if amnt <= 0:
        return "Enter a valid positive amount."

    if amnt <= data[name]:
        data[name] -= amnt
        return f"Withdrawal successful. Remaining balance: {data[name]}"

    return f"Insufficient balance. Available: {balance(name)}"


@get_name
@set_password
def ATM(name):
    cnt = 3

    while cnt > 0:
        print("\n1. Balance Enquiry")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice not in {1,2,3,4}:
            print("Enter a valid chice (1 - 4)!!")
            continue

        if choice == 4:
            print("Exited...")
            break

        pw = input("Enter your PIN: ")

        if pw != verify[name]:
            cnt -= 1
            print(f"Incorrect PIN! Attempts remaining: {cnt}")

            if cnt == 0:
                print("Session locked due to 3 incorrect PIN attempts.")
                break

            continue

        cnt = 3

        if choice == 1:
            print("Current Balance:", balance(name))

        elif choice == 2:
            amnt = float(input("Enter amount to deposit: "))
            print(deposit(name, amnt))

        elif choice == 3:
            amnt = float(input("Enter amount to withdraw: "))
            print(withdraw(name, amnt))


ATM()
ATM()
ATM()
print(data)
print(verify)
