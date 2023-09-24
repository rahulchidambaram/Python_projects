#reverse using for loop
string = input("Enter a word :")

def reverse(string):
    result = ""
    for i in string:
        result = i + result   
    return result

print("Original String :",string)
print("Reverse String :",reverse(string))


#reverse inbuilt function - reversed()

string = input("Enter a word :")
result = "".join(reversed(string))
print("Reverse String :",result)


#reverse using extended slice

slicestr = input("Enter a word :")
print("Reverse String :",slicestr[::-1])   #start,stop,step - [null:null:-1]
    