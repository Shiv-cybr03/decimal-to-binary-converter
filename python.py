def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

def decimal_to_binary(decimal_number):
    binary_number = bin(decimal_number)
    return binary_number

while True:
    user = input("Enter 'exit' to end the program:")
    if user.lower() == 'exit':
        print("Exiting the Program")
        break
    else:
        print("**********************************")
    print("""Chose option:- \n 1. binary_to_decimal \n 2. decimal_to_binary""")
    num = int(input("Choise the option:"))
    if num == 1:
        binary_number = input("Enter a binary number: ")
        try:
            decimal_result = binary_to_decimal(binary_number)
            print(f"The decimal equivalent of {binary_number} is: {decimal_result}")
        except ValueError:
            print("Invalid binary number. Please enter a valid binary number.")
    elif num == 2:
        decimal_number = int(input("Enter a decimal number: "))
        try:
            binary_result = decimal_to_binary(decimal_number)
            print(f"The hexa decimal equivalent of {decimal_number} is: {binary_result}")
        except ValueError:
            print("Invalid decimal. Please enter a valid decimal number.")
    else:
        print("Please enter valid Option:")   
        


