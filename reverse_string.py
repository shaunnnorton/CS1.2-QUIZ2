from linkedlist import Stack
def reverse_string(string):
    string_stack = Stack()
    reversed_string = ''
    for i in range(len(string)):
        string_stack.append(string[i])
    for i in range(len(string)):
        reversed_string += string_stack.read()
        string_stack.remove()
    return reversed_string
print(reverse_string('hello'))