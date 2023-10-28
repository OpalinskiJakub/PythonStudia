#Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i
# wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury 
# stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie
# i kontynuować pracę. 

while True:
    try:
        number=input("Podaj liczbe rzeczywsita ")
        
        if number.lower()=="stop":
            break
        
        afterCasting=float(number)
        numberAfterPow=afterCasting ** 3
        
        print(f"x={number} \nx^3={numberAfterPow}")
        
        
    except ValueError:
        print("To nie jest liczba rzeczywista. Spróbuj ponownie.")
    