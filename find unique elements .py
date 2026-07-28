# Program: Find unique elements present only in one list (not in both)

def unique_to_each(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    only_in_list1 = set1 - set2
    only_in_list2 = set2 - set1
    
    return {
        "only_in_list1": list(only_in_list1),
        "only_in_list2": list(only_in_list2)
    }

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = unique_to_each(list_a, list_b)
print(result)