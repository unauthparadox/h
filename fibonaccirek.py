def fibonacci_rek():

    n = int(input("ciąg fibonacciego (rekurencyjnie) - podaj ilość wyrazów: "))

    def fibonacci_rek1(n):
        if n <= 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            wczesniejsze = fibonacci_rek1(n - 1)
            wczesniejsze.append(wczesniejsze[-1] + wczesniejsze[-2])
            return wczesniejsze

    print(f"ciąg: {fibonacci_rek1(n)}")
    input("aby kontynuować, naciśnij enter.")

if __name__ == "__main__":
    fibonacci_rek()