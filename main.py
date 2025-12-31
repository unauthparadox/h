import eratostenes
import fibonacciiter
import fibonaccirek
import silniaiter
import silniarek
import czynnikipierwsze
import dznabin
import binnadz
import minmaxelement
import porownajteksty
import odwrotkolejnosci
import znakwtekscie
import wzorzec
import cezar


def main():
    while True:
        print("menu algorytmów:")
        print("1. sito eratostenesa.")
        print("2. ciąg fibonacciego (iteracyjnie).")
        print("3. ciąg fibonacciego (rekurencyjnie).")
        print("4. silnia (iteracyjnie).")
        print("5. silnia (rekurencyjnie).")
        print("6. rozkład na czynniki pierwsze.")
        print("7. zamiana liczby dziesiętnej na binarną.")
        print("8. zamiana liczby binarnej na dziesiętną.")
        print("9. szukanie najmniejszego oraz największego elementu w pliku \"liczby.txt\".")
        print("10. porównywanie tekstów.")
        print("11. odwracanie kolejności liter w wyrazie.")
        print("12. zliczenie znaku w tekście.")
        print("13. szukanie wzorca w tekście.")
        print("14. szyfr cezara.")
        print("0. wyjście.")
        
        try:
            wybor = int(input("wybierz opcję: "))
        except ValueError:
            print("podaj poprawny numer.")
            continue

        if wybor == 0:
            print("byebye :)")
            break
        if wybor == 1:
            eratostenes.sito_eratostenesa()
        elif wybor == 2:
            fibonacciiter.fibonacci_iter()
        elif wybor == 3:
            fibonaccirek.fibonacci_rek()
        elif wybor == 4:
            silniaiter.silnia_iter()
        elif wybor == 5:
            silniarek.silnia_rek()
        elif wybor == 6:
            czynnikipierwsze.czynniki_pierwsze()
        elif wybor == 7:
            dznabin.dz_na_bin()
        elif wybor == 8:
            binnadz.bin_na_dz()
        elif wybor == 9:
            minmaxelement.minmax_element()
        elif wybor == 10:
            porownajteksty.porownaj_teksty()
        elif wybor == 11:
            odwrotkolejnosci.odwrot_wyrazu()
        elif wybor == 12:
            znakwtekscie.znak_w_tekscie()
        elif wybor == 13:
            wzorzec.wzorzec_w_tekscie()
        elif wybor == 14:
            cezar.szyfr_cezara()
        else:
            print("nie ma takiej opcji, wybierz ponownie.")

if __name__ == "__main__":
    main()