bilet = int(input("Сколько билетов хотите приобрести? "))
sum_k_oplate = 0
for i in range(1, bilet+1):
    vozrast_poset = int(input("Сколько лет посетителю? "))
    if vozrast_poset < 18:
        sum_k_oplate += 0
    elif 18 <= vozrast_poset < 25:
        sum_k_oplate += 990
    else:
        sum_k_oplate += 1390
if bilet > 3:
    print(sum_k_oplate * 0.9)
else:
    print(sum_k_oplate)
