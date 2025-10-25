from tkinter import *

def add():
    try:
        result.config(text=f"Result: {float(e1.get()) + float(e2.get())}", fg="yellow")
    except ValueError:
        result.config(text="Enter valid numbers!", fg="red")

root = Tk()
root.title("BCA APPS")
root.geometry("400x300")
root.config(bg="black")

Label(root, text="ARITHMETIC OPERATION", bg="pink", fg="purple", font=("Arial", 18, "bold")).pack(pady=10)
Label(root, text="First Number:", bg="black", fg="white").pack()
e1 = Entry(root); e1.pack()
Label(root, text="Second Number:", bg="black", fg="white").pack()
e2 = Entry(root); e2.pack()
Button(root, text="Add", command=add, bg="blue", fg="white").pack(pady=10)
result = Label(root, text="Result:", bg="black", fg="white", font=("Arial", 12, "bold"))
result.pack(pady=5)

root.mainloop()



