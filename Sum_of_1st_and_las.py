#Defining a function to calculate the sum
def sum_first_last_digit(num):
    #convert the num to str
    num_str = str(num)

    #first digit
    first_digit = int(num_str[0])

    #last digit
    last_digit = int(num_str[-1])

    #return the sum
    return first_digit + last_digit

num = int(input("Enter an interger:"))
result = sum_first_last_digit(num)
print(f"The sum of the first and last digit is: {result}")

