import tkinter as tk

def calculate_price():
    total = 0
    if coffee_type.get() == "Espresso":
        total = 2.0
    elif coffee_type.get() == "Cappuccino":
        total = 3.0
    elif coffee_type.get() == "Latte":
        total = 3.5

    if size.get() == "Large":
        total = total + 1

    if sugar.get():
        total = total + 0.5
    if milk.get():
        total = total + 0.5

    label_price.config(text=f"Total Cost: {total:.2f}€")

root = tk.Tk()
root.title("Order Coffee")
root.geometry("400x400")

coffee_type = tk.StringVar(value="Espresso")
tk.Label(root, text="Choose Coffee: ",font=("Arial",12)).pack()
tk.Radiobutton(root, text="Espresso 2€", variable=coffee_type, value="Espresso").pack()
tk.Radiobutton(root, text="Cappuccino 3€", variable=coffee_type, value="Cappuccino").pack()
tk.Radiobutton(root, text="Latte 3.5€", variable=coffee_type, value="Latte").pack()

size = tk.StringVar(value="Small")
tk.Label(root, text="Size: ", font=("Arial",12)).pack()
spinbox = tk.Spinbox(root, values=("Small","Large"), textvariable=size)
spinbox.pack()

sugar = tk.IntVar()
milk = tk.IntVar()
tk.Checkbutton(root, text="Sugar +0.5€", variable=sugar).pack()
tk.Checkbutton(root, text="Milk +0.5€", variable=milk).pack()

tk.Button(root, text="Calculate Cost", command=calculate_price, font=("Arial",14), bg="brown", fg="white").pack(pady=10)

label_price = tk.Label(root, text="Total Cost: 0.00€", font=("Arial",14))
label_price.pack()



root.mainloop()
