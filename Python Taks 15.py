 #1 Print a Fruit name in the list 

name=['Jack', 'Spike', 'Snowy', 'Oggy', 'Apple']
name.remove('Apple')
print(name)

#2 Print a dog name in the list

name=['Jack', 'Spike', 'Snowy', 'Oggy', 'Apple']
print(name[0:3])

#3 Print a dog and cat name in the list
name=['Jack', 'Spike', 'Snowy', 'Oggy', 'Apple']
print(name[0::3])

#4 Check if list contains Elements are strings
name = ['Jack', 'Spike', 'Snowy', 'Oggy', 'Apple']
string = ' '.join(name)
print(string)
print(type(string))

#5 Check the input type from the user
def check_is_digit(input_str):
     if input_str.strip().isdigit():
         print("User input is Number")
     else:
         print("User input is string")


 num1 = input("Enter number and hit enter: ")
 check_is_digit(num1)
 num2 = input("Enter number and hit enter :")
 check_is_digit(num2)

#6 Checking the user's password until it matches
 import re
 user = True

 while user:
     userInput = input('Enter text : ')

     if re.match("tawsif", userInput):
         user = False
         print("Your Password Match")

#7 people's information through checked input
user = input("Your name: ")

user_info = {'bubly': ['Bubly islam', 'Age - 20' ,'Location - Gazipur'], 'ashik': ['Ashik islam', 'Age - 32' ,'Location - Azimpur'],'rafin': ['Rafin islam', 'Age - 25' ,'Location - Mirpur/sector-2'],'habib': ['Habib islam', 'Age - 31' ,'Location - Uttara/sector-4'],'tawsif': ['Redoan Tawsif', 'Age - 21' ,'Location - Rajshahi'],'rahman': ['Abdur Rahman ( Micky )', 'Age - 19' ,'Location - Tangail- college gate'],'shadhin': ['Shadhin Rahman', 'Age - 23' ,'Location - Munshiganj'],'rabbi': ['Rabbi islam', 'Age - 23' ,'Location - Rampura'],'nila': ['Nila islam', 'Age - 21' ,'Location - Uttara/sector-6/House building'],}

for i in user_info:
    if i == user:
        print("Your Information",  user_info[i])
        break
else:
    print('No entry with that name found.')
