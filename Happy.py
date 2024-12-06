# Defining function
def is_happy(num):
    def sum_of_sqaures(n):
        return sum(int(digit)**2 for digit in str(n))
    #unhappy number finding
    repeat = set()
    while num !=1 and num not in repeat:
        repeat.add(num)
        num = sum_of_sqaures(num)
    return num == 1 #reaches 1, happy number
#list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#find happy numbers in list
happy_numbers = [num for num in numbers if is_happy(num)]

#printing happy numbers

print("Happy Numbers:", happy_numbers)
print("Count",len(happy_numbers) )