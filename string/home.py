class CalcException(Exception):
    pass

def output(func):

    def output_date(arg1, arg2, action):
        if action=='+':
            print(arg1+arg2)
        elif action=='-':
            print(arg1-arg2)
        elif action=='*':
            print(arg1*arg2)
        elif action=='/':
            print(arg1/arg2)
            return arg1, arg2, action

def check(func):

    def check_date(arg1, arg2, action):
        try:
            if'.' in arg1:
                arg1=float(arg1)
            else:
                arg1=int(arg1)
        except ValueError:
            raise CalcException('Error arg2')

        try:
            if'.' in arg2:
                arg2=float(arg2)
            else:
                arg2=int(arg2)
        except ValueError:
            raise CalcException('Error arg2')

        if action in ['+','-','*','/']:
            print('ok')
        else:
            print('error')
        return arg1, arg2, action

@output
@check
def func():
    arg1=input('Vvedite chislo >>   ')
    arg2=input('Vvedite chislo >>  ')
    action=input('Vvedite deistvie >>')
    actions=['+','-','*','/']
    return arg1, arg2, action

if __name__ == '__main__':
    arg1, arg2, action=func()
    print(CalcException)
