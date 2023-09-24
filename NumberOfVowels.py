enter = input("Enter a string :")

def vowels_count(enter):
    vowels = "AEIOUaeiou"
    count = 0
    for i in enter:
        if i in vowels:
            count+=1
    return count

result = vowels_count(enter)
print("The number of vowels present in the string :",result)
