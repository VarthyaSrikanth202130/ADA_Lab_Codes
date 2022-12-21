"""Q.Program to implement Binary Search. """

# Binary search using Iteration
def binarySearchIterative(list, value):
    # Setting start-index and end-index
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        if value == list[mid]:
            return mid  
        elif value < list[mid]:
            high = mid - 1
        else:
            low = low +1
    return None
# Binary search using Recursion
def binarySearchRecursive(list,low,high,value):
    if low <= high:
        mid = (low + high)//2
        if value == list[mid]:
            return mid
        elif value < list[mid]:
            return binarySearchRecursive(list, low, mid-1, value)
        else:
            return binarySearchRecursive(list, mid+1, high, value)

    return None

list = [2,4,5,7,9,12,13,16,19]
print(list)
# Taking input value from user
value = int(input("Enter the key to find: "))
# Calling the function to get the position
print("Using Iteration Found at position: {}".format(binarySearchIterative(list, value)))

print("Using Recursion Found at position: {}".format(binarySearchRecursive(list, 0,len(list)-1, value)))

