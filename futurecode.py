# string1 = 'Goodbye'
# string2 = 'World'
# for i in range(len(string1)):
    
#     if i<len(string2):
#         print(string1[i],string2[i])
#     else:
#         print(string1[i])

# string1 = 'Hello'
# string2 = 'Elizabeth'
# for i in range(len(string1)):
#     if i<len(string2):
#          print(string1[i],string2[i])
#     else:
#         print(string1[i], ' ')
# if len(string1)<len(string2):
#     for j in range(len(string1), len(string2)):
#         print(' ', string2[j])



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# # print(numbers)
# new = []
# # n=''
# for num in numbers:
#     if  num>5:
#         new.append(num)
# print(new)

# things = ['This', 'is', 'a', 'list']
# thing_to_find = 'is'

# p = False
# for char in things:
#     if char ==thing_to_find:
#       p =True
#       break
# print(p)

# words = ['This', 'is', 'a', 'list']

# print(words[0])
# print(words[1])
# print(words[2])
# print(words[3])
# print(words[4])


# words = ['This', 'is', 'a', 'list']
# indices = range(4)

# for index in indices:
#     print(index)
#     print(words[index])

# indices = range(4)

# print(indices[0])
# print(indices[1])
# print(indices[2])
# print(indices[3])
# print(indices[4])
# words = ['This', 'is', 'a', 'list']
# print(len(words))
# print(words[len(words)-1])


# things = ['on', 'the', 'way', 'to', 'the', 'store']

# to_find = 'the'

# # for index in range(len(words)):
# #     print(index)
# #     print(words[index])


# things = ['on', 'the', 'way', 'to', 'the', 'store']

# to_find = 'the'
# for char in range(len(things)):
#     if things[char] == to_find:
#         index = char
#         # break
#         # words += char
#         break
#     # if index ==
# print(index)

# string1 = 'Hello'
# string2 = 'World'

# for i in range(len(string1)):
#     char1 = string1[i]
#     char2 = string2[i]
#     print(char1 + ' ' + char2)

# string1 = 'Goodbye'
# string2 = 'World'

# for i in range(len(string1)):
#     if i< len(string2):
#         print(string1[i]+' '+string2[i] )
#     else:
#         print(string1[i])

# print('\n')


    
# string1 = 'Hello'
# string2 = 'Elizabeth'

# for i in range(len(string1)):
#     if i < len(string2):
#         print(string1[i], string2[i])
#     else:
#         print(string1[i], " ")
        
# if len(string2) > len(string1):
#     for j in range(len(string1), len(string2)):
#         print(" ", string2[j])



# Calling function and methods
# string1 = 'Hello'print(callable(len))
# print(len)
# print(print)

# len(things) 
# print(things)
# callable
# len
# print
# f = 'a string'
# print(callable(f))
# f()

# things = print([1, 2, 3])
# length = len(things)
# printed = print(length)
# print(printed)


# word = 'Hello'
# print(word.upper)
# print(word.upper())

# word.append('!')


# nums = [1, 2, 3]
# new_nums = nums + [4, 5]
# print(new_nums)
# print(nums)
# nums.append(4)
# print(nums)

# some_list[index] = new_value
# nums = [1, 2, 3]
# nums[1]=9
# print(nums)

# [7, 8, 9, 8].index(8)

# nums =[1,2,3]
# nums.remove(1)
# print(nums)



# x = ['a', 'b', 'c']
# x.append(x.pop(0))
# x[len(x) - 1] =x[0]
# y = x + [x[0]]
# print(y)
# x = [1, 2, 0, 3]
# x.remove(0)
# x.pop(x.index(0))
# print(x)

# nums = [2, 9, 1, 8, 5, 64]
# print(7 in nums)
# print(2 in nums)



# x = [1, 2, 0, 3]
# y = x.count(1) > 0
# print(y)

# x = 100
# y =sum(range(x+1))
# print(y)


