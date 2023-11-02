import turtle
import random
import time

s = turtle.Screen()
s.title("Primer proyecto")
s.bgcolor("gray")

#se crean los objetos
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#se ocultan las tortugas para que no se vean antes de la linea de salida
jugador1.hideturtle()
jugador2.hideturtle()

#se modifican las apariencias
jugador1.shape("turtle")
jugador1.color("green", "green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

#se quita la linea para hacer la meta e ir al inicio del jugador 1 y mostrar la tortuga
jugador1.penup()
jugador1.goto(270, 170)
jugador1.pendown()
jugador1.pensize(3)
jugador1.circle(30)
jugador1.penup()
jugador1.goto(-250, 200)
jugador1.pendown()

jugador1.showturtle()

#se quita la linea para hacer la meta e ir al inicio del jugador 2 y mostrar la tortuga
jugador2.penup()
jugador2.goto(270, -230)
jugador2.pendown()
jugador2.circle(30)
jugador2.penup()
jugador2.goto(-250, -200)
jugador2.pendown()
jugador2.showturtle()
time.sleep(2)

#en este while se esta tomando el valor de X y comparando con una posicion y el valor de Y para compararlo con otra
while jugador1.pos() [0] <= 240 and jugador2.pos() [0] <= 240:
    
    print(input("presiona enter para tirar dados."))
    
    #se tiran los dados con un numero aleatorio del 1 al 6
    dados = random.randint(1, 6)
    
    #se avanza la cantidad sacada en los dados multiplicado por 10
    jugador1.fd(dados * 10)
    print(f"sacaste {dados} /n avanzas {dados * 10}")
    
    print(input("presiona enter para tirar dados."))
    
    #se tiran los dados con un numero aleatorio del 1 al 6
    dados = random.randint(1, 6)
    
    #se avanza la cantidad sacada en los dados multiplicado por 10
    jugador2.fd(dados * 10)
    print(f"sacaste {dados} /n avanzas {dados * 10}")    
    
    
if jugador1.pos() >= (240, 200):
    print ("el jugador 1 ha ganado! /n felicidades")
else:
    print ("el jugador 2 ha ganado! /n Felicidades")    

turtle.done()