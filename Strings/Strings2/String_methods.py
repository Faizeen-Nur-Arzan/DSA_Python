str1 = "Hello Python"

multilineString = """"
Generalized Syntax:
variable = my_string.method_name()
"""

text = "problem solving is awesome"
capitalized_text = text.capitalize()
print(capitalized_text)

print(text.title())

text2 = "pYtHoN Is cOoL"
lowercased_text = text2.lower()
print(lowercased_text)
uppercased_text = text2.upper()
print(uppercased_text)

is_lower = text.islower()
print(is_lower)
is_upper = text.isupper()
print(is_upper)

print(text2.swapcase())

alphanum = "pi3141592"
print(alphanum.isalnum())

digit = "12334"
print(digit.isdigit())

text = " hello    "
print(text.strip())
print(text.rstrip())

text3 = "I love to solve problems because it makes storms in my brain"
print(text3.replace("storms in my brain", "brainstorming"))

"""
syntax:
separator.join(iterable)
iterable: array(list, tuple, array), strings
"""

string_list = ["Early", "to", "bed", "early", "to", "rise", "makes", "a", "man", "healthy", "wealthy", "and", "wise"]
print(" ".join(string_list))
print("=>".join(string_list))
print("".join(string_list))

my_string = "python is pythonic and python rocks"
print(my_string.count("python"))
print(my_string.count("o"))

my_text = input("Enter a character:\n")
while not len(my_text) == 1:
    my_text = input("ERROR: More than one chracter entered. Try again:\n")
print(ord(my_text))