def count_characters_and_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            char_count = len(content)
            word_count = len(content.split())
            return char_count, word_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0, 0

if __name__ == "__main__":
    file_name = "D:\Python\machine.txt"  
    char_count, word_count = count_characters_and_words(file_name)
    
    print("Total characters in the file: ",char_count)
    print("Total words in the file: ",word_count)
