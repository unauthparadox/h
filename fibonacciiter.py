def fibonacci_iter():
    
    n = int(input("ciąg fibonacciego (iteracyjnie) - podaj ilość wyrazów: "))

    def fibonacci_iter1(n):
        f = [0, 1]
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2]) 
        return f[:n]

    print(f"ciąg: {fibonacci_iter1(n)}")
    input("aby kontynuować, naciśnij enter.")
 
if __name__ == "__main__":
    fibonacci_iter()