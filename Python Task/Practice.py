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

------------------------------------------------------------------------------------ Day 3 ----------------------------------------------------------------





# 1 Write a Python function to find the Max of three numbers.
def f_num(a,b,c):
    num = a
    if b>num:
        num = b
    if c>num:
        num = c
        return num

print(f_num(10,20,30))



#2 Write a Python function to sum all the numbers in a list.
def num_sum(number):
    empty = 0
    for i in number:
        empty += i
    return empty
print(num_sum((8, 2, 3, 0, 7)))


#3 Write a Python function to multiply all the numbers in a list.

def num_sum(number):
    empty = 1
    for i in number:
        empty *= i
    return empty
print(num_sum((8, 2, 3, 9, 7)))

#4 Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def number(n):
    if n == 0:
        return 1 
    else:
        return n* number(n-1)
n = int(input("Enter your factorial Number to find wht ever you want: "))
print(number(n))

#5 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
text = " Hi , this is Tawsif Rahman and you are Watching our YOutUbe Channel"

def letter(text):
    upper = 0
    lower = 0
    for i in text:
        if i.isupper():
            upper +=1
        if i.islower():
            lower +=1
    return upper, lower
print(letter(text))
         



    
        




    
