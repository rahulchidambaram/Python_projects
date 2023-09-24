list1 = [1, 2, 3, 4, 50, 4]
list2 = [3, 4, 50, 6, 7]

def common_elements(list1, list2):
    return list(set(list1) & set(list2))   #removes duplicates and finds common elements


common = common_elements(list1, list2)
print(f"Common elements: {common}")
