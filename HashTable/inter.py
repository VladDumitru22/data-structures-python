def item_in_common(list1, list2):
    hash_table = {}

    for num in list1:
        hash_table[num] = True
    
    for num in list2:
        if num in hash_table:
            return True
    return False

print(item_in_common([1, 2, 10], [3, 5, 7]))
