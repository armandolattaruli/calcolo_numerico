from numpy import *

def bisezioni(f, a, b, tol, itmax):
    # METODO DELLE SUCCESSIVE BISEZIONI
    # Sintassi:
    # [alpha, it] = bisezioni(f, a, b, tol, itmax)
    # help
    # Parametri di input
    # f: funzione di cui cercare uno zero
    # [a, b]: intervallo di lavoro
    # tol: precisione richiesta
    # itmax: numero massimo di iterate consentite

    # Parametri di output
    # alpha: approsimazione di uno zero di f
    # it: numero di iterate consentite

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("La funzione non cambia segno agli estremi dell'intervallo.\n")

    it = 0  # contatore di iterate
    alpha = None  # valore predefinito

    while b - a > tol and it < itmax:  # condizioni: finche b-a non raggiunge la precisione e it deve essere uguale alle iterate massime
        it += 1
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            alpha = c
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        alpha = c  # modifica il valore di alpha solo se il ciclo while viene eseguito

    if alpha is None:
        print("Non e' stato possibile trovare un'approssimazione dello zero della funzione.")
    elif b - a > tol:
        print("Precisione non raggiunta")

    return alpha, it


def f(x):
    y = x - cos(x)
    return y


print(bisezioni(f, 0,pi/2,1e-10,100))
