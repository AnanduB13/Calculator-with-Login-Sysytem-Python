from datetime import datetime
import hashlib
import time

def calculator():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        else:
            return x / y
    
    while True:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        time.sleep(1.5)
        choice = input("Enter choice(1/2/3/4/5):")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Exiting the Calculator")
            pass

def register():
    print("\nRegister your ID")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    encoded_password = hashlib.sha256(password.encode()).hexdigest()
    encoded_username = hashlib.sha256(username.encode()).hexdigest()

    with open("Login.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(',')
            if encoded_username == stored_username or encoded_password == stored_password:
                print("Username already exists. Please try again.\n")
                time.sleep(2)
                choice = input("""Press 1 to register new ID\nPress 2 to login again""")
                if choice == "1":
                    register()
                if choice == "2":
                    login()
                return

        with open("Login.txt", "a") as f1:
            f1.write(encoded_username + "," + encoded_password + "\n")
            print("New User has been Registered")

        choice = input("""Press 1 to register new ID\nPress 2 to login again""")
        if choice == "1":
            register()
        if choice == "2":
            login()  

def login():
    print("\Login with your ID")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    encoded_password = hashlib.sha256(password.encode()).hexdigest()
    encoded_username = hashlib.sha256(username.encode()).hexdigest()
    with open("Login.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                stored_username, stored_password = line.strip().split(',')
                if encoded_username == stored_username and encoded_password == stored_password:
                    current_time = datetime.now()
                    f=open("logg.txt","a")
                    f.write("\nUser "+ username +" logged in at: "+ str(current_time))
                    f.close()
                    print("Login successful!")
                    calculator()
                    break
            else:
                print("Invalid username or password. Please try again.\n")
                current_time = datetime.now()
                f=open("logg.txt","a")
                f.write("\n\nUser tried to login with username: "+ username +", at: "+ str(current_time)+"\n")
                f.close()
                time.sleep(2)
            choice = input("""Press 1 to register new ID\nPress 2 to login again""")
            if choice == "1":
                register()
            if choice == "2":
                login()

#main function
print("Login or Register")
choice = input("Enter your choice 1 or 2:")

if choice == "1":
        login()
if choice == "2":
        register()
