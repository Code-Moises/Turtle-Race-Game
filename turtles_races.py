import turtle
import time
import random
import tkinter as tk

# Configuración inicial
ready = ["READY?", "SET", "GO!!!!"]
go = turtle.Turtle()
go.color("black")
go.hideturtle()

one = turtle.Turtle()
one.hideturtle()

meta = 300

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Race")
screen.setup(width=800, height=600)

finishLine = turtle.Turtle()
finishLine.hideturtle()

turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.penup()
turtle1.speed(1)

turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.shape("turtle")
turtle2.color("blue")
turtle2.penup()
turtle2.speed(1)

# Función para mover la tortuga 1
def moveTurtle1():
    adv_t1 = random.randint(3, 20)
    turtle1.forward(adv_t1)
    checkWinner()

# Función para mover la tortuga 2
def moveTurtle2():
    adv_t2 = random.randint(1, 20)
    turtle2.forward(adv_t2)
    checkWinner()

# Verificar si hay un ganador
def checkWinner():
    if turtle1.xcor() >= meta or turtle2.xcor() >= meta:
        declareWinner()

# Declarar al ganador
def declareWinner():
    if turtle2.xcor() > turtle1.xcor():
        go.color("blue")
        go.write("WINNER: TURTLE 2", font=("Arial", 16, "bold"), align="center")
    elif turtle1.xcor() > turtle2.xcor():
        go.color("red")
        go.write("WINNER: TURTLE 1", font=("Arial", 16, "bold"), align="center")
    else:
        go.write("DRAW", font=("Arial", 16, "bold"), align="center")
    time.sleep(1)
    restartGame()

# Reiniciar el juego
def restartGame():
    answer = screen.textinput("Race Again", "Do you want to race again? (y/n)")
    go.clear()
    if answer and answer.lower() == "y":
        resetGame()
    else:
        screen.bye()

# Reiniciar las tortugas y el juego
def resetGame():
    turtle1.goto(-300, -50)
    turtle2.goto(-300, 50)
    turtle1.showturtle()
    turtle2.showturtle()
    go.color("black")
    startGame()

# Modo de un jugador
def onePlayer():
    one.write("You against Python --> press O to move", font=("Arial", 16, "bold"), align="center")
    time.sleep(2)
    one.clear()
    screen.onkey(moveTurtle1, "o")
    screen.listen()
    while turtle1.xcor() < meta and turtle2.xcor() < meta:
        moveTurtle2()
        screen.update()
    one.clear()

# Modo de dos jugadores
def twoPlayers():
    one.write("Player 1 -> W\nPlayer 2 -> O", font=("Arial", 16, "bold"), align="center")
    time.sleep(2)
    one.clear()
    screen.onkey(moveTurtle2, "w")
    screen.onkey(moveTurtle1, "o")
    screen.listen()
    while turtle1.xcor() < meta and turtle2.xcor() < meta:
        screen.update()
    one.clear()

# Centrar la ventana de tkinter
def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Iniciar el juego
def startGame():
    # Configurar la línea de meta
    finishLine.penup()
    finishLine.goto(300, -100)
    finishLine.pendown()
    finishLine.goto(300, 100)

    # Posicionar las tortugas
    turtle1.goto(-300, -50)
    turtle2.goto(-300, 50)
    turtle1.showturtle()
    turtle2.showturtle()

    # Crear la ventana de selección con tkinter
    ventana = tk.Tk()
    ventana.title("CHOOSE")
    ventana.config(bg="lightgray")

    # Centrar la ventana y hacerla más grande
    ancho_ventana = 300
    alto_ventana = 150
    centrar_ventana(ventana, ancho_ventana, alto_ventana)

    etiqueta = tk.Label(ventana, text="Select:", bg="lightgray", font=("Arial", 14))
    etiqueta.pack(pady=10)

    boton_1_jugador = tk.Button(ventana, text="1 Player", command=lambda: seleccionar_jugadores(1, ventana), font=("Arial", 12))
    boton_1_jugador.pack(pady=5)

    boton_2_jugadores = tk.Button(ventana, text="2 Players", command=lambda: seleccionar_jugadores(2, ventana), font=("Arial", 12))
    boton_2_jugadores.pack(pady=5)

    ventana.mainloop()

# Seleccionar el número de jugadores
def seleccionar_jugadores(num_jugadores, ventana):
    ventana.destroy()  # Cerrar la ventana de selección

    # Mostrar mensajes de "READY?", "SET", "GO!!!!"
    for message in ready:
        go.write(message, font=("Arial", 16, "bold"), align="center")
        time.sleep(1)
        go.clear()

    # Iniciar el modo de juego seleccionado
    if num_jugadores == 1:
        onePlayer()
    elif num_jugadores == 2:
        twoPlayers()
    else:
        print("Selección no válida")

# Iniciar el juego por primera vez
startGame()
turtle.mainloop()