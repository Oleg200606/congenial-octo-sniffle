import math
def ar(a,b):
    print(a + b)
    print (a - b)
    print (a * b)
    print (a / b)
    print (a ** b)
    print (math.sqrt(a),'            ',     math.sqrt(b))
    print (math.factorial(a),'            ',     math.factorial(b))
    print (math.sin(a),'            ',    math.sin(a))
    print (math.cos(a),'            ',    math.cos(a)) 
    print (math.tan(a),'            ',math.tan(a) )
ar(a = int(input("Введите число: ")), b = int(input("Введите число: ")))