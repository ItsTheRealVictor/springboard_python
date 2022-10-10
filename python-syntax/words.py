def print_upper_words(*args):
    for arg in args:
        print(arg.upper())

def print_upper_words_starting_with(*args, starts_with):
    for arg in args:
        if arg[0] in starts_with:
            print(arg.upper())


print_upper_words('cat', 'dog', 'hello', 'b')
print_upper_words_starting_with('dog', 'cat', 'ace', 'big', starts_with=['c','b'])