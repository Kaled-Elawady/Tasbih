
import tkinter as tk

main = tk.Tk()
main.geometry("300x200")
main.resizable(width="False", height="False")

int_var = tk.IntVar()
num = 0
def add_num() :
    global num
    num += 1
    int_var.set(num)
def reset_num():
    global num
    num = 0
    int_var.set(num)

count = tk.Label(main, textvariable=int_var, font=('Times', 30))
add_button = tk.Button(main, text="Add", command=add_num, font=("Times", 30))
reset_button = tk.Button(main, text="Reset", command=reset_num, font=("Times", 30))

count.place(relx=0.5, anchor="n")
add_button.place(relx=0.7, rely=0.5,anchor="center")
reset_button.place(relx=0.3, rely=0.5,anchor="center")

main.mainloop()



