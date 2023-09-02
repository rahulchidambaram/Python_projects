with open("D:\Python\machine.txt", "r") as file:
    content = file.read()

words = content.split()

count_in = 0
count_us = 0
count_eu = 0


for word in words:
    if word.startswith("IN"):
        count_in += 1
    elif word.startswith("US"):
        count_us += 1
    elif word.startswith("EU"):
        count_eu += 1


print("India =",count_in)
print("Europe =",count_eu)
print("USA =",count_us)






