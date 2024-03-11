#string method
string_example = 'Hello, world!'
upper_case = string_example.upper()
lower_case =string_example.lower()
lenght_of_string =len(string_example)
capitalized =string_example.capitalize()
reversed_string =string_example[::-1]

#list method
list_example = [1, 2, 3, 4, 5]
list_example.append(6)
removed_element =list_example.pop(2)
sorted_list =sorted(list_example)
list_example.reverse()

#tuple method
tuple_example = (1, 2, 3, 4, 5)
index_of_element = tuple_example.index(3)
count_of_element =tuple_example.count(4)

#set method
set_example = {1, 2, 3, 4, 5}
set_example.add(6)
set_example.remove(3)
set_intersection =set_example.intersection({4, 5, 6})
set_union =set_example.union({7, 8, 9})

#dictinary method
dictionary_example = {'a': 1, 'b': 2, 'c': 3}
key_list =list(dictionary_example.keys())
value_list = list(dictionary_example.values())
item_removed =dictionary_example.pop('b')
dictionary_example.update({'d':4})

#integer method
num = 42
bit_lenght = num.bit_length()
abs_value = abs(num)
binary_representation = bin(num)

#float method
pi =3.14159
rounded_pi =round(pi, 2)


#boolean method
bool_value = True
inverted_bool =not bool_value
bool_as_string =str(bool_value)

#NoneType method
none_value = None # No specific method for non type




#string exercise
my_name = 'kodaolu khalid'
print(my_name)
print(len(my_name))

string =' The boy us very tall'
new_string = string.replace('Tall', 'Short')
print(new_string)

user_input = input('Enter a string')
reversed_string = user_input[::-1]
print('Reversed string:',reversed_string)


Test ='  How are you  '
print(Test.strip())


def is_palindrome(input_string):
    clean_string =''.join(c.lower() for c in input_string if c.isalnum())
    return  clean_string ==clean_string[::-1]
user_input =input('Enter a string:')
result = is_palindrome(user_input)
if result:
    print('The string is a palindrome')
else:
    print('The string is not palindrome')



user_input = input('Enter your e-mail address')




Example = 'How Are You'
print(Example.upper())


sentence = 'I Am a Soft Worker'
print(len(sentence))
print(sentence[1])

sentence1 = sentence[6:18]
print(sentence1)

print(sentence.lower())
print(sentence.upper())


new_sentence = string.replace('You', 'They')
print(new_sentence)


#boolean
age = 25
is_student = False
if age < 18 or is_student:
    print('You are either a student or under 18')
if age >= 18 and not is_student:
    print('You are an adult and not a student')


Today = 'saturday, sunday'
is_weekend = True
if Today == 'saturday, sunday' or is_weekend:
    print('Today is saturday or sunday')
else:
    print('Today is any other day of the week')


same_number_of_fingers =input('Is the number of finger on your left equal to that of the right')
if same_number_of_fingers == True:
    print('The two is equal')
else:
    print('Thr two are not equal')


age = int(input('Are you a teenager'))
is_even = True if age % 2 == 0 else False
is_teenager = True if 13 <= age <= 19 else False
if  is_teenager == True:
    print('You are really a teenager')
else:
    print('You are either not of age or more than the required age')



Name = input('is the letter "a"  in your name: ')
has_letter_a = Name
if has_letter_a == True:
    print('my name consist of letter a')
else:
    print('my name does not consist of yhe letter a')


possibility =input('can you write something')
has_pen = True
has_paper =False
if has_pen == True:
    print('You can write something')
else:
    print('You can write nothing')