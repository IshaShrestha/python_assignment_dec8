#Define a global static password value by yourself. Then define a function which prompts user for a password. If the password is a match, print "password match" or else print "Wrong password"

value = 1234

def f(passw):

    if(passw == value):
        print("The passwords match.")
    else:
        print("Wrong password.")

passw = int(input("Enter your password:"))

f(passw)
