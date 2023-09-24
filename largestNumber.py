num_list = [1100,123,432,2,200,46]

#second largest number
                             # print(sorted(num_list)[-2])
list2 = list(set(num_list))
num_list.sort()
print("Second largest Number :",list2[-2])


def find_largest(num):
    if not num:
        return False
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    return largest


largest_num = find_largest(num_list)
print("The largest number is :",largest_num)

