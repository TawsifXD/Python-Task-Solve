# user_info = {" ame": " ", "Age" : "", "Location": " "}


# while True:
#     user_info.update({"Name": input( "Enter Your Name: ") } )
#     user_info.update({"Age": int(input('Enter Your Age: '))})
#     user_info.update({"Location": input("Enter Your Location: ")})

#     break

# print(user_info)

# user = {}

# key = input("Enter your name: ")
# value = input("Enter your full name: ")

# user[key] = value

# print(user)






from sre_parse import State


while True:
        user = {}
        key = input('username: ')
        value = []
        value.append(input("Enter your full name: "))
        value.append(input("Enter your age: "))
        value.append(input("Enter your location: "))
        user[key] = value
        print(user)


        State = input("if you want to quit type yes or type anything to continue")

        if State == 'yes':
            break




    
        




    
