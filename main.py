# Fundamental Data types

# print(type(2+4))
# print(type(2-4))
# print(type(2 * 4))
# print(type(2 / 4))

# print(type(0))

# print(2**3)
# print(5//4)
# print(6 % 4)

# math functons
# print(round(3.9))
# print(abs(-200))

# birth_year = input('What year were your you born? ') # This example code for me

# age = 2021 - int(birth_year) # This example code for me


# print(f'Your age is: {age}' ) # This example code for me

#username = input('Input your username: ')
#password = input('Input your password: ')
#password_length = len(password)
#hiden_password = '*' * password_length

#print(f'Hi {username}, your password {hiden_password} is {len(password)} letters long.')

# lists-3

# fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
#friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

#new_friend = ['Stanley']

# friends.append('Stanley')

# print(sorted(friends))

# dictionary
#
# Scroll down to see the answers!
# 1 Create a user profile for your new game. This user profile will #be stored in a dictionary with keys: 'age', 'username', 'weapons', #'is_active' and 'clan'
#
# user_profile = {
#  'age' : 20,
#  'username' : 'zoomer',
#  'weapons' : ['gun', 'knief', 'arm'],
#  'is_active' : True,
#  'clan' : 'vDele'
#
# }
#
# 2 iterate and print all the keys in the above user.
# print(user_profile)
# 3 Add a new weapon to your user
# user_profile['weapons'].append('gunshot')
# print(user_profile)
# 4 Add a new key to include 'is_banned'. Set it to false
#user_profile.update({'is_banned' : False})
# print(user_profile)
# 5 Ban the user by setting the previous key to True
#user_profile.update({'is_banned' : True})
# print(user_profile)
# 6 create a new user2 my copying the previous user and update the #age value and username value.
#user_profile_2 = user_profile.copy()
#user_profile_2.update({'username':'Alex', 'age':25})
# print(user_profile_2)

# Conditional Logic
#is_old = True
#
#is_licenced = True
#
# if is_old and is_licenced:
#  print('you are old enough to drive!')
# elif is_licenced:
##   print('you can drive now!')
# else:
#  print('chechcheck')
#
# print('okokoko')
#
# Truthy vs Falsey
#
#password = '123'
#username = 'jonny'
#
# if password and username:
#  print('good job!')
#
# Ternary Operator

#condition_if_true if condition else condition_if_false
# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to # message"
#
# print(can_message)

# Short Circuiting
# is_Friend = True
# is_User = False
# if is_Friend or is_User: # or /and
#   print("Best friend forever!")

# Logical Operator
# > <
#print (4 == 5)
#print('a' > '_')
#print( 0 == 0 )
#
# <> == >= <= !=
# and or not
# print(not(1==1))

# Exercise: Logical Operators
#
#is_magician = False
#is_expert = True
#
# check if magician AND expert: "you are master magician"
#
# if is_magician and is_expert:
#  print('you are a master magician!')
#
# check if magician but not expert: "at least you're getting there"
#
# elif is_magician and not is_expert:
#  print("at least you're getting there")
#
#
# if you're not magiccian: "You need magic powers"
#
# elif not is_magician:
#  print('You need magic powers')


# # is vs ==
#
# print(True is True)
# print(1 is 1)
# print([] is [])
# print(10 is 10.0)
# print([] is [])
# print([1,2,3] is [1,2,3])
# a = [1,2,3]
# b = [1,2,3]
# print(a == b)
# print(a is b)

# For Loops

# for item in (1,2,3,4,5,6):
#   print(item)
#   print(item)
#   print(item)
# print(item)

# for item in (1,2,3,4,5,6):
#  for x in ['a', 'b', 'c']:
#     print(item,x)

# # Iterables
# user = {
#   'name': 'Golem',
#   'age': 5006,
#   'can_swim': False
# }
#
# for k, v in user.items():
#    print(k, v)
#
# for item in user.values():
#   print(item)
#
# for item in user.keys():
#   print(item)

# iterabble - list, dictionary, tuple, set, string
# iterate -> one by one check each item in collection

# # Exercis: Tricky Counter
# # counter
# my_list = [1,2,3,4,5,6,7,8,9,10,100]
# counter = 0
# for item in my_list:
#   counter = counter + item
#
# print(counter)
#
# for item in my_list:
#   for item in my_list:
#     print(item)

# range()

# # print(range(0, 100))
#
# for number in range(0, 10):
#   print(number)
#
# for number in range(0, 10):
#   print('number')
#
# for number in range(10, 0, -2):
#   print(number)
#
# for number in range(10):
#   print(list(range(10)))

# enumerate()
#
# for i,chart in enumerate(list(range(100))):
#  print(i, chart)
#  if chart == 50:
#    print(f'index of 50 is: {i}')

# # While Loops
# i = 0
#
# while i < 50:
#   print(i)
#   i += 1
# else:
#   print('done with all the work')
#


