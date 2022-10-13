money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
p = money_capital + salary - spend * (1 + increase)
while p > 0:
    p = money_capital + salary - spend * (1 + increase)
    month += 1
    increase += 0.05
    salary += 5000
    spend += 6000
    x = spend * (1 + increase)
    if p < 0:
        break
print(month)
