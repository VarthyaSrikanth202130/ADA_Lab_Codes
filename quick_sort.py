"""Q. Program to mplement Quick Srot algorithm witl all necessary functions"""

# Function to get pivot element
def pivot(list, start, end):
 
# Initializing 
    pivot = list[start]
    low = start + 1
    high = end
    while True:
        while low <= high and list[high] >= pivot:
            high = high - 1
 
        while low <= high and list[low] <= pivot:
            low = low + 1
 
        if low <= high:
 
# Swapping values to rearrange
            list[low], list[high] = list[high], list[low]
          
        else:
            break
 
# Swapping pivot with high so that pivot is at its right # #position 
    list[start], list[high] = list[high], list[start]
 
# Returning pivot position
    return high
 
# Function to do quick sort
def quick_sort(list, start, end):
    if start >= end:
        return
 
#call pivot element
    p = pivot(list, start, end)
    quick_sort(list, start, p-1)
    quick_sort(list, p+1, end)
 
# Driver code 
myList = [45,22,13,4,78,11,51,10,3]
 
quick_sort(myList, 0, len(myList) - 1)
print(myList)