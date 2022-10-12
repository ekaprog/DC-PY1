salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
counter = 0

while True:
    counter += 1
    need_money += spend
    if counter > months - 1:
        break
    spend += spend * increase

need_money -= salary * months
print(round(need_money))
