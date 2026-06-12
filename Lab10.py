users={"Alice": "p123", "Bob": "p124", "Charlie": "p125"}
username=input("Enter your username: ")
password=input("Enter your password: ")
counter=0
if username in users:
    while counter<3:
         if users[username]==password:
            print("Login successful!")
            break
         else:
            print("Incorrect password. Try again.")
            password=input("Enter your password: ")
            counter+=1
    if counter==3:
        print("Too many failed attempts. Account locked.")        
else:
    print("Username not found.")