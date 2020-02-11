user_input = input("Enter a number to check if prime ")

val = int(user_input)

if val > 1:
    for i in range(2, val):
        if (val % i) == 0:
            print(val, 'is not a prime number')
            break
        else:
            print(val, 'is a prime number')
            break
else:
    print('Please enter a number')
