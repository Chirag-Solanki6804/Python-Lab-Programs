# 11. WAP program to convert a list of characters entered by user into a string.

# Take a list of characters from the user
char_list = input("Enter characters separated by spaces: ").split()

# Convert the list of characters to a string
result_string = ''.join(char_list)

# Print the resulting string
print("Resulting String:", result_string)
