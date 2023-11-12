def filter_string(input_string):
    filtered_string = ""
    for char in input_string:
        if char.isalpha():
            filtered_string += char
    return filtered_string

input_string = "Hello, World! 123"
filtered_string = filter_string(input_string)
print(filtered_string)
