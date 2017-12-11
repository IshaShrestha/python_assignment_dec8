#Define a function to determine whether the user's integer input is a even number or an odd number.

def fun(num):

    if (num%2 == 0):
        print("The given number is even.")
    else:
        print("The given number is odd.")

num = int(input("Enter a number:"))

fun(num)