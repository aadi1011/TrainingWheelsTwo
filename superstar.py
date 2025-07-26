print("hello world")

def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
def add(a, b):
    """Function to add two numbers."""
    return a + b

# This is a comment line
print("Why is there so much traffic in sus??")# This is a comment line

# Open the file in read mode
with open('example.txt', 'r') as file:
    content = file.read()

# Modify the content (replace 'oldword' with 'newword')
modified_content = content.replace('oldword', 'newword')

# Open the file in write mode and save the modified content
with open('example.txt', 'w') as file:
    file.write(modified_content)

print("File modified successfully.")