# x = [12, -6, 2, -1, 3]
# y = sorted(x)[1]
# print(y)


# String Methods and Immutability


# print('the' in 'feed the dog and the cat')
# string = 'feed the dog and the cat'
# print(string.count('the'))
# print(string.index('the'))

# 'Python'.append(' is cool!')

# word.lower()

# sentence = 'Python rocks!'
# new_sentence = sentence.upper()
# print(sentence)
# print(new_sentence)

# nums = [1,2,3,4,5]
# nums.insert(2,9)
# print(nums)

# all_numbers = [2, 4, 8, 1, 9, 7]

# small = []
# big_numbers = []

# for number in all_numbers:
#     if number <= 5:
#         small.append(number)
#     else:
#         big_numbers.append(number)

# print(small)
# print(big_numbers)




# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list2 = list1
# print(list1)
# print(list2)
# print(list1 == list2)

# print(list1 is list2)

# list1.append(4)

# print(list1)
# print(list2)

# never modify something while you iterate over it



# numbers = [10, 7, 8, 3, 12, 15]
# big_numbers =[]
# # numbers.copy()

# for number in numbers:
#     # number = numbers[i]
#     if number > 10:
#         big_numbers.append(number)
# print(big_numbers)


# #  To reiterate, never modify something while you iterate over it. Your options are:

# # Modify a copy
# # Iterate over a copy
# # Don't modify anything, make a new version instead.

# numbers = [10, 7, 8, 3, 12, 15]
# big_numbers =[]
# # 

# for number in numbers.copy():
#     # number = numbers[i]
#   if number <= 10:
#         numbers.remove(number)
# print(numbers)

# # one more method

# numbers = [10, 7, 8, 3, 12, 15]
# big_numbers = numbers.copy()

# for number in numbers:
#     if number <= 10:
#         big_numbers.remove(number)
# print(big_numbers)

# Single and Double Quotes in Strings



# name = 'Alice'

# name = "Alice"
# friend = 'Bob'
# meal = "lunch"
# print(f"{name} went to {meal} with {friend}.")


# name = "Alice"
# age = 20
# print(f"Hello {name}. You are {age} years old.")

# people = ["Alice", "Bob", "Charlie"]
# print(f"There are {len(people)} people waiting, the first one's name is {people[0]}")


# people = ["Alice", "Bob", "Charlie"]
# print(f"There are {len(people)} people waiting, the first one's name is {people[0]}.")

# for letter in "ABC":
#     # print(letter)
#     for number in range(4):
#         print(f'{letter} {number}')
#     print('---')


# start = 1
# end = 12

# for i in range(1,13):
#     for j in range(1,13):
#         result= i *j
#         print(f"{i} x {j} = {result}")
#     print('---')

# players = [ "Alice", "Bpb", "Charlie"]
# fix = ''
# for i in range(len(players)):
#     for j in range(len(players)):
#         if i!= j:
#             print(f"{players[i]} vs {players[j]}")
        
    
# letters = "ABCD"
    
# for i in range(len(letters)):
#     for j in range(len(letters)):
#         for k in range(len(letters)):
#             for l in range(len(letters)):
             
#                 print(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]}")

# letters = "ABCD"

# # Iterate through each possible position of the password
# for a in letters:
#     for b in letters:
#         for c in letters:
#             for d in letters:
#                 password = a + b + c + d
# #                 print(password)

# size = 5

# for i in range(size ,0,-1):
#     # length = size -1
#     line = ''
#     for j in range(i):
#         line += '+'
#     print(line)
        
# size = 5

# for i in range(size):
#     length = size - i
#     line = ''
#     for k in range(length):
#         line += '+'
#     print(line)

        
# players = ['Charlie', 'Alice', 'Dylan', 'Bob']

# # Outer loop for the leftmost person in each pair
# for i in range(len(players)):
#     # Inner loop for the right person in each pair
#     for j in range(i+1, len(players)):
#         print(players[i], "vs", players[j])
# 

