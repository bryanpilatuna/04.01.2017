
a=int(input("Ingrese el numero de lados del Triangulo"))
if(a%2==0):
    b=180/a
    c=b*10
    import turtle
    t= turtle.Pen()
    t.reset()
    for x in range (a):
        t.forward(100)
        t.left(c)
    
else:
    print("Solo funciona para impares")
   

