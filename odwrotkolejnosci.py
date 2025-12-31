def odwrot_wyrazu():

    w = input("odwracanie kolejności liter w wyrazie - podaj wyraz: ")
    def odwrot_kolejnosci_wyrazu(w):
        odwrot_kolejnosci_wyrazu = ""
        for litera in w:
            odwrot_kolejnosci_wyrazu = litera + odwrot_kolejnosci_wyrazu
        return odwrot_kolejnosci_wyrazu

    print(f"odwrócona kolejność: {odwrot_kolejnosci_wyrazu(w)}")
    input("aby kontynuować, naciśnij enter.")
    
if __name__ == "__main__":
    odwrot_wyrazu()
