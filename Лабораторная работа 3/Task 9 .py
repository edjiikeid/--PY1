salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
p = 0
while p <= months:
    p += 1
    salary += 5000
    spend += 6000
    if p >= 1:
        x = spend * (1 + increase) - salary
need_money = x
print(round(need_money))
