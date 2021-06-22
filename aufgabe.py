__author__ = "DoctorFuchs"
__version__ = "1.0.0"

def sqrt(x:float) -> float: # square root (Quadratwurzel)
    return x*x

def getY(a: float, b: float, c: float, x: float) -> float: # löst die Formal auf
    return (a*sqrt(x)+b*x+c) # hier ist die vorgegebene Formel

if __name__ == "__main__": # startet nur, wenn man die Datei direkt ausführt (ist so üblich bei python)
    #bekommt die inputs vom benutzer
    print("Die Formel ist: y = a*x^2+b*x+c")
    user_a = float(input("a: float = "))
    user_b = float(input("b: float = "))
    user_c = float(input("c: float = "))
    user_n = float(input("n: float = "))
    user_x_min = float(input("x start: float = "))
    user_x_max = float(input("x stop: float = "))
    
    X = user_x_min
    
    # zeichnet die Tabelle
    print("\nX" + 3*"\t" + "Y")
    
    while X <= user_x_max:
        Y = getY(user_a, user_b, user_c, X) #
        
        print(str(round(X*1000)/1000) + 3*"\t" + str(round(Y*1000)/1000)) # rundet die Werte auf die 3. Kommastelle (solange sie nicht 0 sind)

        # hier wird der X-wert erhöht, damit die "while" Schleife endet (erst nach der Berechnung. Sonst kommt es zu Fehlern in der Berechnung)
        X += user_n

# Example output
"""
Die Formel ist: y = a*x^2+b*x+c
a: float = 1
b: float = 2
c: float = 3
n: float = 0.5
x start: float = 1
x stop: float = 5

X                       Y
1.0                     6.0
1.5                     8.25
2.0                     11.0
2.5                     14.25
3.0                     18.0
3.5                     22.25
4.0                     27.0
4.5                     32.25
5.0                     38.0
"""
