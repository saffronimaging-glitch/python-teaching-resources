# Topic: Strings vs Numbers
# Description: Quotation marks change how Python treats values.

number = 10          # Integer
text_number = "10"   # String

print("Number + 5 =", number + 5)

# This will NOT work as expected:
# print(text_number + 5)

# Instead:
print("Text number:", text_number)
