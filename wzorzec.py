def wzorzec_w_tekscie():

    t = input("szukanie wzorca w tekście - podaj tekst, w którym chcesz znaleźć wzorzec: ")
    w = input("podaj wzorzec: ")

    if w in t:
        print("wzorzec jest w tekście.")
    else:
        print("wzorca nie ma w tekście.")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    wzorzec_w_tekscie()