# my_list = [1,2,3]
# for item in my_list:
#   print(item)
#
# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# while True:
#   response = input('say something: ')
#   if (response == 'bye'):
#     break

# break, continue, pass

# my_list = [1,2,3]
# for item in my_list:
#   print(item)
#   break
#
# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   break

# my_list = [1,2,3]
# for item in my_list:
#   print(item)
#   continue
#   print(my_list)
#
# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   continue
#   print(my_list)

# my_list = [1,2,3]
# for item in my_list:
#   # thinking about it
#   pass
#
# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   break

# Our First GUI

# #Exercise!
# #Display the image below to the right hand side where the 0 is going to be ' ', and the # 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# #1 iterate over picture
#   # if 0 -> print ' '
#   # if 1 -> print *
#
# for row in picture:
#   for pixel in row:
#     if (pixel == 1):
#       print('*', end='')
#     else:
#       print(' ', end='')
#   print('')

# # DEVELOPER FUNDAMENTALS: IV
# # CLEAN
# # Readability
# # predictability
# # Did not repeat yourself
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# #1 iterate over picture
#   # if 0 -> print ' '
#   # if 1 -> print *
# fill = '*'
# empty = ' '
#
# for row in picture:
#   for pixel in row:
#     if (pixel == 1):
#       print(fill, end='')
#     else:
#       print(empty, end='')
#   print('')

# # Exercise: Check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicate = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in duplicate:
#       duplicate.append(value)
#
# print(duplicate)

# # Functions
# # Idea DRY
# def say_hello():
#   print('helllllo!')
#
# say_hello()
#
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
#
# fill = '*'
# empty = ' '
#
# def show_tree():
#   for row in picture:
#     for pixel in row:
#       if (pixel == 1):
#         print(fill, end='')
#       else:
#         print(empty, end='')
#     print('')
#
# show_tree()
#
# print(show_tree)

# # Parameters and Arguments
# def say_hello(name, emoji):
#   print(f'helllllo {name} {emoji}')
#
# # arguments
# say_hello('Alex', '=)') # call the function
# say_hello('Dan', '=)')

# Default Parameters and Keyword Arguments
# parameters
# Default Parameters
# def say_hello(name='Darth Vader', emoji='=('):
#  print(f'helllllo {name} {emoji}')

# positional arguments
# say_hello('Alex', '=)') # call the function
# say_hello('=)', 'Dan')
# say_hello()

# keywords arguments
# say_hello(emoji="=)", name= 'Bibi') # bad practice


# # Returndef sum(num1, num2):
#   return num1 + num2
#
# # Should do one thing really well
# # Should return something
#
# total = sum(10,16)
# print(total)
# print(sum(10,total))
# print(sum(10, sum(10,5)))
# # [1,2,3].clear() -> None
#
# def sum_sum(num1, num2):
#   def another_func(n1, n2):
#     return n1 + n2
#   return another_func(num1, num2) # returnt -> exit function
#   print('Hello')
# total = sum_sum(10, 20)
# print(total)

# Exercise: Tesla


# #1. Wrap the above code in a function called checkDriverAge(). Whenever you call this # function, you will get prompted for age.
# # Notice the benefit in having checkDriverAge() instead of copying and pasting the # function everytime?
# age = input("What is your age?: ")
#
# def checkDriveAge(age = 0):
#   if int(age) < 18:
# 	  print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
# 	  print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
# 	  print("Congratulations on your first year of driving. Enjoy the ride!")
#
# checkDriveAge()


# #2 Instead of using the input(). Now, make the checkDriverAge() function accept an # argument of age, so that if you enter:
# #checkDriverAge(92);
# #it returns "Powering On. Enjoy the ride!"
# #also make it so that the default age is set to 0 if no argument is given.
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too yound to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge(input("What is your age?: "))

# Metods vs Functions
#
# list()
# print()
# max()
# min()
# input()
#
# def some_random_stuff():
# pass
#
# some_random_stuff()
#
# 'hello'.

# # Docstrings
#
# def test(a):
#   '''
#   Info: this function tests and prints param a
#   '''
#   print(a)
#
#
# help(test)
# print(test.__doc__)

# # CleanCode
#
# def is_odd_or_event(num):
#   if num % 2 == 0:
#     return True
#   elif num % 2 != 0:
#     return False
#
# print(is_odd_or_event(50))
#
# def is_event(num):
#   if num % 2 == 0:
#     return True
#   else:
#     return False
# print(is_event(52))
#
# # Match cleaner
# def is_event(num):
#   return num % 2 == 0
#
# print(is_event(52))

# # №1: Input/Output
# def mean(x: list):
#   mu = sum(x) / len(x)
#   return(mu)
#
# print(mean([1,2,3]))

