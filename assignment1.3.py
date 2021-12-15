import decimal
from decimal import Decimal

decimal.getcontext().prec = 1000#保留1000位小数

c = Decimal(7)/Decimal(911)

print(c)
