

"""
O(1) - Constant Time

"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# constant time: regardless of how long the list is, 
# you will always only print the first item, so it's O(1)
def sample_print(animal_list):
    print(animal_list[0])

# constant time again, because even if the range is one million, 
# you will perform the same number of operations
def sample_print_2(animal_list):
    for i in range(1000):
        print(animal_list[0])    

"""
O(n) - Linear Time
"""

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# there is a linear relationship between size of the input 
# and the number of operations it takes to process it all
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
​
​
"""
O(n) - Linear Time (but this example will take longer than the true O(n))
"""
​
​
def print_animals(animal_list):
    for i in range(len(animal_list)): # this part is O(n)
        print(animal_list[i]) # this part is O(1)
        my_number = 0 # this part is O(1)
        for _ in range(100000): # this part is constant, O(1)
            my_number += 1
# ​so all together it's O(n * (1 + 1 + 1 + (100000 * 1))) = O (n * 100003)
# O(100003n) but to describe the shape we can simplify it by dropping the constant
# and end with O(n).. but it's still going to be slower than the true O(n)
​
"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""
​
​
"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# Print a list of all possible animal pairs
def print_animal_pairs(animals): # O(n^2) because O(n * n * 1)
    for animal_1 in animals: # O(n)
        for animal_2 in animals: #O(n)
            print(f"{animal_1} - {animal_2}") # O(1)
​
​
# Print a list of all possible animal triples
def print_animal_triples(animals): #O(n ^ 3) because 3 for loops
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
# Print a list of all possible animal triples
def print_animal_triples():
    for animal in animals:
        print(animal)
​
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten"tuples?
"""
​
​
"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# free all the animals, half at a time
# (remove them from the array)
def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]
​
# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time
​
​
"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
