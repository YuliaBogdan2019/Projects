# import Bcalc as BC
# m_arg1, m_arg2, m_action=BC.input_date()
# try:
#     m_arg1, m_arg2, m_action = BC.check_date(m_arg1, m_arg2, m_action)
# except CalcException as e:
#     print(e)
#     exit(1)
# BC.output_date(m_arg1, m_arg2, m_action)
from Bcalc import input_date
a,b,c=input_date()
print(a,b,c)
