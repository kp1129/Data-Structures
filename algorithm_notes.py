"""
If you are looking through unordered data, there's
unfortunately nothing better than looking at each 
item to see if it's what you're looking for. 
So if you can, sort first!
O(n)

"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False        

# https://visualgo.net/bn/sorting    

"""
If you can eliminate half the possibilities each round,
like in binary search, big o improves to O(log n)

"""
def find_value_binary(arr, value):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find middle
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True

        else:
            if value < arr[middle]:
                # search the lower half
                last = middle - 1 
            else:
                # search the upper half
                first = middle + 1

    return found      
          

"""
planning session for insertion sort
https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

"""

def insertion_sort(input_list):

    # think of the first element as sorted

    # for all unsorted items
    for i in range(1, len(input_list)):

        # mark the current item we are considering
        current = input_list[i]

        # look left until we find the proper place to insert the item
        # as we are 'looking left', we need to shift items to the right
        # ix = input_list[i - 1]
        # while input_list[ix] > current

        j = i
        while j > 0 and current < input_list[j - 1]:
            input_list[j] = input_list[j - 1]
            j -= 1

        # when item to the left is less than or equal to current
        # or there are no items to the left" (basically when you've found
        # the insertion point)
        #insert item
        input_list[j] = current

    return input_list

print(insertion_sort([9,8,7,6,5,4,3,2,1]))    