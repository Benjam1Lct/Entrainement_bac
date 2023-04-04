def verifie(tab):
    if len(tab) == 0:
        return False
    for i in range(len(tab)-1):
        if tab[i+1] < tab[i]:
            return False
    return True

urne = ['A', 'A', 'B','B', 'C', 'B', 'C','B', 'C', 'C']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))

election = depouille(urne)
print(election)
print(vainqueur(election))
