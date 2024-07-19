# Luhn algorithm practice

# Get user input
user_input = input("Enter a number: ")
input_reversed = []

# Reverse string
for i in user_input[::-1]:
    input_reversed.append(int(i))

# Modify even values
for i in range(len(input_reversed)):
    if i % 2 != 0:
        input_reversed[i] = input_reversed[i] * 2
        if input_reversed[i] > 9:
            input_reversed[i] = input_reversed[i] - 9
            

reversed_sum = sum(input_reversed)
modulo_check = reversed_sum % 10

if(modulo_check):
    print("Please double check your card number.")
else:
    print("Thank you for shopping with us.")
