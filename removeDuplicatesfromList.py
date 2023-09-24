input_list = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(input_list):
    return list(set(input_list))   #list(set(list_name))


unique_list = remove_duplicates(input_list)

print(f"List with duplicates removed: {unique_list}")
