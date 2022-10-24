  -------------------------------------------------------------------------- Day 1 -------------------------------------------------------------------------------  



# Adding input from the user to the dictionary


 user_info = {" ame": " ", "Age" : "", "Location": " "}


 while True:
    user_info.update({"Name": input( "Enter Your Name: ") } )
     user_info.update({"Age": int(input('Enter Your Age: '))})
    user_info.update({"Location": input("Enter Your Location: ")})

     break

 print(user_info)
 
# Adding input from the user to the dictionary

 user = {}

 key = input("Enter your name: ")
 value = input("Enter your full name: ")

 user[key] = value

 print(user)

# Adding input from the user to the dictionary

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

          
  -------------------------------------------------------------------------- Day 2 -------------------------------------------------------------------------------    
          

# Find the sum of all numbers in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4] 

sum_is = 0 

for i in range(0, len(my_list)):
    sum_is = sum_is + my_list[i]
    print("Your total sum is : ", sum_is)
   
   
# Find the even numbers in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

for i in my_list:
    if i % 2 == 0:
        print("Even number: ", i)


# Fine the odd numbers in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

for i in my_list:
    if i % 2 != 0:
        print("Odd number: ", i)


# Count the number of even numbers in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

even = 0

for i in my_list:
    if i % 2 == 0:
        even +=1
print("Even count: " ,even)

# Print all the states in the list

state = ['Alabama', 'Virginia', 'Maryland']

for i in state:
    print("State name: ", i)
  
# loop through a list of mixed data type and extract only integer values

my_list = [1, 2, 'apple', 3, 4, 'orange']

for i in my_list:
    if isinstance(i,int):
        print("Output is :",i)


# Print all the keys

my_dict = {"apple": 2.50, "orange": 4.99, "banana": 0.59}

print(my_dict.keys())


# Print all the keys and values
my_dict = {"apple": 2.50, "orange": 4.99, "banana": 0.59}

print(my_dict)





    
        




    
