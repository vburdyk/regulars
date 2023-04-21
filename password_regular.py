import re

password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

password = input("Print your password: ")

if len(password) < 8:
    print("Password is too short, try longer")
elif not re.search(r"[a-z]", password):
    print("Your password need to have at least one symbol in lower register")
elif not re.search(r"[A-Z]", password):
    print("Your password need to have at least one symbol in upper register")
elif not re.search(r"\d", password):
    print("Your password need to have at least one digit")
elif not re.search(r"\W", password):
    print("Your password need to have at least one special symbol")
else:
    print("You have really good password")