import re

def replace_with_colon(text):
    pattern = r"[ ,.]"  
    return re.sub(pattern, ":", text)

test_string = "Привет, мир. Это тест. 123.45"
result = replace_with_colon(test_string)
print(result)