# # ^args and **kwargs
#
# def super_func(name, *args, i='hi', **kwargs)# :
#   print(*args)
#   total = 0
#   for items in kwargs.values():
#     total += items
#   return sum(args) +total
#
# print(super_func('Andy', 1,2,3,4,5, num1=5, # num2=10))
#
# # Rule: params, *args, default parameters, # **kwargs

# # Exercise: Functions
# def highest_even(li):
#   evens = []
#   for item in li:
#     if item % 2 == 0:
#       evens.append(item)
#   return max(evens)
#
# print(highest_even([2,10,2,3,4,5,6,11]))

# # Walrus Operator
# a = 'helllllll00000000000000o'
#
# if ((n := len(a)) > 10):
#   print(f"too long {n} elements")
#
# while ((n := len(a)) > 1):
#   print(n)
#   a = a[:-1]
#
# print(a)

# # Scope - what variables do I have access to?
# if True:
#   x = 10
#
# def some_func():
#   total = 100
#
# print(x)

# # Scope Rules
#
# a = 1
#
# def parent_local():
#   def confusion_local():
#     a = 5
#     return a
#
# def parent_parent():
#   a = 10
#   def confusion_parent():
#     return a
#   return confusion_parent()
#
# def parent_global():
#   def confusion_global():
#     return a
#   return confusion_global()
#
# def parent_built():
#   def confusion_built():
#     return sum
#   return confusion_built()
#
# print(parent_built())
# print(a)
#
# # 1 - start with local scope
# # 2 - Parent  local?
# # 3 - Global
# # 4 - built inpython functions

# Global Keyword
# Scope - what variables do I have access to?

# a = 10
# def confusion(b):
#   print(b)
#   a = 90
# confusion(300)
# total = 0
# def count():
#   total = 0
#   total += 1
#   return total
# count()
# count()

# total = 0
#
# def count():
#   global total
#   total += 1
#   return total
#
# count()
# count()
# print(count())

# # total = 0
#
# def count(total):
#   total += 1
#   return total
#
# print(count(count(count(total))))
#

# 1 - start with local scope
# 2 - Parent  local?
# 3 - Global
# 4 - built inpython functions

# nonlocal Keyword

# def outer():
#   x = "local"
#   def inner():
#     nonlocal x
#     x = "nonlocal"
#     print("inner:", x)
#
#   inner()
#   print("outer:", x)
#
# outer()

# 1 - start with local scope
# 2 - Parent  local? --> nonlocal x
# 3 - Global
# 4 - built inpython function

# Why Do We Need Scope?
''''
x = float(2.8)
print(x)
x = "Hello"[0]
print(x)
name = "John Appleseed   "
# strip() can be used to remove any whitespace from both the beginning and the end of a string
print(name.strip())
'''
# Which collection is ordered, changeable, and allows duplicate members? LIST
# Which collection does not allow duplicate members? SET


# OOP
# # What Is OOP
# class BigObject: # Class
#     pass
#
# obj1 = BigObject() # instanciate - create object
# obj2 = BigObject() # instanciate - create object
# obj3 = BigObject() # instanciate - create object
#
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type({}))
# print(type(()))
# print(type(obj1))

# Create our Own Objects
#
#class PlayerCharacters:
#   def __init__(self, name, age):
#        self.name = name  # attrubutes
#        self.age = age
#
#    def run(self):
#        print('run')
#        return 'done'
#
#player1 = PlayerCharacters('Alexey', 22)
#player2 = PlayerCharacters('Tom', 22)
#player2.attack = 50
#
#print(player1.name)
#print(player2.attack)
#
# Attributes and Methods
# 
# class PlayerCharacters:
#     # Class Object Attribute
#     membership = True
# 
#     def __init__(self, name, age):
#         if (PlayerCharacters.membership):
#             self.name = name  # attrubutes
#             self.age = age
# 
#     def shout(self):
#         print(f'my name is {self.name}')
# 
#     def run(self, hello):
#         print(f'my name is {self.name}')
# 
# 
# player1 = PlayerCharacters('Alexey', 22)
# player2 = PlayerCharacters('Tom', 22)
# player2.attack = 50
# 
# # help(list)
# 
# print(player2.name)
# print(player1.membership)
# print(player1.shout())
# print(player1.run('hello'))

# __init__
# class PlayerCharacter:
#     membership= True
#     def __init__(self, name = 'anonymous', age = 0):
#         if(age > 18):
#             self.name = name
#             self.age = age
#     def shout(self):
#         print(f"my name is {self.name}")
# 
# player1 = PlayerCharacter('Tom', 18)
# # player2 = PlayerCharacter()
# 
# print(player1.shout())

# Exercise: Cats Everywhere

# Given to below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat("Tom", 3)
cat_2 = Cat("Sam", 4)
cat_3 = Cat("Lex", 5)

# 2 Create a function that finds the oldest cat
def oldCat():
    if 


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

