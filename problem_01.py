num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

if num2 !=0:
quotient_result = round(num1 / num2, 2)
else:
quotient_result = "undefined"


print(f"The sum is {num1 + num2}")
print(f"The difference is {num1 - num2}")
print(f"The product is {num1 * num2}")
print(f"The quotient is {(num1 / num2):.2f}")