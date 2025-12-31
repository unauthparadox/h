def sito_eratostenesa():

    n = int(input("sito eratostenesa - podaj liczbę całkowitą: "))
    liczby = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if liczby[p] == True:
            for i in range(p * p, n + 1, p):
                liczby[i] = False
        p += 1
    pierwsze = [p for p in range(2, n + 1) if liczby[p]]

    print(f"liczby pierwsze: {pierwsze}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    sito_eratostenesa()