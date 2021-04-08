#Ali Yenidoğan
#2nd Homework

print("****WELCOME****")
print("**REGISTRATION**")


nick = str(input("Please create a username:",))
password = str(input("Please create a password:",))

print("Registration succesful")

a = str(input("Please type your username:",))
b = str(input("Please type your password:",))
if (a == nick and b == password):
    print("Login Succesful")
else:
    print("Your username or password is incorrect")
        
     