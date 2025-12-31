def silnia_rek():

    try:
        n = int(input("silnia (rekurencyjnie) - podaj liczbę naturalną: "))
    except ValueError:
        print("to nie jest liczba. spróbuj ponownie.")

    def silnia_rek1(n):
        if n < 0:
            return "nie można obliczyć silni z liczby ujemnej."
        elif n == 0 or n == 1:
            return 1
        else:
            return n * silnia_rek1(n - 1)

    print(f"silnia wynosi: {silnia_rek1(n)}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    silnia_rek()