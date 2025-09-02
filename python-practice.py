Users = ["Mohammed", "Adin"]
user_name = input("What is your name: ")
if user_name in Users:
    print(f"Hello {user_name}, you can access the file")
else:
    print(f"Greetings {user_name}, however this is not for you")

