def silnia_iter():

    try:
        n = int(input("silnia (iteracyjnie) - podaj liczbę naturalną: "))
    except ValueError:
        print("to nie jest liczba. spróbuj ponownie.")

    def silnia_iter1(n):
        if n < 0:
            return "nie można obliczyć silni z liczby ujemnej."
        elif n == 0 or n == 1:
            return 1
        else:
            wynik = 1
        for i in range(1, n + 1):
            wynik *= i
        return wynik

    print(f"silnia wynosi: {silnia_iter1(n)}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    silnia_iter()