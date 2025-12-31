def minmax_element():

       with open("liczby.txt", "r") as file:
              content = file.readlines()

       min_liczba = float('inf')
       max_liczba = float('-inf')
       min_linia = -1
       max_linia = -1

       for index, line in enumerate(content):
              number = int(line.strip())
              if number < min_liczba:
                     min_liczba = number
                     min_linia = index + 1 
              if number > max_liczba:
                     max_liczba = number
                     max_linia = index + 1

       print(f"najmniejszy element: {min_linia} o wartości \"{min_liczba}\"")
       print(f"największy element: {max_linia} o wartości \"{max_liczba}\"")
       input("aby kontynuować, naciśnij enter.")
       
if __name__ == "__main__":
    minmax_element()