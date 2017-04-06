
import turtle

def menu():
	print "Press 1 to make a square"
	print "Press 2 to make a equilateral triangle"
	print "Press 3 to make a star "
	print "Press 4 to make a Hexagon"
	print "Press 5 to make a Octagon"
	print "Press 6 to make a Circle"
	print "Press q to quit "


def square(namef, colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	namef.hideturtle()
	namef.speed(0)
	namef.begin_fill()
	for i in range(4):
		namef.forward(50)
		namef.left(90)
	namef.end_fill()
	wn.exitonclick()


def triangle(namef, colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	for i in range(3):
		namef.forward(50)
		namef.left(120)
	wn.exitonclick()

def star(namef, colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	for i in range(5):
		namef.forward(50)
		namef.left(145)
	wn.exitonclick()

def hexagon(namef, colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	for i in range(6):
		namef.forward(50)
		namef.left(60)
	wn.exitonclick()

def octagon(namef,colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	for i in range(8):
		namef.forward(50)
		namef.left(45)
	wn.exitonclick()

def circle(namef, colorf):
	wn = turtle.Screen()
	namef = turtle.Turtle()
	namef.color(colorf)
	for i in range(360):
		namef.forward(1)
		namef.left(1)
	wn.exitonclick()
def main():
	choice = ''
	print "Hello and welcome to the Shape Creator"
	print "What is your name?"
	name = raw_input()

	print "Okay, " + name +" lets get started"

	print "What is your favorite color?"
	color = raw_input() 

	

	while choice != 'q':
		menu()
		choice = raw_input("what will you choose?")
		if choice == '1':
			square(name, color)
		elif choice == '2':
			triangle(name,color)
		elif choice == '3':
			star(name, color)
		elif choice == '4':
			hexagon(name,color)
		elif choice == '5':
			octagon(name, color)
		elif choice == '6':
			circle(name, color)



main()






