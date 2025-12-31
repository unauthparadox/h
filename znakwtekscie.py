def znak_w_tekscie():

    t = input("zliczenie znaku w tekście - podaj tekst, w jakim chcesz zliczyć wystąpienia: ")
    z = input("jaki znak chcesz zliczyć?: ")

    def zlicz(t, z):
        return t.count(z)

    print(f"ilosc wystapien znaku \"{z}\" w tekscie: {zlicz(t, z)}")
    input("aby kontynuować, naciśnij enter.")
    
if __name__ == "__main__":
    znak_w_tekscie()