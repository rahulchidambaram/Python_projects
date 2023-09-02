def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

numerator = 8
denominator = 0
result = divide_numbers(numerator, denominator)

if result is not None:
    print("The result of",numerator,"divided by ",denominator," is: ",result)
