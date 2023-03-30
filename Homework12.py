per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада = "))
deposit = []
for key in per_cent:
    deposit.append(int(per_cent[key] * money / 100))
max_deposit = int(max(deposit))
print("Накопленные деньги за год вклада = ", deposit)
print("Максимальная сумма, которую Вы можете заработать - ", max_deposit)
