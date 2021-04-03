#Create a new list named add_ten that adds ten to every element in the list nums.
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]
print(add_ten)

#Create a new list named divide_by_two that contains half of every element in the list nums.
# Make sure to divide by 2, not 2.0!
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num / 2 for num in nums]
print(divide_by_two)

#Create a new list named double_nums by multiplying each number in nums by two.
nums = [4, 8, 15, 16, 23, 42]
double_nums = [num * 2 for num in nums]
print(double_nums)

#Create a new list named first_character that contains the first character from every name in the list names
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
print(first_character)

# Create a new list named greetings that adds "Hello, " in front of each name in the list names.
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]
print(greetings)

#Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at
# position i equals "Jerry". The entry should be False otherwise
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [i == "Jerry" for i in names]
print(is_Jerry)

#Create a new list named lengths that contains the size of each name in the list of names
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
print(lengths)

#Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]
print(opposite)

#Create a new list named parity that contains a 1 or a 0 for each element of nums.
# For each element, if that element was even, the new list should contain a 0.
# If the element was odd, the new list should contain a 1.
nums = [4, 8, 15, 16, 23, 42]
parity = [(num % 2) for num in nums]
print(parity)

#You’ve been given a list of the numbers between 0 and 10.
# We created this list using the range function!
# Create a new list named squares that contains the square of every number in this list.
nums = range(11)
squares = [num**2 for num in nums]
print(squares)
