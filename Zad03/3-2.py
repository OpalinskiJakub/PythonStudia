

L = [3, 5, 4] ; L = L.sort()

#Podany kod przypisuje None do L zamiast posortrowanej listy
#Aby zachowac posortowana liste nalezaloby to zrobic tak:
#L = [3, 5, 4] ; L.sort()

#---------------------------------------------------------------
x, y = 1, 2, 3

#Podany kod próbuje się przypisać trzy wartości do dwóch zmiennych
# To spowoduje błąd, ponieważ liczba wartości po prawej 
# stronie przypisania nie zgadza się z liczbą zmiennych po lewej stronie przypisania.

#---------------------------------------------------------------

X = 1, 2, 3 ; X[1] = 4

# Podany kod proboje utworzyć krotke,
# Krotki  są niemutowalne, co oznacza,
# że nie można zmieniać ich zawartości po ich utworzeniu. Poprzez X[1] = 4, 
# próbujemy  zmienić wartość drugiego elementu krotki X, co powoduje błąd.
#---------------------------------------------------------------

X = [1, 2, 3] ; X[3] = 4
# Podany kod próbuje zmienić wartość elementu listy o indeksie 3 na 4.
# Jednak lista nie zawiera indeksu 3 więc spowoduje to błąd.

#---------------------------------------------------------------

X = "abc" ; X.append("d")

#Podany kod tworzy łańcuch, łańcuchy sa niezmiennymi sekwencjami,
#proba dodania d poprzez append generuje bład



#---------------------------------------------------------------

L = list(map(pow, range(8)))

# W podanym zamiast pow powinnismy umiesic lambde 
# można rozwiazac to w taki sposób za pomoca lambdy:
#x=lambda i : pow(i,2)
#L = list(map(x, range(8)))




#---------------------------------------------------------------



