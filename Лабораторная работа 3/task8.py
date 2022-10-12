money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

balance = money_capital + salary

while True:
    if balance < spend:
        break
    balance = balance - spend + salary
    month += 1
    spend += spend * increase

print(month)
