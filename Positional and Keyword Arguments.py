#Normal Argument
def standard_arg(arg):
    print(arg)

#Positional Argument
def pos_only_arg(arg, /):
    print(arg)
    
#Keyword Argument
def kwd_only_arg(*, arg):
    print(arg)  