# players = ['Charlie', 'Alice', 'Dylan', 'Bob']
# for i in range(len(players)):
#     for j in range(len(players)):
#         if i < j:
#             print(f'{players[i]} vs {players[j]}')

# a = 2
# b = 3
# c = 4
# d = 5
# print(a * b + c * d)

# word = 'AMAZING'
# vowels = []
# consonants = []
# for letter in word:
#     if letter.lower() in 'aeiou':
#         vowels.append(letter)
#     else:
#         consonants.append(letter)
# print(vowels)
# print(consonants)

# strings = ["abc", "def", "ghi"]
# # string = strings[1]
# print(strings[-2][-1])
# strings = [['hello', 'there'], ['how', 'are', 'you']]
# # print(strings[1][2][0])
# strings[1].append("today")
# print(strings)

# Looping over a nested loop 

# numbers = [[1, 2, 3], [4, 5], [6], []]
# for sublist in numbers:
#     for num in sublist:
#         print(num)
#     print('---')

# strings = [
#     [
#         "hello there",
#         "how are you",
#     ],
#     [
#         "goodbye world",
#         "hello world",
#     ]
# ]

# word = "goodbye"

# found = False  

# for sublist in strings:
#     for string in sublist:
#         if word in string:
#             found = True
#             break

#     print(found)

# strings = ["abc", "def", "ghi"]
# for i in range(len(strings[0])):
#     line = ''
#     for j in strings:
#         line += j[i]
#     #  i = string
#     print(line)


# strings = ["abcqwe", "def", "ghiq"]
# lengths = []

# for string in strings:
#     lengths.append(len(string))
# length = max(lengths)

# for i in range (length):
#     line =""
#     for string in strings:
#         if i >= len(string):
#             line +=" "
#         else:
#                 line += string[i]
#     print(line)

# def say_hello(person_name):
#     print(f"Hello {person_name}!")
#     print("How are you?")
# say_hello("Alice")
# say_hello("Bob")
    
# def print_twice(x):
#     print(x)
#     print(x)
# print_twice("Hello")

# def print_many(n,  thing):
#     for _ in range(n):
#         print(thing)
# def print_twice(x):
#     print_many(2, x)
    
# print_twice("Hello")


# def double(x):
#     return x * 2

# number = 5
# twice = double(number)
# print(number)
# print(twice)

# def double(x):
#     return x * 2

# number = 5
# double(number)
# print(number)


# def double(x):
#     return x * 2

# def quadruple(x):
#     return double(double(x))

# number = 5
# double(number)
# print(double)

# def quadruple(x):
#     x = double(x)
#     x = double(x)
#     return x
    
# def quadruple(x):
#     return double(double(x))
    
# n =5


# __---------Testing functions----------

# def assert_equal(actual,expected):
#     if actual == expecte:
#         print('OK')
#     else:
#         print(f"Error!{repr(actual)} != {repr(expected)}")


# def double(x):
#     return x * 3
    
# assert_equal(double(2),4)
# assert_equal(double(5),10)

# def double(x):
#     return x * 2

# def quadruple(x):
#     return double(double(x))

# assert_equal(quadruple(2),8)
# assert_equal(quadruple(5), 20)
# string ='more'
# sides='++'
# def surround(string,sides):
#     return sides + string +sides
    
# assert_equal(surround("more", "++"), "++more++")
# assert_equal(surround("the same", "="), "=the same=")

    





# string = ''
# level = ''
# surround = ''

# def surround(string, char):
#     return char + string + char

# def alert(string, level):
#     string = surround(string, ' ')
#     for _ in range(level):
#         string = surround(string, '!')
#     return string
# assert_equal(alert("Warning", 2), "!! Warning !!")
# assert_equal(alert("DANGER", 4), "!!!! DANGER !!!!")

# name = 'Alice'
# print
# -------------return ends the function call-----------
# def foo():
#     return 1
#     return 2
# print(foo())
# def double_numbers(numbers):
#     for x in numbers:
#         return x * 2

