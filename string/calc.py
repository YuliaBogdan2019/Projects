arg1=input('Vvedite chislo 1   ')
arg2=input('Vvedite chislo 2   ')
action=input('Vvedite deistvie')
actions=['+','-','*','/']

try:
    if'.' in arg1:
        arg1=float(arg1)
    else:
        arg1=int(arg1):
            print('Error arg1')
        exit(1)
try:
    if'.' in arg1:
        arg1=float(arg2)
    else:
        arg2=int(arg2)
    print('Error arg2')
        exit(1)


if action in actions:
    print('ok')
else:
    print('error')

if action=='+':
    print(arg1+arg2)
elif action=='-':
    print(arg1-arg2)
elif action=='*':
    print(arg1*arg2)
elif action=='/':
    print(arg1/arg2)
