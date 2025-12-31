def szyfr_cezara():

    t = input("szyfr cezara - podaj tekst (małe litery): ")
    try:
        n = int(input("o ile chcesz przesunąć litery? (podaj numer): "))
    except ValueError:
        print("to nie jest liczba. spróbuj ponownie.")

    def szyfr_cezara1(t, n):
        alfabet = "abcdefghijklmnopqrstuvwxyz"
        wynik = ""

        for znak in t:
            if znak in alfabet:
                i = alfabet.index(znak)
                wynik += alfabet[(i + n) % 26]
            else:
                wynik += znak

        return wynik

    print("szyfrogram: ", szyfr_cezara1(t, n))
    input("aby kontynuować, naciśnij enter.")
    
if __name__ == "__main__":
    szyfr_cezara()