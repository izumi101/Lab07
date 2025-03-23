def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

text = "Hello World!"
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")