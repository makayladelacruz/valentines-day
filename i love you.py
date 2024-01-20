import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def exit_application():
    msg_box = tk.messagebox.askquestion('i have a question', 'Will you be my Valentine?',
                                        icon='warning')
    if msg_box == 'yes':
        tk.messagebox.showinfo('Return', 'Yay! I love you < 3')
    else:
        while msg_box== 'no':
            msg_box = tk.messagebox.askquestion(':(', 'Let me ask you again: Will you be my valentine?')
            if msg_box=='yes':
                tk.messagebox.showinfo('Return', 'Yay! I love you < 3')





button1 = tk.Button(root, text='hi baby', command=exit_application, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()