def add():
    name=input("Account name: ")
    password=input("Password : ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" + password +"\n")

def view():
     with open("passwords.txt","r") as f:
         for line in f.readlines():
            data=line.rstrip()
            user, password=data.split("|")
            print("User :",user,"Password :",password)



while True:

    user_input=input("Do you want to add or view the passoword? anytime type q to quit :")
    if user_input=="q":
        break

    if user_input =="add":
        add()
    elif user_input=="view":
        view() 