def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global - because there is no assignment
eggs = 42 # global
ham()
spam()
print(eggs)
ham()
