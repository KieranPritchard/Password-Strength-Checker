import string

def header():
    #Prints the header of the program
    print('-' * 30)
    print("Password Strength Checker")
    print('-' * 30)

def password_check(users_password):

    #Flags for different keys
    lower_case_flag = string.ascii_lowercase
    upper_case_flag = string.ascii_uppercase
    number_flag = string.digits
    symbol_flag = string.punctuation
    
    number_of_flags_checked = []

    #Checks x fits the info in the flags
    for x in users_password:
        if x in lower_case_flag:
            number_of_flags_checked.append(1)
        elif x in upper_case_flag:
            number_of_flags_checked.append(2)
        elif x in number_flag:
            number_of_flags_checked.append(3)
        elif x in symbol_flag:
            number_of_flags_checked.append(4)
        
    #Checks the length of the password
    if len(users_password) >= 8:
        number_of_flags_checked.append(5)

    #Removes duplicates
    number_of_flags_checked = list(dict.fromkeys(number_of_flags_checked))
    
    #Checks the flags that where added to determine length
    if len(number_of_flags_checked) == 1:
        print("Password Strength Is: " + "Very Weak")
    elif len(number_of_flags_checked) == 2:
        print("Password Strength Is: " + "Weak")
    elif len(number_of_flags_checked) == 3:
        print("Password Strength Is: " + "Moderate")
    elif len(number_of_flags_checked) == 4:
        print("Password Strength Is: " + "Strong")
    elif len(number_of_flags_checked) == 5:
        print("Password Strength Is: " + "Very Strong")

def main():
    header()
    password_check(users_password = input("Please Input your password: "))

if __name__ == "__main__":
    main()