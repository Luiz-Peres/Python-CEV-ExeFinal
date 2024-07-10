def bold(x):
    return(f"\033[1{x}\033[0")
def light(x):
    return(f"\033[2{x}\033[0")
def underline(x):
    return(f"\033[4{x}\033[0")
def blinking(x):
    return(f"\033[5{x}\033[0")