# assert_equal(double_numbers([1, 2, 3]), [2, 4, 6])


# def foo():
#     for letter in 'abc':
#         for number in range(3):
#             print(f"{letter} {number}")
#             if letter == 'b':
#                 break

# foo()



# def is_friend(name):
#     if name == "Alice":
#         return True
#     elif name == "Bob":
#         return True
#     else:
#         return False
     

# assert_equal(is_friend("Alice"), True)
# assert_equal(is_friend("Bob"), True)
# assert_equal(is_friend("Charlie"), False)
    


# def is_friend(name):
#     return name == "Alice" or name == "Bob"

    

# assert_equal(is_friend("Alice"), True)
# assert_equal(is_friend("Bob"), True)
# assert_equal(is_friend("Charlie"), False)


# def is_friend(name):
#     return name == "Alice" or "Bob"

    

# assert_equal(is_friend("Alice"), True)
# assert_equal(is_friend("Bob"), True)
# assert_equal(is_friend("Charlie"), False)


# def is_valid_percentage(x):
#     if x<0 or x>100:
#         return False
#     else: 
#         return True
# assert_equal(is_valid_percentage(-1), False)
# assert_equal(is_valid_percentage(0), True)
# assert_equal(is_valid_percentage(50), True)
# assert_equal(is_valid_percentage(100), True)
# assert_equal(is_valid_percentage(101), False)

# ---------------Introducing and--------------------------

# def is_valid_percentage(x):
#     if x>=0 and x<=100:
#         return True
#     else: 
#         return False
# assert_equal(is_valid_percentage(-1), False)
# assert_equal(is_valid_percentage(0), True)
# assert_equal(is_valid_percentage(50), True)
# assert_equal(is_valid_percentage(100), True)
# assert_equal(is_valid_percentage(101), False)

# def all_equal(row):
#     return row[0] == row[1] == row[2]

# assert_equal(all_equal(["X", "X", "X"]), True)
# assert_equal(all_equal(["O", "O", "O"]), True)
# assert_equal(all_equal(["X", "O", "X"]), False)


# ---------------Multi-line statements----------------------

# name = "Bob"

# is_friend = name == "Alice" or \
#             name == "Bob"
# print(is_friend)

# is_friend = (name == "Alice" or
#              name == "Bob")
# print(is_friend)

# is_friend = [name == "Alice",
#              name == "Bob"]
# print(is_friend)

# print(name == "Alice" or
#       name == "Bob")

# -------------Combining and and or--------------------

# def diagonal_winner(board) :
#     middle = board[1][1]
#     return (
#             ((middle == board [0][0] and middle == board [2][2] )) or
#             (middle == board[0][2] and middle ==board[2][0] )
# )
# assert_equal(
#     diagonal_winner(
#         [
#             ['X', 'O', 'X'],
#             ['X', 'X', 'O'],
#             ['O', 'O', 'X']
#         ]
#     ),
#     True
# )

# assert_equal(
#     diagonal_winner(
#         [
#             ['X', 'X', 'O'],
#             ['X', 'O', 'O'],
#             ['O', 'X', 'X']
#         ]
#     ),
#     True
# )

# assert_equal(
#     diagonal_winner(
#         [
#             ['O', 'X', 'O'],
#             ['X', 'X', 'X'],
#             ['O', 'O', 'X']
#         ]
#     ),
#     False
# )

# Introducing not

# def invalid_image(filename):
#     return not (filename.endswith(".png") or filename.endswith(".jpg"))
 
# assert_equal(invalid_image("dog.png"), False)
# assert_equal(invalid_image("cat.jpg"), False)
# assert_equal(invalid_image("invoice.pdf"), True)
def invalid_image(filename):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        return False
    else:
        return True

assert_equal(invalid_image("dog.png"), False)
assert_equal(invalid_image("cat.jpg"), False)
assert_equal(invalid_image("invoice.pdf"), True)