user_input = input("Enter a word or phrase: ")

def palindrome(word):
    word = word.replace(" ","").lower()  # Remove spaces and convert to lowercase

    return word == word[::-1]            # Compare the string with its reverse


if palindrome(user_input):
    print(user_input,"is a palindrome!")
else:
    print(user_input,"is not a palindrome")


