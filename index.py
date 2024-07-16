from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter your password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            acc, pwd = data.rsplit(" || ")
            print("Account Name: " + acc + "  Password: " + pwd)


def add():
    acc_name = input("Enter Account Name: ")
    pwd = input("Enter Password: ")
    with open("passwords.txt", "a") as f:
        f.write(acc_name + " || " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Select mode (view/add) or enter 'q' to terminate the process: "
    ).lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
