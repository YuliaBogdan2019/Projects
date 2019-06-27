class CalcException(Exception):
    pass

def check(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        arg1, arg2, action=result
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
    return wrapper

@check
def input_date():
    arg1=input('Vvedite chislo >>   ')
    arg2=input('Vvedite chislo >>  ')
    action=input('Vvedite deistvie >>')
    actions=['+','-','*','/']
    return arg1, arg2, action


def output_date(arg1, arg2, action):
    if action=='+':
        print(arg1+arg2)
    elif action=='-':
        print(arg1-arg2)
    elif action=='*':
        print(arg1*arg2)
    elif action=='/':
        print(arg1/arg2)


if __name__ == '__main__':
    try:
        m_arg1, m_arg2, m_action = input_date()
    except CalcException as e:
        print(e)
        exit(1)
    output_date(m_arg1, m_arg2, m_action)
