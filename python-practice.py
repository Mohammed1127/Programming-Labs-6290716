Users = ["Mohammed","Luc"]
user_name = input("What is your name: ")
if user_name in Users:
    print(f"Hello {user_name}, you can access the file")
else:
    print(f"Greetings {user_name}, this is not for you")
if user_name not in Users:
    print("Close the folder immediately like a good little boy")

