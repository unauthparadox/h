def dz_na_bin():

    n = int(input("zamiana liczby dziesiętnej na binarną - podaj liczbę dziesiętną: "))

    def dz_na_bin1(n):
        if n == 0:
            return "0"
        bin = ""
        while n > 0:
            r = n % 2
            bin = str(r) + bin
            n //= 2
        return bin

    print(f"liczba binarna: {dz_na_bin1(n)}")
    input("aby kontynuować, naciśnij enter.")
    
if __name__ == "__main__":
    dz_na_bin()