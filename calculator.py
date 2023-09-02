import basiccalculator
import scientificcalculator

# Using functions from basiccalculator module
result_add = basiccalculator.add(10, 5)
result_subtract = basiccalculator.subtract(15, 3)
result_multiply = basiccalculator.multiply(4, 6)

print("Basic Calculator:")
print("10 + 5 = ",result_add)
print("15 - 3 = ",result_subtract)
print("4 * 6 = ",result_multiply)

# Using functions from scientificcalculator module
result_area_circle = scientificcalculator.area_of_circle(5)
result_area_triangle = scientificcalculator.area_of_triangle(4, 8)

print("\nScientific Calculator:")
print("Area of circle with radius 5: ",result_area_circle)
print("Area of triangle with base 4 and height 8: ",result_area_triangle)