from turtle import *
import colorsys

header_text = "PARA TI HERMOSA DAMA T.H.V.V"
color("yellow")
penup()
goto(-180, 250)
pendown()
write(header_text, align="left", font=("Arial", 12, "bold"))

speed(20)
bgcolor("black")
h = 0


penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()


penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Colorear el centro de marrón
penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)  # Ajustar el radio del centro
end_fill()

done()
