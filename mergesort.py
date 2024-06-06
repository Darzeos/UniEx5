#6. Moved import to top of code
import matplotlib.pyplot as plt

#1. Changed name of function better represent workings
#Assigns an element from old_list[j] to new_list[i]
def assign_element(new_list, i, old_list, j):
    new_list[i] = old_list[j]

#2. Shortend parameter name
#merge sort body
def merge_sort(arr):
    #3. Removed redundanten checks and renamed variables
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        #4. Renamed indexes for better recognition
        left_index = 0
        right_index = 0
        sorted_index = 0

        # Merge the sorted halves
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                assign_element(arr, sorted_index, left_half, left_index)
                left_index += 1
            else:
                assign_element(arr, sorted_index, right_half, right_index)
                right_index += 1
            sorted_index += 1

        # Copy any remaining elements of left_half
        while left_index < len(left_half):
            arr[sorted_index] = left_half[left_index]
            left_index += 1
            sorted_index += 1

        # Copy any remaining elements of right_half
        while right_index < len(right_half):
            arr[sorted_index] = right_half[right_index]
            right_index += 1
            sorted_index += 1

#5. Extracted plot functions to create seperate plots via parameter to remove code doubling
def plot_list(arr, title):
    x = range(len(arr))
    plt.plot(x, arr)
    plt.title(title)
    plt.show()


#7. Renamed some variables
# Example usage
myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
# Plot original list
plot_list(myList, 'Original List')
    
# Sort the list using merge sort
merge_sort(myList)
    
# Plot sorted list
plot_list(myList, 'Sorted List')