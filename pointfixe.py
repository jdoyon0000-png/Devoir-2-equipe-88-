import time

def Pointfixe(fonction_pointfixe, Q0, tolr, nmax):
    X = [0] * (nmax + 1)
    Q_actuel = Q0

    for i in range(nmax + 1):

        if i == 0:
            print(f'{i} Q0 = {Q_actuel:E}')
            time.sleep(0.5)
            X[i] = Q_actuel

        else:

            Q_suivant = fonction_pointfixe(Q_actuel)
            En = abs(Q_suivant - Q_actuel)
            

            Q_next = fonction_pointfixe(Q_suivant)
            En_plus_1 = abs(Q_next - Q_suivant)
            

            ratio1 = En_plus_1 / En if En != 0 else 0
            ratio2 = En_plus_1 / (En**2) if En != 0 else 0

            print(f'{i} Q_actuel = {Q_actuel:E}, err = {En:E}, Ratio1 = {ratio1:E}, Ratio 2 = {ratio2:E}')
            time.sleep(0.5)

            X[i] = Q_suivant

            if En < tolr:
                print('La méthode du point fixe a convergé!')
                return X[:i+1]

            Q_actuel = Q_suivant

    print('La méthode du point fixe n\'a pas convergé...')
    return X