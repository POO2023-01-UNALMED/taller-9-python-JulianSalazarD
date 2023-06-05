from functools import partial
from tkinter import Tk, Button, Entry, END

number_1 = ""
number_2 = ""
operator = None
i = 0

# Configuración ventana principal
root = Tk()
root.title("Calculadora")
root.resizable(0, 0)
root.geometry("295x270")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


def evento(value):
    global number_1, number_2, operator, i
    if i == 0:
        pantalla.delete(0, END)
    if value.isdigit() or value == ".":
        if operator is None:
            number_1 += value
        else:
            number_2 += value
    else:
        operator = value
    pantalla.insert(i, value)
    i += 1


def result():
    global number_1, number_2, operator, i
    r = None
    if operator == "+":
        r = str(float(number_1) + float(number_2))
    elif operator == "-":
        r = float(number_1) - float(number_2)
    elif operator == "*":
        r = float(number_1) * float(number_2)
    elif operator == "/":
        r = float(number_1) / float(number_2)

    pantalla.delete(0, END)
    pantalla.insert(0, r)
    number_1 = ""
    number_2 = ""
    operator = None
    i = 0


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
                 command=partial(evento, "9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",
                     command=partial(result)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,
                     command=partial(evento, ".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
                   command=partial(evento, "+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
                     command=partial(evento, "-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                              cursor="hand2", command=partial(evento, "*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                        cursor="hand2", command=partial(evento, "/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
