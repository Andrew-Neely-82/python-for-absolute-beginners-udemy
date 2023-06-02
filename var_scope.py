example = 'hello world' # global variable

def loc_ex():
    example = 'this is a local variable' # local variable
    return example
    
print(example)
print(loc_ex())