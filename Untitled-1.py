

def plus(a,b):
    c = int(a) + int(b)
    return(c)
    
def multyply(a,b):
    c = int(a) - int(b)
    return(c)
    
def div(a,b):
    c = int(a) / int(b)
    return(c)

def subtract(a,b):
    c = int(a) * int(b)
    return(c)
    
user_input = input('Введите выражение, знакчение которого надо вычислить ')
if len(user_input) > 3:
    N =str(user_input[0] + user_input [2] + user_input[4])
match user_input[3]:
    case "+":
        res = (plus(user_input[0],user_input[4]))
        
    case "-":
        res = (multyply(user_input[0],user_input[4]))
        
    case "/":
        res = (div(user_input[0],user_input[4]))
        
    case "*":
        res = (subtract(user_input[0],user_input[4]))
        