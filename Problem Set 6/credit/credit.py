# Prompt user for input
number = "NULL"
while not(number.isnumeric()):
    number = input("Number: ")
length = len(number)

# If block for length validation
if length < 13 or length > 16:
    print("INVALID")
else:
    # Applying Luhn's Algorithm
    checksum = 0
    for i in range(length-2, -1, -2):
        product = int(number[i]) * 2
        if product > 9:
            checksum += (product % 10) + (product // 10)
        else:
            checksum += product
    for i in range(length-1, -1, -2):
        checksum += int(number[i])
    # If the total sum has remainder 0 when divided by 10, It is valid
    if checksum % 10 == 0:
        if length == 13:
            print("VISA")
        elif length == 15:
            if (number[0] == '3' and (number[1] == '4' or number[1] == '7')):
                print("AMEX")
            else:
                print("INVALID")
        elif (length == 16):
            if number[0] == '4':
                print("VISA")
            elif (number[0] == '5' and (number[1] < '6')):
                print("MASTERCARD")
            else:
                print("INVALID")
    else:
        print("INVALID")