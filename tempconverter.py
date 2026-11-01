
from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("700x700")
root.configure(bg="lightblue")

def convert():
    try:
        celsius = float(E1.get())

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        E2.delete(0, END)
        E2.insert(0, str(round(fahrenheit, 2)))

        E3.delete(0, END)
        E3.insert(0, str(round(kelvin, 2)))

    except ValueError:
        E2.delete(0, END)
        E3.delete(0, END)
        E2.insert(0, "Invalid input")
        E3.insert(0, "Invalid input")


def clear():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)


heading = Label(root, text="TEMPERATURE CONVERTER",
                font=("Arial", 22, "bold"),
                bg="lightblue", fg="darkblue")
heading.place(x=150, y=5)


l1 = Label(root, text="Enter temperature in Celsius",
           width=30, height=3, font=("Arial", 16),
           bg="lightblue")
l1.place(x=70, y=70)


E1 = Entry(root, width=20, font=("Arial", 14))
E1.place(x=400, y=85)



b1 = Button(root, text="Convert", width=15, height=3,
            font=("Arial", 16), bg="green",
            fg="white", command=convert)
b1.place(x=300, y=170)


l2 = Label(root, text="Fahrenheit", width=15,
           height=3, font=("Arial", 16),
           bg="lightblue")
l2.place(x=100, y=270)



l3 = Label(root, text="Kelvin", width=15,
           height=3, font=("Arial", 16),
           bg="lightblue")
l3.place(x=400, y=270)



E2 = Entry(root, width=20, font=("Arial", 14))
E2.place(x=100, y=370)

E3 = Entry(root, width=20, font=("Arial", 14))
E3.place(x=400, y=370)



b2 = Button(root, text="Clear", width=15, height=2,
            font=("Arial", 14), bg="red",
            fg="white", command=clear)
b2.place(x=300, y=470)


root.mainloop()
