
def plus(number_list):
    res = number_list[0]
    for i in range (1,len(number_list)):
        res += number_list[i]
    return(res)
    
    
def multyply(number_list):
    res = number_list[0]
    for i in range (1,len(number_list)):
        res *= number_list[i]
    return(res)
    
    
def div(number_list):
    res = number_list[0]
    for i in range (1,len(number_list)):
        res /= number_list[i]
    return(res)
    

def subtract(number_list):
    res = number_list[0]
    for i in range (1,len(number_list)):
        res -= number_list[i]
    return(res)
    
def factorial(number):
    res = 1
    for i in range(1,int(number) + 1):
        res = res * i

    return(res)

def pow(number_list):
    res = number_list[0]
    for i in range (1,len(number_list)):
        res **= number_list[i]
    return(res)

def user_input_split (user_input):
    if '+' in user_input:
        num_list = user_input.split('+')
        oper = '+'

    elif '-' in user_input:
        num_list = user_input.split('-')
        oper = '-'
    elif '*' in user_input:
        num_list = user_input.split('*')
        oper = '*'
    elif '/' in user_input:
        num_list = user_input.split('/')
        oper = '/'
    elif '!' in user_input:
        num_list = user_input.split('!')
        num_list = num_list[0]
        oper = '!'
    elif '^' in user_input:
        num_list = user_input.split('^')
        oper = '^'

    else :
        print('неизвестная операция')

    if type(num_list) == 'list':
        num_list = type_transfer(num_list )
    return (num_list,oper)

def type_transfer (num_list):
    for i in range (0, len(num_list)):
        num_list[i] = float (num_list[i])
    
    return(num_list)
    
user_input = input('Введите выражение, знакчение которого надо вычислить ')
number_list,operations = (user_input_split(user_input))
match operations:
    case '+':
        print(plus(number_list))

    case '*':
        print(multyply(number_list))

    case '-':
        print(subtract(number_list))

    case '/':
        print(div(number_list))

    case '!':
        print(factorial(number_list))

    case '^':
        print(pow(number_list))
    case _:
        print('неизвестная операция ')