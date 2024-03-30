import re

def Checker(email : str) :
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.search(pattern, email) :
        return "Valid email address"
    return "Not a valid email address"

print(Checker(input("Please enter your email address : ")))