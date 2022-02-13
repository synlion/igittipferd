import sys

# DEFINING FUNCTIONS
def get_first_name():
    x = input("Enter your first name or enter 'quit' to end the program:\n")
    return(x) 

def get_last_name():
    y = input("Enter your last name:\n")
    return(y)

def system_exit():
    if first_name == "quit":
        sys.exit("\nThank you for using this service.\n")
    else:
        return(first_name)

def create_email():
    return f"{first_name}.{last_name}@uni-mail.de"


# CREATING AND PRINTING THE EMAIL ADDRESS
emails = []
x = 1

while x == 1:
    first_name  = get_first_name()
    first_name = first_name.lower().strip()
    system_exit() 
    last_name = get_last_name()
    last_name = last_name.lower().replace(" ", "")

    emails.append(create_email())
    print(f"Your university e-Mail address is:\n{emails[-1]}\n")

    # hello github
