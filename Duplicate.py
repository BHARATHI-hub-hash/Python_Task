#defining a function

def find_duplicate(list1, list2, list3):

    #convert list to set
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    #find duplicates
    duplicates = set1.intersection(set2).intersection(set3)

    return duplicates

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 4, 5, 8, 9]
list3 = [2, 4, 5, 10, 11]

duplicates = find_duplicate(list1, list2, list3)
print(f"The duplicates in all 3 lists are: {duplicates}")
