"""Q. Program implement Merge Sort Algorithm with all the necessary functions."""

# Funtion to divide the lists in the two sublists
def sort(sorted_list):
    if len(sorted_list) <= 1:
        return sorted_list
# Perform merge_sort recursively on both halves
    middle = len(sorted_list) // 2
    left = sorted_list[:middle]
    right = sorted_list[middle:]

    left = sort(left)
    right = sort(right)
    return merge(left, right)
# Defining a function for merge the list
def merge(a_list, b_list):
    combined_list = []
    index_a = 0
    index_b = 0
    length_a = len(a_list)
    length_b = len(b_list)
# Sort each one and place into the result
    while index_a < length_a and index_b < length_b:
        if a_list[index_a] <= b_list[index_b]:
            combined_list.append(a_list[index_a])
            index_a = index_a + 1
        else:
            combined_list.append(b_list[index_b])
            index_b = index_b + 1

    while index_a < length_a:
        combined_list.append(a_list[index_a])
        index_a = index_a + 1
    while index_b < length_b:
        combined_list.append(b_list[index_b])
        index_b = index_b + 1
    return combined_list
# Driver code
list = [51,11,25,10,9,44,13,32,]
print(sort(list))