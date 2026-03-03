import time


def Pointfixe(fonction_pointfixe, Q0, tolr, nmax):

    X = [0] * (nmax + 1)
    
    Q_avant = Q0
    Qn = Q0
    
    for i in range(nmax + 1):
        if i == 0:
            X[i] = Q0

            print(f'{i} Qn = {Q0:E}')
            time.sleep(0.5)
            

            Q_avant = Q0
            Qn = fonction_pointfixe(Q0)
            
        else:
            X[i] = Qn
            e_n = abs(Qn - Q_avant)
            

            err_rel = e_n / abs(Qn) if Qn != 0 else e_n
            

            if err_rel < tolr or i == nmax:
                print(f'{i} Qn = {Qn:E}, err = {e_n:E}')
                time.sleep(0.5)
                
                if err_rel < tolr:
                    print('La méthode du point fixe a convergé!')
                else:
                    print('La méthode du point fixe n\'a pas convergé...')
                return X[:i+1]
                
            else:

                Q_next = fonction_pointfixe(Qn)
                e_n_plus1 = abs(Q_next - Qn)
                
                ratio1 = e_n_plus1 / e_n
                ratio2 = e_n_plus1 / (e_n**2)
                ratio3 = e_n_plus1 / (e_n**3)
                

                print(f'{i} Qn = {Qn:E}, err = {e_n:E}, Ratio1 = {ratio1:E}, Ratio2 = {ratio2:E}, Ratio3 = {ratio3:E}')
                time.sleep(0.5)

                Q_avant = Qn
                Qn = Q_next

    return X