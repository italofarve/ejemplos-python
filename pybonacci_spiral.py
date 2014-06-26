# coding: utf-8
#
# Script Python para generar una espiral de Fibonacci.
# Autor: Italo Farfán Vera

import turtle
import random

def draw_window():
	"""Define parametros de la ventana y llama a la función: draw_spiral().
	"""
	window = turtle.Screen()
	window.bgcolor("white")
	draw_spiral()
	window.getcanvas().postscript(file="1.eps")
	window.exitonclick()

def draw_spiral():
	"""Dibuja la espiral de Fibonacci.
	"""
	# Define parametros de la línea que dibuja la espiral
	mercury = turtle.Turtle()
	mercury.shape("classic")
	# mercury.color("green")
	mercury.pensize(10)
	# Tamaño de la espiral de (6,13)
	for x in range(6,13):
		a = fibonacci(x)
		mercury.color(draw_color(a))
		print a
		mercury.circle(a, 90)

def fibonacci(n):
	"""Genera la sucesión de Fibonacci según el rango (tamaño = range(6,13).
	"""
	fib1 = 0
	fib2 = 1

	if n == 0:
		return fib1
	elif n == 1:
		return fib2
	else:
		for i in range(n-1):
			fib = fib1 + fib2
			fib1 = fib2
			fib2 = fib
	return fib

def draw_color(a):
	"""Colorea usando los colores primareos de forma aleatoría.
	"""
	rgb = (1.0, 1.0, 1.0)
	rounds = (a % 2) + 1
	while(rounds):
		#change tuple to list 
		lst = list(rgb)
		lst[random.randint(0,2)] = 0.0
		rgb = tuple(lst)
		rounds = rounds - 1
	return rgb

draw_window()