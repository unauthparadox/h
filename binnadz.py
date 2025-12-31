def bin_na_dz():

    n = input("zamiana liczby binarnej na dziesiętną - podaj liczbę binarną: ")

    def bin_na_dz1(n):
        dz = 0
        pot = 0
        for i in range(len(n) - 1, -1, -1):
            if n[i] == '1':
                dz += 2 ** pot
            pot += 1
        return dz

    print(f"liczba dziesiętna: {bin_na_dz1(n)}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    bin_na_dz()