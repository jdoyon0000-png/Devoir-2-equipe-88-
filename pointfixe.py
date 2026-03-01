import time

def Pointfixe(fonction_pointfixe, Q0, tolr, nmax):
    X = [0] * (nmax + 1)
    Q_actuel = Q0

    for i in range(nmax + 1):

        if i == 0:
            print(f'{i} Q0 = {Q_actuel:E}')
            time.sleep(0.5)
            X[i] = Q_actuel

        elif i == 1:
            Q_suivant = fonction_pointfixe(Q_actuel)
            erreurRelative = abs((Q_suivant - Q_actuel) / Q_suivant)

            print(f'{i} Q_actuel = {Q_actuel:E}, Q_suivant = {Q_suivant:E}, err_rel = {erreurRelative:E}')
            time.sleep(0.5)

            X[i] = Q_suivant

            if erreurRelative < tolr:
                print('La méthode du point fixe a convergé!')
                return X[:i+1]

            Q_actuel = Q_suivant

        else:
            Q_suivant = fonction_pointfixe(Q_actuel)
            erreurRelative = abs((Q_suivant - Q_actuel) / Q_suivant)

            e_n = abs(X[i-1] - X[i-2]) 
            e_n_plus_1 = abs(Q_suivant - Q_actuel)
       
            ratio1 = e_n_plus_1 / e_n if e_n != 0 else 0
            ratio2 = e_n_plus_1 / (e_n**2) if e_n != 0 else 0

            print(f'{i} Q_actuel = {Q_actuel:E}, Q_suivant = {Q_suivant:E}, err_rel = {erreurRelative:E}, Ratio1 = {ratio1:E}, Ratio 2 = {ratio2:E}')
            time.sleep(0.5)

            X[i] = Q_suivant

            if erreurRelative < tolr:
                print('La méthode du point fixe a convergé!')
                return X[:i+1]

            Q_actuel = Q_suivant

    print('La méthode du point fixe n\'a pas convergé...')
    return X
