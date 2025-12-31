def czynniki_pierwsze():

    n = int(input("rozkład na czynniki pierwsze - podaj liczbę całkowitą: "))
        
    def czynniki_pierwsze1(n):
        czynniki = []
        dzielnik = 2
        while n > 1:
            if n % dzielnik == 0:
                czynniki.append(dzielnik)
                n //= dzielnik
            else:
                dzielnik += 1
        return czynniki
    
    print(f"czynniki pierwsze: {czynniki_pierwsze1(n)}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    czynniki_pierwsze()