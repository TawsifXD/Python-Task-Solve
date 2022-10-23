# input user full information


 user_info = {" ame": " ", "Age" : "", "Location": " "}


 while True:
    user_info.update({"Name": input( "Enter Your Name: ") } )
     user_info.update({"Age": int(input('Enter Your Age: '))})
    user_info.update({"Location": input("Enter Your Location: ")})

     break

 print(user_info)

# User input sum in list

 user = {}

 key = input("Enter your name: ")
 value = input("Enter your full name: ")

 user[key] = value

 print(user)


# Update information by user


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


# Find the sum of all numbers in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4] 

sum_is = 0 

for i in range(0, len(my_list)):
    sum_is = sum_is + my_list[i]
    print("Your total sum is : ", sum_is)



    
        




    
