somme_paires = 0

for i in range(1, 101):
    if i % 2 == 0:
        somme_paires += i

print("La somme des nombres pairs entre 1 et 100 est :", somme_paires)
