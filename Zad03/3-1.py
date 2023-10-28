
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Podany kod jest poprawny składniowo w Pythonie i nie powinno być żadnych błędów. 
# Python nie wymaga średników na końcu linii, 
# ale można ich używać do oddzielenia instrukcji na jednej linii.

#----------------------------------------------------------------


for i in "axby": if ord(i) < 100: print (i)

#Podany kod ma błąd składniowy. W Pythonie, nie można używać instrukcji warunkowej if bez bloku, 
#chyba że jest to (wyrażenie warunkowe(przy instrukcjach prostych można zrezygnować z wcięcia)). 
#Poprawiony kod powinien wyglądać tak:

for i in "axby":
    if ord(i) < 100:
        print(i)
        
#----------------------------------------------------------------

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#Podany kod jest poprawny, korzystamy tutaj z wyrazenia warunkowego;
# if condition: simple_statement
# if condition to for i in "axby":
# simple_statement to print (ord(i) if ord(i) < 100 else i)
# ord(i) if ord(i) < 100 else i to wyrazenie trojargumentowe