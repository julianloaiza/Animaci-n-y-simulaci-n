"""
Julián Andrés Loaiza Ospina
Curso Animación y Simulación 2020-1
Pontificia universidad Javeriana de Cali.

Hoja Fractal con Turtle.
"""
from turtle import *
from collections import deque
import sys
sys.setrecursionlimit(999999)


"""
L-system: 

G = (V, w, P)

V (set) Alfabeto
w (x : V) inicio
P (x -> y..yn) y : V Reglas   

"""
# Reglas


# V = {'0','1','[',']'}
P = {'X':"F+[[X]-X]-F[-FX]+X",'F':"FF",'+':"+",'-':"-",'[':"[",']':"]"}

dq = deque()

def f0(): pass

def f1(): forward(10)

def f2():
	right(25)	

def f3():
	left(25)


def f4():
	dq.append((position(),heading()))

def f5():
	pos,angle = dq.pop()
	penup()
	setposition(pos)
	setheading(angle)
	pendown()

D = {'X':f0,'F':f1,'+':f2,'-':f3,'[':f4,']':f5}

def dibujar(fractal):
	global D
	for x in fractal:
		D[x]()

def generar(lastStr,n):
	global P
	newStr = ""
	if n == 0:
		newStr = lastStr
	else:
		for x in lastStr:
			newStr += P[x]
		newStr = generar(newStr, n-1)
	return newStr

def main():
	n = 5
	w = 'X'
	fractal = generar(w,n)
	speed(1000)
	penup()
	setposition(0,-200)
	setheading(90)
	pendown()

	dibujar(fractal)
	input()

main()