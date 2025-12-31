def porownaj_teksty():

    n = input("porównywanie tekstów - podaj pierwszy tekst: ")
    m = input("podaj drugi tekst: ")

    if n == m:
        print("teksty są identyczne.")
    else:
        print("teksty są różne.")
    input("aby kontynuować, naciśnij enter.")
        
if __name__ == "__main__":
    porownaj_teksty()