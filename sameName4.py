def spam():
    print(eggs) #ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

# Doesn't work because eggs is assigned in spam but called before it is assigned.
# The global variable for eggs cannot be used if eggs is assigned in the function
