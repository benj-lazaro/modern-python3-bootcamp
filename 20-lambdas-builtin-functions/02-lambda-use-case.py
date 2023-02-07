# Lambda use case demo
# Use case: To pass a function into another function as a parameter & the former function will never be used again
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


# Initially, this function will be passed as a parameter
def say_hi():
    print("Hello!")


def say_bye():
    print("Bye!")


# The function say_hi() is replaced with s lambda statement
# Former default value of the parameter command: 'command=say_hi'
# Removes the need to write a separate function (e.g. say_hi())
button = tk.Button(frame, text="HI", fg="red", command=lambda: print("Hi!"))
button.pack(side=tk.LEFT)

# Using a normal function passed as a parameter
button2 = tk.Button(frame, text="BYE", fg="red", command=say_bye)
button2.pack(side=tk.RIGHT)
root.mainloop()

